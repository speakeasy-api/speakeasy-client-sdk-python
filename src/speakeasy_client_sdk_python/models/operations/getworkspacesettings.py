"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from speakeasy_client_sdk_python.models.shared import (
    workspacesettings as shared_workspacesettings,
)
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, PathParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetWorkspaceSettingsGlobalsTypedDict(TypedDict):
    workspace_id: NotRequired[str]


class GetWorkspaceSettingsGlobals(BaseModel):
    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None


class GetWorkspaceSettingsRequestTypedDict(TypedDict):
    workspace_id: NotRequired[str]
    r"""Unique identifier of the workspace."""


class GetWorkspaceSettingsRequest(BaseModel):
    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None
    r"""Unique identifier of the workspace."""


class GetWorkspaceSettingsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    workspace_settings: NotRequired[shared_workspacesettings.WorkspaceSettingsTypedDict]
    r"""OK"""


class GetWorkspaceSettingsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    workspace_settings: Optional[shared_workspacesettings.WorkspaceSettings] = None
    r"""OK"""
