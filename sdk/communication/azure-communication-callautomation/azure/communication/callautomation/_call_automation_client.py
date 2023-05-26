# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, Union, Optional, TYPE_CHECKING, Iterable
from urllib.parse import urlparse
from azure.core.tracing.decorator import distributed_trace
from ._version import SDK_MONIKER
from ._api_versions import DEFAULT_VERSION
from ._call_connection_client import CallConnectionClient
from ._generated._client import AzureCommunicationCallAutomationService
from ._shared.utils import (
    get_authentication_policy,
    parse_connection_str
)
from ._generated.models import (
    CreateCallRequest,
    AnswerCallRequest,
    RedirectCallRequest,
    RejectCallRequest,
    StartCallRecordingRequest
)
from ._models import (
    CallConnectionProperties,
    RecordingProperties
)
from ._content_downloader import ContentDownloader
from ._utils import (
    get_repeatability_guid,
    get_repeatability_timestamp,
    serialize_phone_identifier,
    serialize_identifier,
    serialize_communication_user_identifier
)
if TYPE_CHECKING:
    from ._models  import (
        CallInvite,
        ServerCallLocator,
        GroupCallLocator
    )
    from azure.core.credentials import (
        TokenCredential,
        AzureKeyCredential
    )
    from ._shared.models import (
        CommunicationIdentifier,
        CommunicationUserIdentifier,
        PhoneNumberIdentifier
    )
    from ._generated.models._enums import (
        CallRejectReason,
        RecordingContent,
        RecordingChannel,
        RecordingFormat
    )
    from azure.core.exceptions import HttpResponseError

class CallAutomationClient(object):
    """A client to interact with the AzureCommunicationService CallAutomation service.
    Call Automation provides developers the ability to build server-based,
    intelligent call workflows, and call recording for voice and PSTN channels.

    :param endpoint: The endpoint of the Azure Communication resource.
    :type endpoint: str
    :param credential: The access key we use to authenticate against the service.
    :type credential: ~azure.core.credentials.TokenCredential
     or ~azure.core.credentials.AzureKeyCredential
    :keyword api_version: Azure Communication Call Automation API version.
    :paramtype api_version: str
    :keyword source: ACS User Identity to be used when the call is created or answered.
     If not provided, service will generate one.
    :paramtype source: ~azure.communication.callautomation.CommunicationUserIdentifier
    """
    def __init__(
            self,
            endpoint: str,
            credential: Union['TokenCredential', 'AzureKeyCredential'],
            *,
            api_version: Optional[str] = None,
            source: Optional['CommunicationUserIdentifier'] = None,
            **kwargs
    ) -> None:
        if not credential:
            raise ValueError("credential can not be None")

        try:
            if not endpoint.lower().startswith('http'):
                endpoint = "https://" + endpoint
        except AttributeError:
            raise ValueError("Host URL must be a string")

        parsed_url = urlparse(endpoint.rstrip('/'))
        if not parsed_url.netloc:
            raise ValueError(f"Invalid URL: {format(endpoint)}")

        self._client = AzureCommunicationCallAutomationService(
            endpoint,
            api_version=api_version or DEFAULT_VERSION,
            credential=credential,
            authentication_policy=get_authentication_policy(
                 endpoint, credential),
            sdk_moniker=SDK_MONIKER,
            **kwargs)

        self._call_recording_client = self._client.call_recording
        self._downloader = ContentDownloader(self._call_recording_client)
        self.source = source

    @classmethod
    def from_connection_string(
        cls,
        conn_str: str,
        **kwargs
    ) -> 'CallAutomationClient':
        """Create CallAutomation client from a Connection String.

        :param conn_str: A connection string to an Azure Communication Service resource.
        :type conn_str: str
        :return: CallAutomationClient
        :rtype: ~azure.communication.callautomation.CallAutomationClient
        """
        endpoint, access_key = parse_connection_str(conn_str)

        return cls(endpoint, access_key, **kwargs)

    @distributed_trace
    def get_call_connection(
        self,
        call_connection_id: str,
        **kwargs
    ) -> CallConnectionClient:
        """ Get CallConnectionClient object.
        Interact with ongoing call with CallConnectionClient.

        :param call_connection_id: CallConnectionId of ongoing call.
        :type call_connection_id: str
        :return: CallConnectionClient
        :rtype: ~azure.communication.callautomation.CallConnectionClient
        """
        if not call_connection_id:
            raise ValueError("call_connection_id can not be None")

        return CallConnectionClient._from_callautomation_client( #pylint:disable=protected-access
            callautomation_client=self._client,
            call_connection_id=call_connection_id,
            **kwargs)

    @distributed_trace
    def create_call(
        self,
        target_participant: 'CallInvite',
        callback_url: str,
        *,
        operation_context: Optional[str] = None,
        **kwargs
    ) -> CallConnectionProperties:
        """Create a call connection request to a target identity.

        :param target_participant: Call invitee's information.
        :type target_participant: ~azure.communication.callautomation.CallInvite
        :param callback_url: The call back url where callback events are sent.
        :type callback_url: str
        :keyword operation_context: Value that can be used to track the call and its associated events.
        :paramtype operation_context: str
        :return: CallConnectionProperties
        :rtype: ~azure.communication.callautomation.CallConnectionProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        create_call_request = CreateCallRequest(
            targets=[serialize_identifier(target_participant.target)],
            callback_uri=callback_url,
            source_caller_id_number=serialize_phone_identifier(
                target_participant.source_caller_id_number) if target_participant.source_caller_id_number else None,
            source_display_name=target_participant.source_display_name,
            source=serialize_communication_user_identifier(
                self.source) if self.source else None,
            operation_context=operation_context,
        )

        result = self._client.create_call(
            create_call_request=create_call_request,
            **kwargs)

        return CallConnectionProperties._from_generated(# pylint:disable=protected-access
            result)

    @distributed_trace
    def create_group_call(
        self,
        target_participants: List['CommunicationIdentifier'],
        callback_url: str,
        *,
        source_caller_id_number: Optional['PhoneNumberIdentifier'] = None,
        source_display_name: Optional[str] = None,
        operation_context: Optional[str] = None,
        **kwargs
    ) -> CallConnectionProperties:
        """Create a call connection request to a list of multiple target identities.
        This will call all targets simultaneously, and whoever answers the call will join the call.

        :param target_participants: A list of targets.
        :type target_participants: list[~azure.communication.callautomation.CommunicationIdentifier]
        :param callback_url: The call back url for receiving events.
        :type callback_url: str
        :keyword source_caller_id_number: The source caller Id, a phone number,
         that's shown to the PSTN participant being invited.
         Required only when calling a PSTN callee.
        :paramtype source_caller_id_number: ~azure.communication.callautomation.PhoneNumberIdentifier
        :keyword source_display_name: Display name of the caller.
        :paramtype source_display_name: str
        :keyword operation_context: Value that can be used to track the call and its associated events.
        :paramtype operation_context: str
        :return: CallConnectionProperties
        :rtype: ~azure.communication.callautomation.CallConnectionProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        create_call_request = CreateCallRequest(
            targets=[serialize_identifier(identifier)
                     for identifier in target_participants],
            callback_uri=callback_url,
            source_caller_id_number=serialize_phone_identifier(
                source_caller_id_number) if source_caller_id_number else None,
            source_display_name=source_display_name,
            source=serialize_identifier(
                self.source) if self.source else None,
            operation_context=operation_context,
        )

        result = self._client.create_call(
            create_call_request=create_call_request,
            repeatability_first_sent=get_repeatability_timestamp(),
            repeatability_request_id=get_repeatability_guid(),
            **kwargs)

        return CallConnectionProperties._from_generated(# pylint:disable=protected-access
            result)

    @distributed_trace
    def answer_call(
        self,
        incoming_call_context: str,
        callback_url: str,
        *,
        operation_context: Optional[str] = None,
        **kwargs
    ) -> CallConnectionProperties:
        """Answer incoming call with Azure Communication Service's IncomingCall event
        Retrieving IncomingCall event can be set on Azure Communication Service's Azure Portal.

        :param incoming_call_context: This can be read from body of IncomingCall event.
         Use this value to answer incoming call.
        :type incoming_call_context: str
        :param callback_url: The call back url for receiving events.
        :type callback_url: str
        :keyword operation_context: The operation context.
        :paramtype operation_context: str
        :return: CallConnectionProperties
        :rtype: ~azure.communication.callautomation.CallConnectionProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        answer_call_request = AnswerCallRequest(
            incoming_call_context=incoming_call_context,
            callback_uri=callback_url,
            answered_by=serialize_communication_user_identifier(
                self.source) if self.source else None,
            operation_context=operation_context
        )

        result = self._client.answer_call(
            answer_call_request=answer_call_request,
            repeatability_first_sent=get_repeatability_timestamp(),
            repeatability_request_id=get_repeatability_guid(),
            **kwargs)

        return CallConnectionProperties._from_generated(# pylint:disable=protected-access
            result)

    @distributed_trace
    def redirect_call(
        self,
        incoming_call_context: str,
        target_participant: 'CallInvite',
        **kwargs
    ) -> None:
        """Redirect incoming call to a specific target.

        :param incoming_call_context: This can be read from body of IncomingCall event.
         Use this value to redirect incoming call.
        :type incoming_call_context: str
        :param target_participant: The target identity to redirect the call to.
        :type target_participant: ~azure.communication.callautomation.CallInvite
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        redirect_call_request = RedirectCallRequest(
            incoming_call_context=incoming_call_context,
            target=serialize_identifier(target_participant.target),
        )

        self._client.redirect_call(
            redirect_call_request=redirect_call_request,
            repeatability_first_sent=get_repeatability_timestamp(),
            repeatability_request_id=get_repeatability_guid(),
            **kwargs)

    @distributed_trace
    def reject_call(
        self,
        incoming_call_context: str,
        *,
        call_reject_reason: Optional[Union[str,'CallRejectReason']] = None,
        **kwargs
    ) -> None:
        """Reject incoming call.

        :param incoming_call_context: This can be read from body of IncomingCall event.
         Use this value to reject incoming call.
        :type incoming_call_context: str
        :keyword call_reject_reason: The rejection reason.
        :paramtype call_reject_reason: str or ~azure.communication.callautomation.CallRejectReason
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseErrorr:
        """
        reject_call_request = RejectCallRequest(
            incoming_call_context=incoming_call_context,
            call_reject_reason=call_reject_reason
        )

        self._client.reject_call(
            reject_call_request=reject_call_request,
            repeatability_first_sent=get_repeatability_timestamp(),
            repeatability_request_id=get_repeatability_guid(),
            **kwargs)

    @distributed_trace
    def start_recording(
        self,
        call_locator: Union['ServerCallLocator', 'GroupCallLocator'],
        *,
        recording_state_callback_url: Optional[str] = None,
        recording_content_type: Optional[Union[str, 'RecordingContent']] = None,
        recording_channel_type: Optional[Union[str, 'RecordingChannel']] = None,
        recording_format_type: Optional[Union[str, 'RecordingFormat']] = None,
        audio_channel_participant_ordering: Optional[List['CommunicationIdentifier']] = None,
        channel_affinity: Optional[List['ChannelAffinity']] = None,
        **kwargs
    ) -> RecordingProperties:
        """Start recording for a ongoing call. Locate the call with call locator.

        :param call_locator: The call locator to locate ongoing call.
        :type call_locator: ~azure.communication.callautomation.ServerCallLocator
         or ~azure.communication.callautomation.GroupCallLocator
        :keyword recording_state_callback_url: The url to send notifications to.
        :paramtype recording_state_callback_url: str
        :keyword recording_content_type: The content type of call recording.
        :paramtype recording_content_type: str or ~azure.communication.callautomation.RecordingContent
        :keyword recording_channel_type: The channel type of call recording.
        :paramtype recording_channel_type: str or ~azure.communication.callautomation.RecordingChannel
        :keyword recording_format_type: The format type of call recording.
        :paramtype recording_format_type: str or ~azure.communication.callautomation.RecordingFormat
        :keyword audio_channel_participant_ordering:
         The sequential order in which audio channels are assigned to participants in the unmixed recording.
         When 'recordingChannelType' is set to 'unmixed' and `audioChannelParticipantOrdering is not specified,
         the audio channel to participant mapping will be automatically assigned based on the order in
         which participant first audio was detected.
         Channel to participant mapping details can be found in the metadata of the recording.
        :paramtype audio_channel_participant_ordering: list[~azure.communication.callautomation.CommunicationIdentifier]
        :keyword channel_affinity: The channel affinity of call recording
         When 'recordingChannelType' is set to 'unmixed', if channelAffinity is not specified,
         'channel' will be automatically assigned.
         Channel-Participant mapping details can be found in the metadata of the recording.
        :paramtype channel_affinity: list[~azure.communication.callautomation.ChannelAffinity]
        :return: RecordingProperties
        :rtype: ~azure.communication.callautomation.RecordingProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        channel_affinity_internal = []

        if channel_affinity:
            for channel in channel_affinity:
                channel_affinity_internal.append(channel._to_generated(# pylint:disable=protected-access
                    ))

        start_recording_request = StartCallRecordingRequest(
            call_locator=call_locator._to_generated(# pylint:disable=protected-access
            ),
            recording_state_callback_uri = recording_state_callback_url,
            recording_content_type = recording_content_type,
            recording_channel_type = recording_channel_type,
            recording_format_type = recording_format_type,
            audio_channel_participant_ordering = audio_channel_participant_ordering,
            channel_affinity = channel_affinity_internal,
            repeatability_first_sent=get_repeatability_timestamp(),
            repeatability_request_id=get_repeatability_guid()
        )

        recording_state_result = self._call_recording_client.start_recording(
        start_call_recording = start_recording_request, **kwargs)

        return RecordingProperties._from_generated(# pylint:disable=protected-access
            recording_state_result)

    @distributed_trace
    def stop_recording(
        self,
        recording_id: str,
        **kwargs
    ) -> None:
        """Stop recording the call.

        :param recording_id: The recording id.
        :type recording_id: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        self._call_recording_client.stop_recording(recording_id = recording_id, **kwargs)

    @distributed_trace
    def pause_recording(
        self,
        recording_id: str,
        **kwargs
    ) -> None:
        """Pause recording the call.

        :param recording_id: The recording id.
        :type recording_id: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        self._call_recording_client.pause_recording(recording_id = recording_id, **kwargs)

    @distributed_trace
    def resume_recording(
        self,
        recording_id: str,
        **kwargs
    ) -> None:
        """Resume recording the call.

        :param recording_id: The recording id.
        :type recording_id: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        self._call_recording_client.resume_recording(recording_id = recording_id, **kwargs)

    @distributed_trace
    def get_recording_properties(
        self,
        recording_id: str,
        **kwargs
    ) -> RecordingProperties:
        """Get call recording properties and its state.

        :param recording_id: The recording id.
        :type recording_id: str
        :return: RecordingProperties
        :rtype: ~azure.communication.callautomation.RecordingProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        recording_state_result = self._call_recording_client.get_recording_properties(
            recording_id = recording_id, **kwargs)
        return RecordingProperties._from_generated(# pylint:disable=protected-access
            recording_state_result)

    @distributed_trace
    def download_recording(
        self,
        recording_url: str,
        *,
        offset: int = None,
        length: int = None,
        **kwargs
    ) -> Iterable[bytes]:
        """Download a stream of the call recording.

        :param recording_url: Recording's url to be downloaded
        :type recording_url: str
        :param offset: If provided, only download the bytes of the content in the specified range.
         Offset of starting byte.
        :type offset: int
        :param length: If provided, only download the bytes of the content in the specified range.
         Length of the bytes to be downloaded.
        :type length: int
        :return: Iterable[bytes]
        :rtype: Iterable[bytes]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        stream = self._downloader.download_streaming(
            source_location = recording_url,
            offset = offset,
            length = length,
            **kwargs
        )
        return stream

    @distributed_trace
    def delete_recording(
        self,
        recording_url: str,
        **kwargs
    ) -> None:
        """Delete a call recording from given recording url.

        :param recording_url: Recording's url.
        :type recording_url: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        self._downloader.delete_recording(recording_location = recording_url, **kwargs)
