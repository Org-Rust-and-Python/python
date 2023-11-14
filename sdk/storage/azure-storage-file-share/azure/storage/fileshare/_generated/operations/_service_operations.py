# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_set_properties_request(
    url: str, *, content: Any, timeout: Optional[int] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    restype: Literal["service"] = kwargs.pop("restype", _params.pop("restype", "service"))
    comp: Literal["properties"] = kwargs.pop("comp", _params.pop("comp", "properties"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    version: Literal["2024-02-04"] = kwargs.pop("version", _headers.pop("x-ms-version", "2024-02-04"))
    accept = _headers.pop("Accept", "application/xml")

    # Construct URL
    _url = kwargs.pop("template_url", "{url}")
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, "str", skip_quote=True),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["restype"] = _SERIALIZER.query("restype", restype, "str")
    _params["comp"] = _SERIALIZER.query("comp", comp, "str")
    if timeout is not None:
        _params["timeout"] = _SERIALIZER.query("timeout", timeout, "int", minimum=0)

    # Construct headers
    _headers["x-ms-version"] = _SERIALIZER.header("version", version, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, content=content, **kwargs)


def build_get_properties_request(url: str, *, timeout: Optional[int] = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    restype: Literal["service"] = kwargs.pop("restype", _params.pop("restype", "service"))
    comp: Literal["properties"] = kwargs.pop("comp", _params.pop("comp", "properties"))
    version: Literal["2024-02-04"] = kwargs.pop("version", _headers.pop("x-ms-version", "2024-02-04"))
    accept = _headers.pop("Accept", "application/xml")

    # Construct URL
    _url = kwargs.pop("template_url", "{url}")
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, "str", skip_quote=True),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["restype"] = _SERIALIZER.query("restype", restype, "str")
    _params["comp"] = _SERIALIZER.query("comp", comp, "str")
    if timeout is not None:
        _params["timeout"] = _SERIALIZER.query("timeout", timeout, "int", minimum=0)

    # Construct headers
    _headers["x-ms-version"] = _SERIALIZER.header("version", version, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_shares_segment_request(
    url: str,
    *,
    prefix: Optional[str] = None,
    marker: Optional[str] = None,
    maxresults: Optional[int] = None,
    include: Optional[List[Union[str, _models.ListSharesIncludeType]]] = None,
    timeout: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    comp: Literal["list"] = kwargs.pop("comp", _params.pop("comp", "list"))
    version: Literal["2024-02-04"] = kwargs.pop("version", _headers.pop("x-ms-version", "2024-02-04"))
    accept = _headers.pop("Accept", "application/xml")

    # Construct URL
    _url = kwargs.pop("template_url", "{url}")
    path_format_arguments = {
        "url": _SERIALIZER.url("url", url, "str", skip_quote=True),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["comp"] = _SERIALIZER.query("comp", comp, "str")
    if prefix is not None:
        _params["prefix"] = _SERIALIZER.query("prefix", prefix, "str")
    if marker is not None:
        _params["marker"] = _SERIALIZER.query("marker", marker, "str")
    if maxresults is not None:
        _params["maxresults"] = _SERIALIZER.query("maxresults", maxresults, "int", minimum=1)
    if include is not None:
        _params["include"] = _SERIALIZER.query("include", include, "[str]", div=",")
    if timeout is not None:
        _params["timeout"] = _SERIALIZER.query("timeout", timeout, "int", minimum=0)

    # Construct headers
    _headers["x-ms-version"] = _SERIALIZER.header("version", version, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class ServiceOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.fileshare.AzureFileStorage`'s
        :attr:`service` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def set_properties(  # pylint: disable=inconsistent-return-statements
        self, storage_service_properties: _models.StorageServiceProperties, timeout: Optional[int] = None, **kwargs: Any
    ) -> None:
        """Sets properties for a storage account's File service endpoint, including properties for Storage
        Analytics metrics and CORS (Cross-Origin Resource Sharing) rules.

        :param storage_service_properties: The StorageService properties. Required.
        :type storage_service_properties: ~azure.storage.fileshare.models.StorageServiceProperties
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>`. Default value is None.
        :type timeout: int
        :keyword restype: restype. Default value is "service". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "properties". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
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

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        restype: Literal["service"] = kwargs.pop("restype", _params.pop("restype", "service"))
        comp: Literal["properties"] = kwargs.pop("comp", _params.pop("comp", "properties"))
        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/xml"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _content = self._serialize.body(storage_service_properties, "StorageServiceProperties", is_xml=True)

        _request = build_set_properties_request(
            url=self._config.url,
            timeout=timeout,
            restype=restype,
            comp=comp,
            content_type=content_type,
            version=self._config.version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    @distributed_trace
    def get_properties(self, timeout: Optional[int] = None, **kwargs: Any) -> _models.StorageServiceProperties:
        """Gets the properties of a storage account's File service, including properties for Storage
        Analytics metrics and CORS (Cross-Origin Resource Sharing) rules.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>`. Default value is None.
        :type timeout: int
        :keyword restype: restype. Default value is "service". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype restype: str
        :keyword comp: comp. Default value is "properties". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StorageServiceProperties or the result of cls(response)
        :rtype: ~azure.storage.fileshare.models.StorageServiceProperties
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

        restype: Literal["service"] = kwargs.pop("restype", _params.pop("restype", "service"))
        comp: Literal["properties"] = kwargs.pop("comp", _params.pop("comp", "properties"))
        cls: ClsType[_models.StorageServiceProperties] = kwargs.pop("cls", None)

        _request = build_get_properties_request(
            url=self._config.url,
            timeout=timeout,
            restype=restype,
            comp=comp,
            version=self._config.version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))

        deserialized = self._deserialize("StorageServiceProperties", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list_shares_segment(
        self,
        prefix: Optional[str] = None,
        marker: Optional[str] = None,
        maxresults: Optional[int] = None,
        include: Optional[List[Union[str, _models.ListSharesIncludeType]]] = None,
        timeout: Optional[int] = None,
        **kwargs: Any
    ) -> _models.ListSharesResponse:
        """The List Shares Segment operation returns a list of the shares and share snapshots under the
        specified account.

        :param prefix: Filters the results to return only entries whose name begins with the specified
         prefix. Default value is None.
        :type prefix: str
        :param marker: A string value that identifies the portion of the list to be returned with the
         next list operation. The operation returns a marker value within the response body if the list
         returned was not complete. The marker value may then be used in a subsequent call to request
         the next set of list items. The marker value is opaque to the client. Default value is None.
        :type marker: str
        :param maxresults: Specifies the maximum number of entries to return. If the request does not
         specify maxresults, or specifies a value greater than 5,000, the server will return up to 5,000
         items. Default value is None.
        :type maxresults: int
        :param include: Include this parameter to specify one or more datasets to include in the
         response. Default value is None.
        :type include: list[str or ~azure.storage.fileshare.models.ListSharesIncludeType]
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>`. Default value is None.
        :type timeout: int
        :keyword comp: comp. Default value is "list". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ListSharesResponse or the result of cls(response)
        :rtype: ~azure.storage.fileshare.models.ListSharesResponse
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

        comp: Literal["list"] = kwargs.pop("comp", _params.pop("comp", "list"))
        cls: ClsType[_models.ListSharesResponse] = kwargs.pop("cls", None)

        _request = build_list_shares_segment_request(
            url=self._config.url,
            prefix=prefix,
            marker=marker,
            maxresults=maxresults,
            include=include,
            timeout=timeout,
            comp=comp,
            version=self._config.version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))

        deserialized = self._deserialize("ListSharesResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore
