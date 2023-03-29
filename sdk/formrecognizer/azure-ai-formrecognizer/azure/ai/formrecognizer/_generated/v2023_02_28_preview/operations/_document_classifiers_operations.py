# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, cast

from msrest import Serializer

from ...._polling import DocumentModelAdministrationClientLROPoller
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.polling.base_polling import LROBasePolling
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_build_classifier_request_initial(
    *,
    json: Optional[_models.BuildDocumentClassifierRequest] = None,
    content: Any = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-02-28-preview"))  # type: str
    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/documentClassifiers:build")

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_params,
        headers=_headers,
        json=json,
        content=content,
        **kwargs
    )


def build_list_classifiers_request(
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-02-28-preview"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/documentClassifiers")

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_classifier_request(
    classifier_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-02-28-preview"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/documentClassifiers/{classifierId}")
    path_format_arguments = {
        "classifierId": _SERIALIZER.url("classifier_id", classifier_id, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9._~-]{1,63}$'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_delete_classifier_request(
    classifier_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-02-28-preview"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/documentClassifiers/{classifierId}")
    path_format_arguments = {
        "classifierId": _SERIALIZER.url("classifier_id", classifier_id, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9._~-]{1,63}$'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_classify_document_request_initial(
    classifier_id: str,
    *,
    json: Optional[_models.ClassifyDocumentRequest] = None,
    content: Any = None,
    string_index_type: Optional[Union[str, "_models.StringIndexType"]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-02-28-preview"))  # type: str
    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[Union[str, "_models.ContentType"]]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/documentClassifiers/{classifierId}:analyze")
    path_format_arguments = {
        "classifierId": _SERIALIZER.url("classifier_id", classifier_id, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9._~-]{1,63}$'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if string_index_type is not None:
        _params['stringIndexType'] = _SERIALIZER.query("string_index_type", string_index_type, 'str')
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_params,
        headers=_headers,
        json=json,
        content=content,
        **kwargs
    )


def build_get_classify_result_request(
    classifier_id: str,
    result_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-02-28-preview"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/documentClassifiers/{classifierId}/analyzeResults/{resultId}")
    path_format_arguments = {
        "classifierId": _SERIALIZER.url("classifier_id", classifier_id, 'str', max_length=64, min_length=0, pattern=r'^[a-zA-Z0-9][a-zA-Z0-9._~-]{1,63}$'),
        "resultId": _SERIALIZER.url("result_id", result_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )

class DocumentClassifiersOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.ai.formrecognizer.v2023_02_28_preview.FormRecognizerClient`'s
        :attr:`document_classifiers` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    def _build_classifier_initial(  # pylint: disable=inconsistent-return-statements
        self,
        build_request: _models.BuildDocumentClassifierRequest,
        **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-02-28-preview"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        _json = self._serialize.body(build_request, 'BuildDocumentClassifierRequest')

        request = build_build_classifier_request_initial(
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._build_classifier_initial.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['Operation-Location']=self._deserialize('str', response.headers.get('Operation-Location'))


        if cls:
            return cls(pipeline_response, None, response_headers)

    _build_classifier_initial.metadata = {'url': "/documentClassifiers:build"}  # type: ignore


    @distributed_trace
    def begin_build_classifier(  # pylint: disable=inconsistent-return-statements
        self,
        build_request: _models.BuildDocumentClassifierRequest,
        **kwargs: Any
    ) -> DocumentModelAdministrationClientLROPoller[None]:
        """Build document classifier.

        Builds a custom document classifier.

        :param build_request: Building request parameters.
        :type build_request:
         ~azure.ai.formrecognizer.v2023_02_28_preview.models.BuildDocumentClassifierRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of DocumentModelAdministrationClientLROPoller that returns either None or
         the result of cls(response)
        :rtype: ~...._polling.DocumentModelAdministrationClientLROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-02-28-preview"))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', "application/json"))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._build_classifier_initial(  # type: ignore
                build_request=build_request,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x,y,z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})


        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        if polling is True:
            polling_method = cast(PollingMethod, LROBasePolling(
                lro_delay,
                
                path_format_arguments=path_format_arguments,
                **kwargs
        ))  # type: PollingMethod
        elif polling is False: polling_method = cast(PollingMethod, NoPolling())
        else: polling_method = polling
        if cont_token:
            return DocumentModelAdministrationClientLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return DocumentModelAdministrationClientLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_build_classifier.metadata = {'url': "/documentClassifiers:build"}  # type: ignore

    @distributed_trace
    def list_classifiers(
        self,
        **kwargs: Any
    ) -> Iterable[_models.GetDocumentClassifiersResponse]:
        """List document classifiers.

        List all document classifiers.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either GetDocumentClassifiersResponse or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.ai.formrecognizer.v2023_02_28_preview.models.GetDocumentClassifiersResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-02-28-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.GetDocumentClassifiersResponse]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_classifiers_request(
                    api_version=api_version,
                    template_url=self.list_classifiers.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

            else:
                
                request = build_list_classifiers_request(
                    api_version=api_version,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("GetDocumentClassifiersResponse", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_classifiers.metadata = {'url': "/documentClassifiers"}  # type: ignore

    @distributed_trace
    def get_classifier(
        self,
        classifier_id: str,
        **kwargs: Any
    ) -> _models.DocumentClassifierDetails:
        """Get document classifier.

        Gets detailed document classifier information.

        :param classifier_id: Unique document classifier name.
        :type classifier_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DocumentClassifierDetails, or the result of cls(response)
        :rtype: ~azure.ai.formrecognizer.v2023_02_28_preview.models.DocumentClassifierDetails
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-02-28-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.DocumentClassifierDetails]

        
        request = build_get_classifier_request(
            classifier_id=classifier_id,
            api_version=api_version,
            template_url=self.get_classifier.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('DocumentClassifierDetails', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_classifier.metadata = {'url': "/documentClassifiers/{classifierId}"}  # type: ignore


    @distributed_trace
    def delete_classifier(  # pylint: disable=inconsistent-return-statements
        self,
        classifier_id: str,
        **kwargs: Any
    ) -> None:
        """Delete document classifier.

        Deletes document classifier.

        :param classifier_id: Unique document classifier name.
        :type classifier_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-02-28-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_delete_classifier_request(
            classifier_id=classifier_id,
            api_version=api_version,
            template_url=self.delete_classifier.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete_classifier.metadata = {'url': "/documentClassifiers/{classifierId}"}  # type: ignore


    def _classify_document_initial(  # pylint: disable=inconsistent-return-statements
        self,
        classifier_id: str,
        string_index_type: Optional[Union[str, "_models.StringIndexType"]] = None,
        classify_request: Optional[Union[IO, str, _models.ClassifyDocumentRequest]] = None,
        *,
        content_type: Optional[Union[str, "_models.ContentType"]] = "application/json",
        **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-02-28-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        _json = None
        _content = None
        content_type = content_type or ""
        if content_type.split(";")[0] in ['application/json']:
            _json = classify_request
        elif content_type.split(";")[0] in ['application/octet-stream', 'application/pdf', 'application/vnd.openxmlformats-officedocument.presentationml.presentation', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'image/bmp', 'image/heif', 'image/jpeg', 'image/png', 'image/tiff', 'text/html']:
            _content = classify_request
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['application/octet-stream', 'application/pdf', 'application/vnd.openxmlformats-officedocument.presentationml.presentation', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'image/bmp', 'image/heif', 'image/jpeg', 'image/png', 'image/tiff', 'text/html', 'application/json']".format(content_type)
            )

        request = build_classify_document_request_initial(
            classifier_id=classifier_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            string_index_type=string_index_type,
            template_url=self._classify_document_initial.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['Operation-Location']=self._deserialize('str', response.headers.get('Operation-Location'))


        if cls:
            return cls(pipeline_response, None, response_headers)

    _classify_document_initial.metadata = {'url': "/documentClassifiers/{classifierId}:analyze"}  # type: ignore


    @distributed_trace
    def begin_classify_document(  # pylint: disable=inconsistent-return-statements
        self,
        classifier_id: str,
        string_index_type: Optional[Union[str, "_models.StringIndexType"]] = None,
        classify_request: Optional[Union[IO, str, _models.ClassifyDocumentRequest]] = None,
        *,
        content_type: Optional[Union[str, "_models.ContentType"]] = "application/json",
        **kwargs: Any
    ) -> LROPoller[None]:
        """Classify document.

        Classifies document with document classifier.

        :param classifier_id: Unique document classifier name.
        :type classifier_id: str
        :param string_index_type: Method used to compute string offset and length. Default value is
         None.
        :type string_index_type: str or
         ~azure.ai.formrecognizer.v2023_02_28_preview.models.StringIndexType
        :param classify_request: Classify request parameters. Default value is None.
        :type classify_request: IO or str or
         ~azure.ai.formrecognizer.v2023_02_28_preview.models.ClassifyDocumentRequest
        :keyword content_type: Media type of the body sent to the API. Known values are:
         "application/octet-stream", "application/pdf",
         "application/vnd.openxmlformats-officedocument.presentationml.presentation",
         "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
         "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "image/bmp",
         "image/heif", "image/jpeg", "image/png", "image/tiff", "text/html", and "application/json".
         Default value is "application/json".
        :paramtype content_type: str or ~azure.ai.formrecognizer.v2023_02_28_preview.models.ContentType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-02-28-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._classify_document_initial(  # type: ignore
                classifier_id=classifier_id,
                string_index_type=string_index_type,
                classify_request=classify_request,
                content_type=content_type,
                api_version=api_version,
                cls=lambda x,y,z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})


        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        if polling is True:
            polling_method = cast(PollingMethod, LROBasePolling(
                lro_delay,
                
                path_format_arguments=path_format_arguments,
                **kwargs
        ))  # type: PollingMethod
        elif polling is False: polling_method = cast(PollingMethod, NoPolling())
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_classify_document.metadata = {'url': "/documentClassifiers/{classifierId}:analyze"}  # type: ignore

    @distributed_trace
    def get_classify_result(
        self,
        classifier_id: str,
        result_id: str,
        **kwargs: Any
    ) -> _models.AnalyzeResultOperation:
        """Get document classifier result.

        Gets the result of document classifier.

        :param classifier_id: Unique document classifier name.
        :type classifier_id: str
        :param result_id: Analyze operation result ID.
        :type result_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AnalyzeResultOperation, or the result of cls(response)
        :rtype: ~azure.ai.formrecognizer.v2023_02_28_preview.models.AnalyzeResultOperation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2023-02-28-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.AnalyzeResultOperation]

        
        request = build_get_classify_result_request(
            classifier_id=classifier_id,
            result_id=result_id,
            api_version=api_version,
            template_url=self.get_classify_result.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('AnalyzeResultOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_classify_result.metadata = {'url': "/documentClassifiers/{classifierId}/analyzeResults/{resultId}"}  # type: ignore
