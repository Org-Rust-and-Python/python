# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._quota_operations import (
    build_create_or_update_request,
    build_get_request,
    build_list_request,
    build_update_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class QuotaOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.quota.aio.QuotaMgmtClient`'s
        :attr:`quota` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(self, resource_name: str, scope: str, **kwargs: Any) -> _models.CurrentQuotaLimitBase:
        """Get the quota limit of a resource. The response can be used to determine the remaining quota to
        calculate a new quota limit that can be submitted with a PUT request.

        :param resource_name: Resource name for a given resource provider. For example:


         * SKU name for Microsoft.Compute
         * SKU or TotalLowPriorityCores for Microsoft.MachineLearningServices
           For Microsoft.Network PublicIPAddresses. Required.
        :type resource_name: str
        :param scope: The target Azure resource URI. For example,
         ``/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/qms-test/providers/Microsoft.Batch/batchAccounts/testAccount/``.
         This is the target Azure resource URI for the List GET operation. If a ``{resourceName}`` is
         added after ``/quotas``\ , then it's the target Azure resource URI in the GET operation for the
         specific resource. Required.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CurrentQuotaLimitBase or the result of cls(response)
        :rtype: ~azure.mgmt.quota.models.CurrentQuotaLimitBase
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2023-02-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.CurrentQuotaLimitBase] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_name=resource_name,
            scope=scope,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ExceptionResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

        deserialized = self._deserialize("CurrentQuotaLimitBase", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get.metadata = {"url": "/{scope}/providers/Microsoft.Quota/quotas/{resourceName}"}

    async def _create_or_update_initial(
        self,
        resource_name: str,
        scope: str,
        create_quota_request: Union[_models.CurrentQuotaLimitBase, IO],
        **kwargs: Any
    ) -> Optional[_models.CurrentQuotaLimitBase]:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2023-02-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Optional[_models.CurrentQuotaLimitBase]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_quota_request, (IO, bytes)):
            _content = create_quota_request
        else:
            _json = self._serialize.body(create_quota_request, "CurrentQuotaLimitBase")

        request = build_create_or_update_request(
            resource_name=resource_name,
            scope=scope,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._create_or_update_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ExceptionResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("CurrentQuotaLimitBase", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_initial.metadata = {"url": "/{scope}/providers/Microsoft.Quota/quotas/{resourceName}"}

    @overload
    async def begin_create_or_update(
        self,
        resource_name: str,
        scope: str,
        create_quota_request: _models.CurrentQuotaLimitBase,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.CurrentQuotaLimitBase]:
        """Create or update the quota limit for the specified resource with the requested value. To update
        the quota, follow these steps:


        #. Use the GET operation for quotas and usages to determine how much quota remains for the
        specific resource and to calculate the new quota limit. These steps are detailed in `this
        example
        <https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670>`_.
        #. Use this PUT operation to update the quota limit. Please check the URI in location header
        for the detailed status of the request.

        :param resource_name: Resource name for a given resource provider. For example:


         * SKU name for Microsoft.Compute
         * SKU or TotalLowPriorityCores for Microsoft.MachineLearningServices
           For Microsoft.Network PublicIPAddresses. Required.
        :type resource_name: str
        :param scope: The target Azure resource URI. For example,
         ``/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/qms-test/providers/Microsoft.Batch/batchAccounts/testAccount/``.
         This is the target Azure resource URI for the List GET operation. If a ``{resourceName}`` is
         added after ``/quotas``\ , then it's the target Azure resource URI in the GET operation for the
         specific resource. Required.
        :type scope: str
        :param create_quota_request: Quota request payload. Required.
        :type create_quota_request: ~azure.mgmt.quota.models.CurrentQuotaLimitBase
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either CurrentQuotaLimitBase or the result
         of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.quota.models.CurrentQuotaLimitBase]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_update(
        self,
        resource_name: str,
        scope: str,
        create_quota_request: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.CurrentQuotaLimitBase]:
        """Create or update the quota limit for the specified resource with the requested value. To update
        the quota, follow these steps:


        #. Use the GET operation for quotas and usages to determine how much quota remains for the
        specific resource and to calculate the new quota limit. These steps are detailed in `this
        example
        <https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670>`_.
        #. Use this PUT operation to update the quota limit. Please check the URI in location header
        for the detailed status of the request.

        :param resource_name: Resource name for a given resource provider. For example:


         * SKU name for Microsoft.Compute
         * SKU or TotalLowPriorityCores for Microsoft.MachineLearningServices
           For Microsoft.Network PublicIPAddresses. Required.
        :type resource_name: str
        :param scope: The target Azure resource URI. For example,
         ``/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/qms-test/providers/Microsoft.Batch/batchAccounts/testAccount/``.
         This is the target Azure resource URI for the List GET operation. If a ``{resourceName}`` is
         added after ``/quotas``\ , then it's the target Azure resource URI in the GET operation for the
         specific resource. Required.
        :type scope: str
        :param create_quota_request: Quota request payload. Required.
        :type create_quota_request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either CurrentQuotaLimitBase or the result
         of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.quota.models.CurrentQuotaLimitBase]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create_or_update(
        self,
        resource_name: str,
        scope: str,
        create_quota_request: Union[_models.CurrentQuotaLimitBase, IO],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.CurrentQuotaLimitBase]:
        """Create or update the quota limit for the specified resource with the requested value. To update
        the quota, follow these steps:


        #. Use the GET operation for quotas and usages to determine how much quota remains for the
        specific resource and to calculate the new quota limit. These steps are detailed in `this
        example
        <https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670>`_.
        #. Use this PUT operation to update the quota limit. Please check the URI in location header
        for the detailed status of the request.

        :param resource_name: Resource name for a given resource provider. For example:


         * SKU name for Microsoft.Compute
         * SKU or TotalLowPriorityCores for Microsoft.MachineLearningServices
           For Microsoft.Network PublicIPAddresses. Required.
        :type resource_name: str
        :param scope: The target Azure resource URI. For example,
         ``/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/qms-test/providers/Microsoft.Batch/batchAccounts/testAccount/``.
         This is the target Azure resource URI for the List GET operation. If a ``{resourceName}`` is
         added after ``/quotas``\ , then it's the target Azure resource URI in the GET operation for the
         specific resource. Required.
        :type scope: str
        :param create_quota_request: Quota request payload. Is either a CurrentQuotaLimitBase type or a
         IO type. Required.
        :type create_quota_request: ~azure.mgmt.quota.models.CurrentQuotaLimitBase or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either CurrentQuotaLimitBase or the result
         of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.quota.models.CurrentQuotaLimitBase]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2023-02-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CurrentQuotaLimitBase] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_or_update_initial(
                resource_name=resource_name,
                scope=scope,
                create_quota_request=create_quota_request,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("CurrentQuotaLimitBase", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "original-uri"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_create_or_update.metadata = {"url": "/{scope}/providers/Microsoft.Quota/quotas/{resourceName}"}

    async def _update_initial(
        self,
        resource_name: str,
        scope: str,
        create_quota_request: Union[_models.CurrentQuotaLimitBase, IO],
        **kwargs: Any
    ) -> Optional[_models.CurrentQuotaLimitBase]:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2023-02-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Optional[_models.CurrentQuotaLimitBase]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_quota_request, (IO, bytes)):
            _content = create_quota_request
        else:
            _json = self._serialize.body(create_quota_request, "CurrentQuotaLimitBase")

        request = build_update_request(
            resource_name=resource_name,
            scope=scope,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._update_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ExceptionResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("CurrentQuotaLimitBase", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _update_initial.metadata = {"url": "/{scope}/providers/Microsoft.Quota/quotas/{resourceName}"}

    @overload
    async def begin_update(
        self,
        resource_name: str,
        scope: str,
        create_quota_request: _models.CurrentQuotaLimitBase,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.CurrentQuotaLimitBase]:
        """Update the quota limit for a specific resource to the specified value:


        #. Use the Usages-GET and Quota-GET operations to determine the remaining quota for the
        specific resource and to calculate the new quota limit. These steps are detailed in `this
        example
        <https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670>`_.
        #. Use this PUT operation to update the quota limit. Please check the URI in location header
        for the detailed status of the request.

        :param resource_name: Resource name for a given resource provider. For example:


         * SKU name for Microsoft.Compute
         * SKU or TotalLowPriorityCores for Microsoft.MachineLearningServices
           For Microsoft.Network PublicIPAddresses. Required.
        :type resource_name: str
        :param scope: The target Azure resource URI. For example,
         ``/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/qms-test/providers/Microsoft.Batch/batchAccounts/testAccount/``.
         This is the target Azure resource URI for the List GET operation. If a ``{resourceName}`` is
         added after ``/quotas``\ , then it's the target Azure resource URI in the GET operation for the
         specific resource. Required.
        :type scope: str
        :param create_quota_request: Quota requests payload. Required.
        :type create_quota_request: ~azure.mgmt.quota.models.CurrentQuotaLimitBase
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either CurrentQuotaLimitBase or the result
         of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.quota.models.CurrentQuotaLimitBase]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update(
        self,
        resource_name: str,
        scope: str,
        create_quota_request: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.CurrentQuotaLimitBase]:
        """Update the quota limit for a specific resource to the specified value:


        #. Use the Usages-GET and Quota-GET operations to determine the remaining quota for the
        specific resource and to calculate the new quota limit. These steps are detailed in `this
        example
        <https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670>`_.
        #. Use this PUT operation to update the quota limit. Please check the URI in location header
        for the detailed status of the request.

        :param resource_name: Resource name for a given resource provider. For example:


         * SKU name for Microsoft.Compute
         * SKU or TotalLowPriorityCores for Microsoft.MachineLearningServices
           For Microsoft.Network PublicIPAddresses. Required.
        :type resource_name: str
        :param scope: The target Azure resource URI. For example,
         ``/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/qms-test/providers/Microsoft.Batch/batchAccounts/testAccount/``.
         This is the target Azure resource URI for the List GET operation. If a ``{resourceName}`` is
         added after ``/quotas``\ , then it's the target Azure resource URI in the GET operation for the
         specific resource. Required.
        :type scope: str
        :param create_quota_request: Quota requests payload. Required.
        :type create_quota_request: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either CurrentQuotaLimitBase or the result
         of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.quota.models.CurrentQuotaLimitBase]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_update(
        self,
        resource_name: str,
        scope: str,
        create_quota_request: Union[_models.CurrentQuotaLimitBase, IO],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.CurrentQuotaLimitBase]:
        """Update the quota limit for a specific resource to the specified value:


        #. Use the Usages-GET and Quota-GET operations to determine the remaining quota for the
        specific resource and to calculate the new quota limit. These steps are detailed in `this
        example
        <https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670>`_.
        #. Use this PUT operation to update the quota limit. Please check the URI in location header
        for the detailed status of the request.

        :param resource_name: Resource name for a given resource provider. For example:


         * SKU name for Microsoft.Compute
         * SKU or TotalLowPriorityCores for Microsoft.MachineLearningServices
           For Microsoft.Network PublicIPAddresses. Required.
        :type resource_name: str
        :param scope: The target Azure resource URI. For example,
         ``/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/qms-test/providers/Microsoft.Batch/batchAccounts/testAccount/``.
         This is the target Azure resource URI for the List GET operation. If a ``{resourceName}`` is
         added after ``/quotas``\ , then it's the target Azure resource URI in the GET operation for the
         specific resource. Required.
        :type scope: str
        :param create_quota_request: Quota requests payload. Is either a CurrentQuotaLimitBase type or
         a IO type. Required.
        :type create_quota_request: ~azure.mgmt.quota.models.CurrentQuotaLimitBase or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either CurrentQuotaLimitBase or the result
         of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.quota.models.CurrentQuotaLimitBase]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2023-02-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CurrentQuotaLimitBase] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._update_initial(
                resource_name=resource_name,
                scope=scope,
                create_quota_request=create_quota_request,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("CurrentQuotaLimitBase", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "original-uri"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_update.metadata = {"url": "/{scope}/providers/Microsoft.Quota/quotas/{resourceName}"}

    @distributed_trace
    def list(self, scope: str, **kwargs: Any) -> AsyncIterable["_models.CurrentQuotaLimitBase"]:
        """Get a list of current quota limits of all resources for the specified scope. The response from
        this GET operation can be leveraged to submit requests to update a quota.

        :param scope: The target Azure resource URI. For example,
         ``/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/qms-test/providers/Microsoft.Batch/batchAccounts/testAccount/``.
         This is the target Azure resource URI for the List GET operation. If a ``{resourceName}`` is
         added after ``/quotas``\ , then it's the target Azure resource URI in the GET operation for the
         specific resource. Required.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CurrentQuotaLimitBase or the result of
         cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.quota.models.CurrentQuotaLimitBase]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2023-02-01"] = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )
        cls: ClsType[_models.QuotaLimits] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    scope=scope,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("QuotaLimits", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ExceptionResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/{scope}/providers/Microsoft.Quota/quotas"}
