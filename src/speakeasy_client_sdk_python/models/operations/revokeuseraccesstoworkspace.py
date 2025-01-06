"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
import pydantic
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, PathParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RevokeUserAccessToWorkspaceGlobalsTypedDict(TypedDict):
    workspace_id: NotRequired[str]


class RevokeUserAccessToWorkspaceGlobals(BaseModel):
    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None


class RevokeUserAccessToWorkspaceRequestTypedDict(TypedDict):
    user_id: str
    r"""Unique identifier of the user."""
    workspace_id: NotRequired[str]
    r"""Unique identifier of the workspace."""


class RevokeUserAccessToWorkspaceRequest(BaseModel):
    user_id: Annotated[
        str,
        pydantic.Field(alias="userId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""Unique identifier of the user."""

    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None
    r"""Unique identifier of the workspace."""


class RevokeUserAccessToWorkspaceResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class RevokeUserAccessToWorkspaceResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
