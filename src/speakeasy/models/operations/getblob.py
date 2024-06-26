"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import error as errors_error
from typing import Optional


@dataclasses.dataclass
class GetBlobRequest:
    digest: str = dataclasses.field(metadata={'path_param': { 'field_name': 'digest', 'style': 'simple', 'explode': False }})
    namespace_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'namespace_name', 'style': 'simple', 'explode': False }})
    organization_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'organization_slug', 'style': 'simple', 'explode': False }})
    workspace_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_slug', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetBlobResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    blob: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""OK"""
    error: Optional[errors_error.Error] = dataclasses.field(default=None)
    r"""Default error response"""
    

