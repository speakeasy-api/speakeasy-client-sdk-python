"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import error as errors_error
from ...models.shared import unboundedrequest as shared_unboundedrequest
from typing import Optional


@dataclasses.dataclass
class GetRequestFromEventLogRequest:
    request_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'requestID', 'style': 'simple', 'explode': False }})
    r"""The ID of the request to retrieve."""
    



@dataclasses.dataclass
class GetRequestFromEventLogResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    error: Optional[errors_error.Error] = dataclasses.field(default=None)
    r"""Default error response"""
    unbounded_request: Optional[shared_unboundedrequest.UnboundedRequest] = dataclasses.field(default=None)
    r"""OK"""
    

