"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
import pydantic
from speakeasy_client_sdk_python.models.shared import (
    accessdetails as shared_accessdetails,
)
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, QueryParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetWorkspaceAccessRequestTypedDict(TypedDict):
    gen_lock_id: NotRequired[str]
    r"""Unique identifier of the generation target."""
    target_type: NotRequired[str]
    r"""The type of the generated target."""
    passive: NotRequired[bool]
    r"""Skip side-effects like incrementing metrics."""


class GetWorkspaceAccessRequest(BaseModel):
    gen_lock_id: Annotated[
        Optional[str],
        pydantic.Field(alias="genLockId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Unique identifier of the generation target."""

    target_type: Annotated[
        Optional[str],
        pydantic.Field(alias="targetType"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The type of the generated target."""

    passive: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Skip side-effects like incrementing metrics."""


class GetWorkspaceAccessResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    access_details: NotRequired[shared_accessdetails.AccessDetailsTypedDict]
    r"""OK"""


class GetWorkspaceAccessResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    access_details: Optional[shared_accessdetails.AccessDetails] = None
    r"""OK"""
