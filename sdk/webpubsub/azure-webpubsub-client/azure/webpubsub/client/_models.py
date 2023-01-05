# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------


import sys
from typing import Any, Mapping, overload, Union, Optional, TypeVar, Tuple
import json
import math
import threading
import base64

from . import _model_base
from ._model_base import rest_field, AzureJSONEncoder
from ._enums import WebPubSubDataType, UpstreamMessageType

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class JoinGroupMessage:
    def __init__(self, group: str, ack_id: Optional[int] = None) -> None:
        self.kind: Literal["joinGroup"] = "joinGroup"
        self.group = group
        self.ack_id = ack_id


class LeaveGroupMessage:
    def __init__(self, group: str, ack_id: Optional[int] = None) -> None:
        self.kind: Literal["leaveGroup"] = "leaveGroup"
        self.group = group
        self.ack_id = ack_id


class AckMessageError:
    def __init__(self, *, name: str, message: str):
        self.name = name
        self.message = message


class AckMessage:
    def __init__(
        self,
        ack_id: int,
        success: bool,
        error: Optional[AckMessageError] = None,
    ) -> None:
        self.kind: Literal["ack"] = "ack"
        self.ack_id = ack_id
        self.success = success
        self.error = error


class SendEventMessage:
    def __init__(
        self,
        data_type: WebPubSubDataType,
        data: Any,
        event: str,
        ack_id: Optional[int] = None,
    ) -> None:
        self.kind: Literal["sendEvent"] = "sendEvent"
        self.data_type = data_type
        self.data = (data,)
        self.event = event
        self.ack_id = ack_id


class JoinGroupData(_model_base.Model):
    type: Literal["joinGroup"] = rest_field(default="joinGroup")
    group: str = rest_field()
    ack_id: Optional[int] = rest_field(name="ackId")

    @overload
    def __init__(
        self,
        *,
        type: Literal["joinGroup"] = "joinGroup",
        group: str,
        ack_id: Optional[int] = None,
    ) -> None:
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LeaveGroupData(_model_base.Model):
    type: Literal["leaveGroup"] = rest_field(default="leaveGroup")
    group: str = rest_field()
    ack_id: Optional[int] = rest_field(name="ackId")

    @overload
    def __init__(
        self,
        *,
        type: Literal["leaveGroup"] = "leaveGroup",
        group: str,
        ack_id: Optional[int] = None,
    ) -> None:
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SendEventData(_model_base.Model):
    type: Literal["event"] = rest_field(default="event")
    data_type: WebPubSubDataType = rest_field(name="dataType")
    data: Any = rest_field()
    event: str = rest_field()
    ack_id: Optional[int] = rest_field(name="ackId")

    @overload
    def __init__(
        self,
        *,
        type: Literal["event"] = "event",
        data_type: WebPubSubDataType,
        data: Any,
        event: str,
        ack_id: Optional[int] = None,
    ) -> None:
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SendToGroupData(_model_base.Model):
    type: Literal["sendToGroup"] = rest_field(default="sendToGroup")
    group: str = rest_field()
    data_type: WebPubSubDataType = rest_field(name="dataType")
    data: Any = rest_field()
    no_echo: bool = rest_field(name="noEcho")
    ack_id: Optional[int] = rest_field(name="ackId")

    @overload
    def __init__(
        self,
        *,
        type: Literal["sendToGroup"] = "sendToGroup",
        group: str,
        data_type: WebPubSubDataType,
        data: Any,
        no_echo: bool,
        ack_id: Optional[int] = None,
    ) -> None:
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SequenceAckData(_model_base.Model):
    type: Literal["sequenceAck"] = rest_field(default="sequenceAck")
    sequence_id: int = rest_field(name="sequenceId")

    @overload
    def __init__(
        self,
        *,
        type: Literal["sequenceAck"] = "sequenceAck",
        sequence_id: int,
    ) -> None:
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SequenceAckMessage:
    def __init__(
        self,
        sequence_id: int,
    ) -> None:
        self.kind: Literal["sequenceAck"] = "sequenceAck"
        self.sequence_id = sequence_id


class OnConnectedArgs(_model_base.Model):
    connection_id: str = rest_field(name="connectionId")
    user_id: str = rest_field(name="userId")

    @overload
    def __init__(self, *, connection_id: str, user_id: str) -> None:
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ConnectedMessage:
    def __init__(self, connection_id: str, user_id: str, reconnection_token: Optional[str] = None) -> None:
        self.kind: Literal["connected"] = "connected"
        self.connection_id = connection_id
        self.user_id = user_id
        self.reconnection_token = reconnection_token


class DisconnectedMessage:
    def __init__(self, message: str) -> None:
        self.kind: Literal["disconnected"] = "disconnected"
        self.message = message


class GroupDataMessage:
    def __init__(
        self,
        data_type: WebPubSubDataType,
        data: Any,
        group: str,
        from_user_id: str,
        sequence_id: Optional[int] = None,
    ) -> None:
        self.kind: Literal["groupData"] = "groupData"
        self.data_type = data_type
        self.data = data
        self.group = group
        self.from_user_id = from_user_id
        self.sequence_id = sequence_id


class ServerDataMessage:
    def __init__(self, data_type: WebPubSubDataType, data: Any, sequence_id: Optional[int] = None) -> None:
        self.kind: Literal["serverData"] = "serverData"
        self.data_type = data_type
        self.data = data
        self.sequence_id = sequence_id


class SendToGroupMessage:
    def __init__(
        self,
        data_type: WebPubSubDataType,
        data: Any,
        group: str,
        no_echo: bool,
        ack_id: Optional[int] = None,
    ) -> None:
        self.kind: Literal["sendToGroup"] = "sendToGroup"
        self.data_type = data_type
        self.data = data
        self.group = group
        self.no_echo = no_echo
        self.ack_id = ack_id


class OnRestoreGroupFailedArgs:
    def __init__(self, group: str, error: Exception) -> None:
        self.group = group
        self.error = error


WebPubSubMessage = TypeVar(
    "WebPubSubMessage",
    GroupDataMessage,
    ServerDataMessage,
    JoinGroupMessage,
    LeaveGroupMessage,
    ConnectedMessage,
    DisconnectedMessage,
    SendToGroupMessage,
    SendEventMessage,
    SequenceAckMessage,
    AckMessage,
)


def get_pay_load(data: Any, data_type: WebPubSubDataType) -> Any:
    if data_type == WebPubSubDataType.TEXT:
        if not isinstance(data, str):
            raise TypeError("Message must be a string.")
        return data
    if data_type == WebPubSubDataType.JSON:
        return data
    if data_type in (WebPubSubDataType.BINARY, WebPubSubDataType.PROTOBUF):
        if isinstance(data, (bytes, bytearray)):
            return base64.b64encode(data).decode()
        raise TypeError("Message must be a bytes or bytearray")
    raise TypeError(f"Unsupported dataType: {data_type}")


def parse_payload(data: Any, data_type: WebPubSubDataType) -> Any:
    if data_type == WebPubSubDataType.TEXT:
        if not isinstance(data, str):
            raise TypeError("Message must be a string when dataType is text")
        return data
    if data_type == "json":
        return data
    if data_type in ("binary", "protobuf"):
        if isinstance(data, (bytes, bytearray)):
            return data
        return bytes(base64.b64decode(data))
    raise TypeError(f"Unsupported dataType: {data_type}")


class WebPubSubClientProtocol:
    def __init__(self) -> None:
        self.is_reliable_sub_protocol = False
        self.name = ""

    @staticmethod
    def parse_messages(
        raw_message: str,
    ) -> Union[ConnectedMessage, DisconnectedMessage, GroupDataMessage, ServerDataMessage, AckMessage]:
        if raw_message is None:
            raise Exception("No input")
        if not isinstance(raw_message, str):
            raise Exception("Invalid input for JSON hub protocol. Expected a string.")

        message = json.loads(raw_message)
        if message["type"] == "system":
            if message["event"] == "connected":
                return ConnectedMessage(
                    connection_id=message["connectionId"],
                    user_id=message["userId"],
                    reconnection_token=message.get("reconnectionToken"),
                )
            if message["event"] == "disconnected":
                return DisconnectedMessage(message=message["message"])
            raise Exception("wrong message event type: {}".format(message["event"]))
        if message["type"] == "message":
            if message["from"] == "group":
                data = parse_payload(message["data"], message["dataType"])
                return GroupDataMessage(
                    data_type=message["dataType"],
                    data=data,
                    group=message["group"],
                    from_user_id=message["fromUserId"],
                    sequence_id=message.get("sequenceId"),
                )
            if message["from"] == "server":
                data = parse_payload(message["data"], message["dataType"])
                return ServerDataMessage(
                    data=data, data_type=message["dataType"], sequence_id=message.get("sequenceId")
                )
            raise Exception("wrong message from: {}".format(message["from"]))
        if message["type"] == "ack":
            return AckMessage(
                ack_id=message["ackId"],
                success=message["success"],
                error=message.get("error"),
            )
        raise Exception("wrong message type: {}".format(message["type"]))

    @staticmethod
    def write_message(message: WebPubSubMessage) -> str:
        if message.kind == UpstreamMessageType.JOIN_GROUP:
            data = JoinGroupData(group=message.group, ack_id=message.ack_id)
        elif message.kind == UpstreamMessageType.LEAVE_GROUP:
            data = LeaveGroupData(group=message.group, ack_id=message.ack_id)
        elif message.kind == UpstreamMessageType.SEND_EVENT:
            data = SendEventData(
                event=message.event,
                ack_id=message.ack_id,
                data_type=message.data_type,
                data=get_pay_load(message.data, message.data_type),
            )
        elif message.kind == UpstreamMessageType.SEND_TO_GROUP:
            data = SendToGroupData(
                group=message.group,
                ack_id=message.ack_id,
                data_type=message.data_type,
                data=get_pay_load(message.data, message.data_type),
                no_echo=message.no_echo,
            )
        elif message.kind == UpstreamMessageType.SEQUENCE_ACK:
            data = SequenceAckData(sequence_id=message.sequence_id)
        else:
            raise Exception(f"Unsupported type: {message.kind}")

        return json.dumps(data, cls=AzureJSONEncoder)


class WebPubSubJsonProtocol(WebPubSubClientProtocol):
    def __init__(self) -> None:
        super().__init__()
        self.is_reliable_sub_protocol = False
        self.name = "json.webpubsub.azure.v1"


class WebPubSubJsonReliableProtocol(WebPubSubClientProtocol):
    def __init__(self) -> None:
        super().__init__()
        self.is_reliable_sub_protocol = True
        self.name = "json.reliable.webpubsub.azure.v1"


class WebPubSubRetryOptions:
    def __init__(
        self,
        max_retries: int = sys.maxsize,
        retry_delay_in_ms: int = 1000,
        max_retry_delay_in_ms: int = 30000,
        mode: Literal["Exponential", "Fixed"] = "Fixed",
    ) -> None:
        self.max_retries = max_retries
        self.retry_delay_in_ms = retry_delay_in_ms
        self.max_retry_delay_in_ms = max_retry_delay_in_ms
        self.mode = mode


class WebPubSubClientOptions:
    def __init__(
        self,
        protocol: Optional[WebPubSubClientProtocol] = None,
        auto_reconnect: Optional[bool] = None,
        auto_restore_groups: Optional[bool] = None,
        message_retry_options: Optional[WebPubSubRetryOptions] = None,
    ) -> None:
        self.protocol = protocol
        self.auto_reconnect = auto_reconnect
        self.auto_restore_groups = auto_restore_groups
        self.message_retry_options = message_retry_options


class SendMessageErrorOptions:
    def __init__(self, ack_id: Optional[int] = None, error_detail: Optional[AckMessageError] = None) -> None:
        self.ack_id = ack_id
        self.error_detail = error_detail
        self.cv = threading.Condition()


class SendMessageError(Exception):
    def __init__(
        self, message: str, ack_id: Optional[int] = None, error_detail: Optional[AckMessageError] = None
    ) -> None:
        super().__init__(message)
        self.name = "SendMessageError"
        self.ack_id = ack_id
        self.error_detail = error_detail


class OnGroupDataMessageArgs:
    def __init__(self, message: GroupDataMessage) -> None:
        self.message = message


class OnServerDataMessageArgs:
    def __init__(self, message: ServerDataMessage) -> None:
        self.message = message


class CloseEvent:
    def __init__(self, close_status_code: Optional[int] = None, close_reason: Optional[str] = None) -> None:
        self.close_status_code = close_status_code
        self.close_reason = close_reason


class OnDisconnectedArgs:
    def __init__(self, connection_id: Optional[str] = None, message: Optional[DisconnectedMessage] = None) -> None:
        self.connection_id = connection_id
        self.message = message


class OnRejoinGroupFailedArgs:
    def __init__(self, group: str, error: Exception) -> None:
        self.group = group
        self.error = error


class SendToGroupOptions:
    def __init__(self, no_echo: bool, fire_and_forget: bool, ack_id: Optional[int] = None) -> None:
        self.no_echo = no_echo
        self.fire_and_forget = fire_and_forget
        self.ack_id = ack_id


class SendEventOptions:
    def __init__(self, fire_and_forget: bool, ack_id: Optional[int] = None) -> None:
        self.fire_and_forget = fire_and_forget
        self.ack_id = ack_id


class JoinGroupOptions:
    def __init__(self, ack_id: Optional[int] = None) -> None:
        self.ack_id = ack_id


class LeaveGroupOptions:
    def __init__(self, ack_id: Optional[int] = None) -> None:
        self.ack_id = ack_id


class RetryPolicy:
    def __init__(self, retry_options: WebPubSubRetryOptions) -> None:
        self.retry_options = retry_options
        self.max_retries_to_get_max_delay = math.ceil(
            math.log2(self.retry_options.max_retry_delay_in_ms or 1)
            - math.log2(self.retry_options.retry_delay_in_ms or 1)
            + 1
        )

    def next_retry_delay_in_ms(self, retry_attempt: int) -> Union[int, None]:
        if retry_attempt > self.retry_options.max_retries:
            return None
        if self.retry_options.mode == "Fixed":
            return self.retry_options.retry_delay_in_ms
        return self.calculate_exponential_delay(retry_attempt)

    def calculate_exponential_delay(self, attempt: int) -> int:
        if attempt >= self.max_retries_to_get_max_delay:
            return self.retry_options.max_retry_delay_in_ms
        return (1 << (attempt - 1)) * self.retry_options.retry_delay_in_ms


class WebPubSubGroup:
    def __init__(self, name: str) -> None:
        self.name = name
        self.is_joined = False


class SequenceId:
    def __init__(self) -> None:
        self.sequence_id = 0
        self.is_update = False

    def try_update(self, sequence_id: int) -> bool:
        self.is_update = True
        if sequence_id > self.sequence_id:
            self.sequence_id = sequence_id
            return True
        return False

    def try_get_sequence_id(self) -> Tuple[bool, Union[int, None]]:
        if self.is_update:
            self.is_update = False
            return (True, self.sequence_id)
        return (False, None)

    def reset(self):
        self.sequence_id = 0
        self.is_update = False
