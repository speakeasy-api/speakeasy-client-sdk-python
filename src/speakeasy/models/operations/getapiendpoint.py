"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import apiendpoint as shared_apiendpoint
from ...models.shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class GetAPIEndpointRequest:
    api_endpoint_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiEndpointID', 'style': 'simple', 'explode': False }})
    r"""The ID of the ApiEndpoint to retrieve."""
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    r"""The ID of the Api the ApiEndpoint belongs to."""
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    r"""The version ID of the Api the ApiEndpoint belongs to."""
    



@dataclasses.dataclass
class GetAPIEndpointResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_endpoint: Optional[shared_apiendpoint.APIEndpoint] = dataclasses.field(default=None)
    r"""OK"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""Default error response"""
    

