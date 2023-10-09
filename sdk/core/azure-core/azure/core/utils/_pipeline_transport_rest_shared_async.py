# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import asyncio
from typing import TYPE_CHECKING, List, Generic, TypeVar, Type, Optional, AsyncIterator, Iterator
from ..pipeline import PipelineContext, PipelineRequest, PipelineResponse
from ..pipeline._tools_async import await_result as _await_result

if TYPE_CHECKING:
    from ..pipeline.policies import SansIOHTTPPolicy


HttpResponseType = TypeVar("HttpResponseType")


class _PartGenerator(AsyncIterator[HttpResponseType], Generic[HttpResponseType]):
    """Until parts is a real async iterator, wrap the sync call.

    :param response: The response to parse
    :type response: ~azure.core.pipeline.transport.AsyncHttpResponse
    :param default_http_response_type: The default HTTP response type to use
    :type default_http_response_type: any
    """

    def __init__(self, response, default_http_response_type: Type[HttpResponseType]) -> None:
        self._response = response
        self._parts: Optional[Iterator[HttpResponseType]] = None
        self._default_http_response_type = default_http_response_type

    async def _parse_response(self) -> Iterator[HttpResponseType]:
        responses = self._response._get_raw_parts(  # pylint: disable=protected-access
            http_response_type=self._default_http_response_type
        )
        if self._response.request.multipart_mixed_info:
            policies: List["SansIOHTTPPolicy"] = self._response.request.multipart_mixed_info[1]

            async def parse_responses(response):
                http_request = response.request
                context = PipelineContext(None)
                pipeline_request = PipelineRequest(http_request, context)
                pipeline_response = PipelineResponse(http_request, response, context=context)

                for policy in policies:
                    await _await_result(policy.on_response, pipeline_request, pipeline_response)

            # Not happy to make this code asyncio specific, but that's multipart only for now
            # If we need trio and multipart, let's reinvesitgate that later
            await asyncio.gather(*[parse_responses(res) for res in responses])

        return responses

    async def __anext__(self) -> HttpResponseType:
        if not self._parts:
            self._parts = iter(await self._parse_response())

        try:
            return next(self._parts)
        except StopIteration:
            raise StopAsyncIteration()  # pylint: disable=raise-missing-from
