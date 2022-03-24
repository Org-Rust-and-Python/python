# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Optional, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from . import models
from ._configuration import ManagedServiceIdentityClientConfiguration
from .operations import Operations, SystemAssignedIdentitiesOperations, UserAssignedIdentitiesOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class ManagedServiceIdentityClient:
    """The Managed Service Identity Client.

    :ivar system_assigned_identities: SystemAssignedIdentitiesOperations operations
    :vartype system_assigned_identities:
     azure.mgmt.msi.operations.SystemAssignedIdentitiesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.msi.operations.Operations
    :ivar user_assigned_identities: UserAssignedIdentitiesOperations operations
    :vartype user_assigned_identities: azure.mgmt.msi.operations.UserAssignedIdentitiesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The Id of the Subscription to which the identity belongs.
    :type subscription_id: str
    :param base_url: Service URL. Default value is 'https://management.azure.com'.
    :type base_url: str
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = ManagedServiceIdentityClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.system_assigned_identities = SystemAssignedIdentitiesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.user_assigned_identities = UserAssignedIdentitiesOperations(self._client, self._config, self._serialize, self._deserialize)


    def _send_request(
        self,
        request,  # type: HttpRequest
        **kwargs: Any
    ) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> ManagedServiceIdentityClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
