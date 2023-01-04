# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, overload, Callable, Union, Optional, Dict, List
import sys
import logging
import threading
import urllib.parse
import websocket

from ._models import (
    WebPubSubClientOptions,
    OnConnectedArgs,
    OnDisconnectedArgs,
    OnServerDataMessageArgs,
    OnGroupDataMessageArgs,
    OnRejoinGroupFailedArgs,
    SendEventOptions,
    JoinGroupOptions,
    LeaveGroupOptions,
    SendToGroupOptions,
    WebPubSubRetryOptions,
    WebPubSubJsonReliableProtocol,
    SequenceId,
    RetryPolicy,
    WebPubSubGroup,
    SendMessageErrorOptions,
    WebPubSubMessage,
    SendMessageError,
    SendEventMessage,
    SendToGroupMessage,
    AckMessage,
    ConnectedMessage,
    SequenceAckMessage,
    CloseEvent,
    OnRestoreGroupFailedArgs,
    DisconnectedMessage,
    GroupDataMessage,
    ServerDataMessage,
    JoinGroupMessage,
    LeaveGroupMessage,
    AckMessageError,
)
from ._enums import WebPubSubDataType, WebPubSubClientState, CallBackType
from ._util import delay

_LOGGER = logging.getLogger(__name__)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports


class WebPubSubClientCredential:
    @overload
    def __init__(self, client_access_url_provider: str) -> None:
        ...

    @overload
    def __init__(self, client_access_url_provider: Callable[[Any], str]) -> None:
        ...

    def __init__(self, client_access_url_provider: Union[str, Callable]) -> None:
        if isinstance(client_access_url_provider, str):
            self._client_access_url_provider = lambda: client_access_url_provider
        else:
            self._client_access_url_provider = client_access_url_provider

    def get_client_access_url(self) -> str:
        return self._client_access_url_provider()


class WebPubSubClient:
    """WebPubSubClient."""

    @overload
    def __init__(
        self,
        credential: WebPubSubClientCredential,
        options: Optional[WebPubSubClientOptions] = None,
    ) -> None:
        """WebPubSubClient
        :param credential: The credential to use when connecting. Required.
        :type credential: ~azure.webpubsub.client.WebPubSubClientCredential
        :param options: The client options
        :type options: ~azure.webpubsub.client.WebPubSubClientOptions
        """

    @overload
    def __init__(
        self,
        credential: str,
        options: Optional[WebPubSubClientOptions] = None,
    ) -> None:
        """WebPubSubClient
        :param credential: The url to connect. Required.
        :type credential: str
        :param options: The client options
        :type options: ~azure.webpubsub.client.WebPubSubClientOptions
        """

    def __init__(
        self,
        credential: Union[WebPubSubClientCredential, str],
        options: Optional[WebPubSubClientOptions] = None,
    ) -> None:
        if isinstance(credential, WebPubSubClientCredential):
            self._credential = credential
        elif isinstance(credential, str):
            self._credential = WebPubSubClientCredential(credential)
        else:
            raise TypeError("type of credential must be str or WebPubSubClientCredential")

        self._options = options or WebPubSubClientOptions()
        self._build_default_options()
        self._message_retry_policy = RetryPolicy(
            retry_options=self._options.message_retry_options or WebPubSubRetryOptions()
        )
        self._reconnect_retry_policy = RetryPolicy(
            WebPubSubRetryOptions(
                max_retries=sys.maxsize, retry_delay_in_ms=1000, max_retry_delay_in_ms=30000, mode="Fixed"
            )
        )
        self._protocol = self._options.protocol or WebPubSubJsonReliableProtocol()
        self._group_map: Dict[str, WebPubSubGroup] = {}
        self._ack_map: Dict[int, SendMessageErrorOptions] = {}
        self._sequence_id = SequenceId()
        self._state = WebPubSubClientState.STOPPED
        self._ack_id = 0
        self._url = None
        self._ws: Optional[websocket.WebSocketApp] = None
        self._handler: Dict[str, List[Callable]] = {
            CallBackType.CONNECTED: [],
            CallBackType.DISCONNECTED: [],
            CallBackType.REJOIN_GROUP_FAILED: [],
            CallBackType.GROUP_MESSAGE: [],
            CallBackType.SERVER_MESSAGE: [],
            CallBackType.STOPPED: [],
        }
        self._last_disconnected_message: Optional[DisconnectedMessage] = None
        self._connection_id: Optional[str] = None
        self._is_initial_connected = False
        self._is_stopping = False
        self._last_close_event: Optional[CloseEvent] = None
        self._reconnection_token = None
        self._cv: threading.Condition = threading.Condition()
        self._thread_seq_ack: Optional[threading.Thread] = None
        self._thread: Optional[threading.Thread] = None

    def _next_ack_id(self) -> int:
        self._ack_id = self._ack_id + 1
        return self._ack_id

    def _send_message(self, message: WebPubSubMessage):
        pay_load = self._protocol.write_message(message)
        if not self._ws or not self._ws.sock:
            raise Exception("The connection is not connected.")

        self._ws.send(pay_load)

    def _send_message_with_ack_id(
        self,
        message_provider: Callable[[int], WebPubSubMessage],
        ack_id: Optional[int] = None,
    ):
        if ack_id is None:
            ack_id = self._next_ack_id()

        message = message_provider(ack_id)
        if ack_id not in self._ack_map:
            self._ack_map[ack_id] = SendMessageErrorOptions(
                error_detail=AckMessageError(name="", message="timeout to receive ack message")
            )
        try:
            self._send_message(message)
        except Exception as e:
            self._ack_map.pop(ack_id)
            raise e

        # wait for ack from service
        with self._ack_map[ack_id].cv:
            self._ack_map[ack_id].cv.wait(60.0)
            options = self._ack_map.pop(ack_id)
            if options.error_detail is not None:
                raise SendMessageError(
                    message="Failed to send message.", ack_id=options.ack_id, error_detail=options.error_detail
                )

    def _get_or_add_group(self, name: str) -> WebPubSubGroup:
        if name not in self._group_map:
            self._group_map[name] = WebPubSubGroup(name=name)
        return self._group_map[name]

    def join_group(self, group_name: str, options: Optional[JoinGroupOptions] = None):
        """Join the client to group.

        :param group_name: The group name. Required.
        :type group_name: str.
        :param options: The options.
        :type options: azure.webpubsub.client.JoinGroupOptions.
        """

        def join_group_attempt():
            group = self._get_or_add_group(group_name)
            self._join_group_core(group_name, options)
            group.is_joined = True

        self._retry(join_group_attempt)

    def _join_group_core(self, group_name: str, options: Optional[JoinGroupOptions] = None):
        self._send_message_with_ack_id(
            message_provider=lambda id: JoinGroupMessage(group=group_name, ack_id=id),
            ack_id=options.ack_id if options else None,
        )

    def leave_group(self, group_name: str, options: Optional[LeaveGroupOptions] = None):
        """Leave the client from group
        :param group_name: The group name. Required.
        :type group_name: str.
        :param options: The options.
        :type options: azure.webpubsub.client.LeaveGroupOptions.
        """

        def leave_group_attempt():
            group = self._get_or_add_group(group_name)
            self._send_message_with_ack_id(
                message_provider=lambda id: LeaveGroupMessage(group=group_name, ack_id=id),
                ack_id=options.ack_id if options else None,
            )
            group.is_joined = False

        self._retry(leave_group_attempt)

    def send_event(
        self,
        event_name: str,
        content: Any,
        data_type: WebPubSubDataType,
        options: Optional[SendEventOptions] = None,
    ):
        """Send custom event to server
        :param event_name: The event name. Required.
        :type event_name: str.
        :param content: The data content. Required.
        :type content: Any.
        :param data_type: The data type. Required.
        :type data_type: Any.
        :param options: The options.
        :type options: azure.webpubsub.client.SendEventOptions.
        """

        def send_event_attempt():
            fire_and_forget = options.fire_and_forget if options else False
            if not fire_and_forget:
                self._send_message_with_ack_id(
                    message_provider=lambda id: SendEventMessage(
                        data_type=data_type, data=content, ack_id=id, event=event_name
                    )
                )
            else:
                self._send_message(message=SendEventMessage(data_type=data_type, data=content, event=event_name))

        self._retry(send_event_attempt)

    def _send_event_attempt(
        self,
        event_name: str,
        content: Any,
        data_type: WebPubSubDataType,
        options: Optional[SendEventOptions] = None,
    ):
        fire_and_forget = options.fire_and_forget if options else False
        if not fire_and_forget:
            self._send_message_with_ack_id(
                message_provider=lambda id: SendEventMessage(
                    data_type=data_type, data=content, ack_id=id, event=event_name
                )
            )
        else:
            self._send_message(message=SendEventMessage(data_type=data_type, data=content, event=event_name))

    def send_to_group(
        self,
        group_name: str,
        content: Any,
        data_type: WebPubSubDataType,
        options: Optional[SendToGroupOptions] = None,
    ):
        """Send message to group.
        :param group_name: The group name. Required.
        :type group_name: str.
        :param content: The data content. Required.
        :type content: Any.
        :param data_type: The data type. Required.
        :type data_type: Any.
        :param options: The options.
        :type options: azure.webpubsub.client.SendToGroupOptions.
        """

        def send_to_group_attempt():
            fire_and_forget = options.fire_and_forget if options else False
            no_echo = options.no_echo if options else False
            if not fire_and_forget:
                self._send_message_with_ack_id(
                    message_provider=lambda id: SendToGroupMessage(
                        group=group_name, data_type=data_type, data=content, ack_id=id, no_echo=no_echo
                    )
                )
            else:
                self._send_message(
                    message=SendToGroupMessage(group=group_name, data_type=data_type, data=content, no_echo=no_echo)
                )

        self._retry(send_to_group_attempt)

    def _retry(self, func: Callable[[], None]):
        retry_attempt = 0
        while self._ws and self._ws.sock:
            try:
                func()
                return
            except Exception as e:
                retry_attempt = retry_attempt + 1
                delay_in_ms = self._message_retry_policy.next_retry_delay_in_ms(retry_attempt)
                if delay_in_ms is None:
                    raise e
                delay(delay_in_ms)

    def _call_back(self, callback_type: CallBackType, *args):
        for func in self._handler[callback_type]:
            func(*args)

    def _start_from_restarting(self):
        if self._state != WebPubSubClientState.DISCONNECTED:
            _LOGGER.warning("Client can be only restarted when it's Disconnected")
            return

        try:
            self._start_core()
        except Exception as e:
            self._state = WebPubSubClientState.DISCONNECTED
            raise e

    def _auto_reconnect(self):
        success = True
        attempt = 0
        while not self._is_stopping:
            try:
                self._start_from_restarting()
                success = True
                break
            except Exception as e:
                _LOGGER.warning("An attempt to reconnect connection failed %s", e)
                attempt = attempt + 1
                delay_in_ms = self._reconnect_retry_policy.next_retry_delay_in_ms(attempt)
                if not delay_in_ms:
                    break
                delay(delay_in_ms)
        if not success:
            self._handle_connection_stopped()

    def _handle_connection_stopped(self):
        self._is_stopping = False
        self._state = WebPubSubClientState.STOPPED
        self._call_back(CallBackType.STOPPED)

    def _handle_connection_close_and_no_recovery(self):
        self._state = WebPubSubClientState.DISCONNECTED
        self._call_back(
            CallBackType.DISCONNECTED,
            OnDisconnectedArgs(connection_id=self._connection_id, message=self._last_disconnected_message),
        )
        if self._options.auto_reconnect:
            self._auto_reconnect()
        else:
            self._handle_connection_stopped()

    def _build_recovery_url(self):
        if self._connection_id and self._reconnection_token and self._url:
            params = {"awps_connection_id": self._connection_id, "awps_reconnection_token": self._reconnection_token}
            url_parse = urllib.parse.urlparse(self._url)
            url_dict = dict(urllib.parse.parse_qsl(url_parse.query))
            url_dict.update(params)
            new_query = urllib.parse.urlencode(url_dict)
            url_parse = url_parse._replace(query=new_query)
            new_url = urllib.parse.urlunparse(url_parse)
            return new_url
        return None

    def is_connected(self) -> bool:
        """check whether the client is still coneected to server after start"""
        return (
            self._state == WebPubSubClientState.CONNECTED
            and self._thread
            and self._thread.is_alive()
            and self._ws
            and self._ws.sock
        )

    def _connect(self, url: str):
        def on_open(_: Any):
            if self._is_stopping:
                try:
                    if self._ws:
                        self._ws.close()
                finally:
                    return

            self._state = WebPubSubClientState.CONNECTED
            with self._cv:
                self._cv.notify()

        def on_message(_: Any, data: str):
            def handle_ack_message(message: AckMessage):
                if message.ack_id in self._ack_map:
                    if not (message.success or (message.error and message.error.name == "Duplicate")):
                        self._ack_map[message.ack_id].ack_id = message.ack_id
                        self._ack_map[message.ack_id].error_detail = message.error
                    with self._ack_map[message.ack_id].cv:
                        self._ack_map[message.ack_id].cv.notify()

            def handle_connected_message(message: ConnectedMessage):
                self._connection_id = message.connection_id

                if not self._is_initial_connected:
                    self._is_initial_connected = True
                    for group_name, group in self._group_map.items():
                        if group.is_joined:
                            try:
                                self._join_group_core(group_name)
                            except Exception as e:
                                self._call_back(
                                    CallBackType.REJOIN_GROUP_FAILED,
                                    OnRestoreGroupFailedArgs(group=group_name, error=e),
                                )

                    connected_args = OnConnectedArgs(connection_id=message.connection_id, user_id=message.user_id)
                    self._call_back(CallBackType.CONNECTED, connected_args)

            def handle_disconnected_message(message: DisconnectedMessage):
                self._last_disconnected_message = message

            def handle_group_data_message(message: GroupDataMessage):
                if message.sequence_id is not None:
                    if not self._sequence_id.try_update(message.sequence_id):
                        # // drop duplicated message
                        return

                self._call_back(CallBackType.GROUP_MESSAGE, OnGroupDataMessageArgs(message))

            def handle_server_data_message(message: ServerDataMessage):
                if message.sequence_id is not None:
                    if not self._sequence_id.try_update(message.sequence_id):
                        # // drop duplicated message
                        return

                self._call_back(CallBackType.SERVER_MESSAGE, OnServerDataMessageArgs(message))

            parsed_message = self._protocol.parse_messages(data)
            if parsed_message.kind == "connected":
                handle_connected_message(parsed_message)
            elif parsed_message.kind == "disconnected":
                handle_disconnected_message(parsed_message)
            elif parsed_message.kind == "ack":
                handle_ack_message(parsed_message)
            elif parsed_message.kind == "groupData":
                handle_group_data_message(parsed_message)
            elif parsed_message.kind == "serverData":
                handle_server_data_message(parsed_message)
            else:
                raise Exception(f"unknown message type: {parsed_message.kind}")

        def on_close(_: Any, close_status_code: int, close_msg: str):
            self._last_close_event = CloseEvent(close_status_code=close_status_code, close_reason=close_msg)
            # clean ack cache
            self._ack_map.clear()

            if self._is_stopping:
                _LOGGER.warning("The client is stopping state. Stop recovery.")
                self._handle_connection_close_and_no_recovery()
                return

            if self._last_close_event and self._last_close_event.close_status_code == 1008:
                _LOGGER.warning("The websocket close with status code 1008. Stop recovery.")
                self._handle_connection_close_and_no_recovery()
                return

            if not self._protocol.is_reliable_sub_protocol:
                _LOGGER.warning("The protocol is not reliable, recovery is not applicable")
                self._handle_connection_close_and_no_recovery()
                return

            recovery_url = self._build_recovery_url()
            if not recovery_url:
                _LOGGER.warning("Connection id or reconnection token is not available")
                self._handle_connection_close_and_no_recovery()
                return

            self._state = WebPubSubClientState.RECOVERING
            i = 0
            while i < 30 or self._is_stopping:
                try:
                    self._connect(recovery_url)
                    return
                except:
                    delay(1000)
                i = i + 1

            _LOGGER.warning("Recovery attempts failed more then 30 seconds or the client is stopping")
            self._handle_connection_close_and_no_recovery()

        self._ws = websocket.WebSocketApp(
            url=url,
            on_open=on_open,
            on_message=on_message,
            on_close=on_close,
            subprotocols=[self._protocol.name] if self._protocol else [],
        )

        # set thread to start listen to server
        self._thread = threading.Thread(target=self._ws.run_forever)
        self._thread.start()
        with self._cv:
            self._cv.wait(timeout=60.0)
        if not self.is_connected():
            raise Exception("Fail to start client")

        # set thread to check sequence id if needed
        if self._protocol.is_reliable_sub_protocol and (
            (self._thread_seq_ack and not self._thread_seq_ack.is_alive()) or (self._thread_seq_ack is None)
        ):

            def sequence_id_ack_periodically():
                while self.is_connected():
                    try:
                        is_updated, seq_id = self._sequence_id.try_get_sequence_id()
                        if is_updated:
                            self._send_message(SequenceAckMessage(sequence_id=seq_id))
                    finally:
                        delay(1000)

            self._thread_seq_ack = threading.Thread(target=sequence_id_ack_periodically)
            self._thread_seq_ack.start()

    def _start_core(self):
        self._state = WebPubSubClientState.CONNECTING
        _LOGGER.info("Staring a new connection")

        # Reset before a pure new connection
        self._sequence_id.reset()
        self._is_initial_connected = False
        self._last_close_event = None
        self._last_disconnected_message = None
        self._connection_id = None
        self._reconnection_token = None
        self._url = None

        self._url = self._credential.get_client_access_url()
        self._connect(self._url)

    def start(self):
        """start the client and connect to serverice"""

        if self._is_stopping:
            raise Exception("Can't start a client during stopping")
        if self._state != WebPubSubClientState.STOPPED:
            raise Exception("Client can be only started when it's Stopped")

        try:
            self._start_core()
        except Exception as e:
            self._state = WebPubSubClientState.STOPPED
            self._is_stopping = False
            raise e

    def stop(self):
        """stop the client"""

        if self._state == WebPubSubClientState.STOPPED or self._is_stopping:
            return
        self._is_stopping = True
        if self._ws:
            self._ws.close()
        if self._thread_seq_ack and self._thread_seq_ack.is_alive():
            self._thread_seq_ack.join()
        if self._thread and self._thread.is_alive():
            self._thread.join()
        self._thread_seq_ack = None
        self._thread = None

    def _build_default_options(self):
        if self._options.auto_reconnect is None:
            self._options.auto_reconnect = True
        if self._options.auto_restore_groups is None:
            self._options.auto_restore_groups = True
        if self._options.protocol is None:
            self._options.protocol = WebPubSubJsonReliableProtocol()

        self._build_message_retry_options()

    def _build_message_retry_options(self):
        if self._options.message_retry_options is None:
            self._options.message_retry_options = WebPubSubRetryOptions()
        if (
            self._options.message_retry_options.max_retries is None
            or self._options.message_retry_options.max_retries < 0
        ):
            self._options.message_retry_options.max_retries = 3
        if (
            self._options.message_retry_options.retry_delay_in_ms is None
            or self._options.message_retry_options.retry_delay_in_ms < 0
        ):
            self._options.message_retry_options.retry_delay_in_ms = 1000
        if (
            self._options.message_retry_options.max_retry_delay_in_ms is None
            or self._options.message_retry_options.max_retry_delay_in_ms < 0
        ):
            self._options.message_retry_options.max_retry_delay_in_ms = 30000
        if self._options.message_retry_options.mode is None:
            self._options.message_retry_options.mode = "Fixed"

    @overload
    def on(self, event: Literal[CallBackType.CONNECTED], listener: Callable[[OnConnectedArgs], None]) -> None:
        """Add handler for connected event.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def on(self, event: Literal[CallBackType.DISCONNECTED], listener: Callable[[OnDisconnectedArgs], None]) -> None:
        """Add handler for disconnected event.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def on(self, event: Literal[CallBackType.STOPPED], listener: Callable[[], None]) -> None:
        """Add handler for stopped event.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def on(
        self, event: Literal[CallBackType.SERVER_MESSAGE], listener: Callable[[OnServerDataMessageArgs], None]
    ) -> None:
        """Add handler for server messages.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def on(
        self, event: Literal[CallBackType.GROUP_MESSAGE], listener: Callable[[OnGroupDataMessageArgs], None]
    ) -> None:
        """Add handler for group messages.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def on(
        self, event: Literal[CallBackType.REJOIN_GROUP_FAILED], listener: Callable[[OnRejoinGroupFailedArgs], None]
    ) -> None:
        """Add handler for rejoining group failed.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    def on(self, event: CallBackType, listener: Callable) -> None:
        if event in self._handler:
            self._handler[event].append(listener)
        else:
            _LOGGER.error("wrong event type: %s", event)

    @overload
    def off(self, event: Literal[CallBackType.CONNECTED], listener: Callable[[OnConnectedArgs], None]) -> None:
        """Remove handler for connected evnet.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def off(self, event: Literal[CallBackType.DISCONNECTED], listener: Callable[[OnDisconnectedArgs], None]) -> None:
        """Remove handler for connected evnet.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def off(self, event: Literal[CallBackType.STOPPED], listener: Callable[[], None]) -> None:
        """Remove handler for stopped evnet.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def off(
        self, event: Literal[CallBackType.SERVER_MESSAGE], listener: Callable[[OnServerDataMessageArgs], None]
    ) -> None:
        """Remove handler for server message.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def off(
        self, event: Literal[CallBackType.GROUP_MESSAGE], listener: Callable[[OnGroupDataMessageArgs], None]
    ) -> None:
        """Remove handler for group message.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    @overload
    def off(
        self, event: Literal[CallBackType.REJOIN_GROUP_FAILED], listener: Callable[[OnRejoinGroupFailedArgs], None]
    ) -> None:
        """Remove handler for rejoining group failed.
        :param event: The event name. Required.
        :type event: str
        :param listener: The handler
        :type listener: callable.
        """

    def off(self, event: CallBackType, listener: Callable) -> None:
        if event in self._handler:
            if listener in self._handler[event]:
                self._handler[event].remove(listener)
            else:
                _LOGGER.info("target listener does not exist")
        else:
            _LOGGER.error("wrong event type: %s", event)
