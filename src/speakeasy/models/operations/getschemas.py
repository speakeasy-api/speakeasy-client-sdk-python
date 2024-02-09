"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import error as errors_error
from ...models.shared import schema as shared_schema
from typing import List, Optional


@dataclasses.dataclass
class GetSchemasRequest:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    r"""The ID of the Api to retrieve schemas for."""
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    r"""The version ID of the Api to delete metadata for."""
    



@dataclasses.dataclass
class GetSchemasResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    error: Optional[errors_error.Error] = dataclasses.field(default=None)
    r"""Default error response"""
    classes: Optional[List[shared_schema.Schema]] = dataclasses.field(default=None)
    r"""OK"""
    

