"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from speakeasy_client_sdk_python.models.shared import (
    workspacesettings as shared_workspacesettings,
)
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    RequestMetadata,
)
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateWorkspaceSettingsGlobalsTypedDict(TypedDict):
    workspace_id: NotRequired[str]


class UpdateWorkspaceSettingsGlobals(BaseModel):
    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None


class UpdateWorkspaceSettingsRequestTypedDict(TypedDict):
    workspace_settings: shared_workspacesettings.WorkspaceSettingsTypedDict
    r"""The workspace settings to update."""
    workspace_id: NotRequired[str]
    r"""Unique identifier of the workspace."""


class UpdateWorkspaceSettingsRequest(BaseModel):
    workspace_settings: Annotated[
        shared_workspacesettings.WorkspaceSettings,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""The workspace settings to update."""

    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None
    r"""Unique identifier of the workspace."""


class UpdateWorkspaceSettingsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class UpdateWorkspaceSettingsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
