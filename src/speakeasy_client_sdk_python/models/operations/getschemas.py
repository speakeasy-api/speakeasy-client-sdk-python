"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
import pydantic
from speakeasy_client_sdk_python.models.shared import schema as shared_schema
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, PathParamMetadata
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetSchemasRequestTypedDict(TypedDict):
    api_id: str
    r"""The ID of the Api to retrieve schemas for."""
    version_id: str
    r"""The version ID of the Api to delete metadata for."""


class GetSchemasRequest(BaseModel):
    api_id: Annotated[
        str,
        pydantic.Field(alias="apiID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The ID of the Api to retrieve schemas for."""

    version_id: Annotated[
        str,
        pydantic.Field(alias="versionID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The version ID of the Api to delete metadata for."""


class GetSchemasResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    classes: NotRequired[List[shared_schema.SchemaTypedDict]]
    r"""OK"""


class GetSchemasResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    classes: Optional[List[shared_schema.Schema]] = None
    r"""OK"""
