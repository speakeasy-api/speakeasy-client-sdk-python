"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import error as shared_error
from ...models.shared import generateopenapispecdiff as shared_generateopenapispecdiff
from typing import Optional


@dataclasses.dataclass
class GenerateOpenAPISpecRequest:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    r"""The ID of the Api to generate an OpenAPI specification for."""
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    r"""The version ID of the Api to generate an OpenAPI specification for."""
    



@dataclasses.dataclass
class GenerateOpenAPISpecResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""Default error response"""
    generate_open_api_spec_diff: Optional[shared_generateopenapispecdiff.GenerateOpenAPISpecDiff] = dataclasses.field(default=None)
    r"""OK"""
    

