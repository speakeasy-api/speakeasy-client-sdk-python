"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiendpoint as shared_apiendpoint
from ..shared import error as shared_error
from typing import Optional



@dataclasses.dataclass
class FindAPIEndpointRequest:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    r"""The ID of the Api the ApiEndpoint belongs to."""
    display_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'displayName', 'style': 'simple', 'explode': False }})
    r"""The displayName of the ApiEndpoint to find (set by operationId from OpenAPI schema)."""
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    r"""The version ID of the Api the ApiEndpoint belongs to."""
    




@dataclasses.dataclass
class FindAPIEndpointResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_endpoint: Optional[shared_apiendpoint.APIEndpoint] = dataclasses.field(default=None)
    r"""OK"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""Default error response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

