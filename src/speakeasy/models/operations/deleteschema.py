"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error as shared_error
from typing import Optional



@dataclasses.dataclass
class DeleteSchemaRequest:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    r"""The ID of the Api to delete schemas for."""
    revision_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'revisionID', 'style': 'simple', 'explode': False }})
    r"""The revision ID of the schema to delete."""
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    r"""The version ID of the Api to delete metadata for."""
    




@dataclasses.dataclass
class DeleteSchemaResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""Default error response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

