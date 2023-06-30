# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
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
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._log_profiles_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class LogProfilesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.monitor.v2016_03_01.aio.MonitorManagementClient`'s
        :attr:`log_profiles` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, log_profile_name: str, **kwargs: Any
    ) -> None:
        """Deletes the log profile.

        :param log_profile_name: The name of the log profile. Required.
        :type log_profile_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2016-03-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            log_profile_name=log_profile_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Insights/logprofiles/{logProfileName}"
    }

    @distributed_trace_async
    async def get(self, log_profile_name: str, **kwargs: Any) -> _models.LogProfileResource:
        """Gets the log profile.

        :param log_profile_name: The name of the log profile. Required.
        :type log_profile_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LogProfileResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2016_03_01.models.LogProfileResource
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2016-03-01"))
        cls: ClsType[_models.LogProfileResource] = kwargs.pop("cls", None)

        request = build_get_request(
            log_profile_name=log_profile_name,
            subscription_id=self._config.subscription_id,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("LogProfileResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Insights/logprofiles/{logProfileName}"}

    @overload
    async def create_or_update(
        self,
        log_profile_name: str,
        parameters: _models.LogProfileResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.LogProfileResource:
        """Create or update a log profile in Azure Monitoring REST API.

        :param log_profile_name: The name of the log profile. Required.
        :type log_profile_name: str
        :param parameters: Parameters supplied to the operation. Required.
        :type parameters: ~azure.mgmt.monitor.v2016_03_01.models.LogProfileResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LogProfileResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2016_03_01.models.LogProfileResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self, log_profile_name: str, parameters: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.LogProfileResource:
        """Create or update a log profile in Azure Monitoring REST API.

        :param log_profile_name: The name of the log profile. Required.
        :type log_profile_name: str
        :param parameters: Parameters supplied to the operation. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LogProfileResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2016_03_01.models.LogProfileResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self, log_profile_name: str, parameters: Union[_models.LogProfileResource, IO], **kwargs: Any
    ) -> _models.LogProfileResource:
        """Create or update a log profile in Azure Monitoring REST API.

        :param log_profile_name: The name of the log profile. Required.
        :type log_profile_name: str
        :param parameters: Parameters supplied to the operation. Is either a LogProfileResource type or
         a IO type. Required.
        :type parameters: ~azure.mgmt.monitor.v2016_03_01.models.LogProfileResource or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LogProfileResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2016_03_01.models.LogProfileResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2016-03-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.LogProfileResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "LogProfileResource")

        request = build_create_or_update_request(
            log_profile_name=log_profile_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("LogProfileResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Insights/logprofiles/{logProfileName}"
    }

    @overload
    async def update(
        self,
        log_profile_name: str,
        log_profiles_resource: _models.LogProfileResourcePatch,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.LogProfileResource:
        """Updates an existing LogProfilesResource. To update other fields use the CreateOrUpdate method.

        :param log_profile_name: The name of the log profile. Required.
        :type log_profile_name: str
        :param log_profiles_resource: Parameters supplied to the operation. Required.
        :type log_profiles_resource: ~azure.mgmt.monitor.v2016_03_01.models.LogProfileResourcePatch
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LogProfileResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2016_03_01.models.LogProfileResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, log_profile_name: str, log_profiles_resource: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.LogProfileResource:
        """Updates an existing LogProfilesResource. To update other fields use the CreateOrUpdate method.

        :param log_profile_name: The name of the log profile. Required.
        :type log_profile_name: str
        :param log_profiles_resource: Parameters supplied to the operation. Required.
        :type log_profiles_resource: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LogProfileResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2016_03_01.models.LogProfileResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self, log_profile_name: str, log_profiles_resource: Union[_models.LogProfileResourcePatch, IO], **kwargs: Any
    ) -> _models.LogProfileResource:
        """Updates an existing LogProfilesResource. To update other fields use the CreateOrUpdate method.

        :param log_profile_name: The name of the log profile. Required.
        :type log_profile_name: str
        :param log_profiles_resource: Parameters supplied to the operation. Is either a
         LogProfileResourcePatch type or a IO type. Required.
        :type log_profiles_resource: ~azure.mgmt.monitor.v2016_03_01.models.LogProfileResourcePatch or
         IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LogProfileResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2016_03_01.models.LogProfileResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2016-03-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.LogProfileResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(log_profiles_resource, (IO, bytes)):
            _content = log_profiles_resource
        else:
            _json = self._serialize.body(log_profiles_resource, "LogProfileResourcePatch")

        request = build_update_request(
            log_profile_name=log_profile_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("LogProfileResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Insights/logprofiles/{logProfileName}"
    }

    @distributed_trace
    def list(self, **kwargs: Any) -> AsyncIterable["_models.LogProfileResource"]:
        """List the log profiles.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either LogProfileResource or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.monitor.v2016_03_01.models.LogProfileResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2016-03-01"))
        cls: ClsType[_models.LogProfileCollection] = kwargs.pop("cls", None)

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
                    subscription_id=self._config.subscription_id,
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
            deserialized = self._deserialize("LogProfileCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Insights/logprofiles"}
