"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from speakeasy_client_sdk_python.models.shared import (
    workspaceinviteresponse as shared_workspaceinviteresponse,
)
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, PathParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GrantUserAccessToWorkspaceGlobalsTypedDict(TypedDict):
    workspace_id: NotRequired[str]


class GrantUserAccessToWorkspaceGlobals(BaseModel):
    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None


class GrantUserAccessToWorkspaceRequestTypedDict(TypedDict):
    email: str
    r"""Email of the user to grant access to."""
    workspace_id: NotRequired[str]
    r"""Unique identifier of the workspace."""


class GrantUserAccessToWorkspaceRequest(BaseModel):
    email: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Email of the user to grant access to."""

    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None
    r"""Unique identifier of the workspace."""


class GrantUserAccessToWorkspaceResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    workspace_invite_response: NotRequired[
        shared_workspaceinviteresponse.WorkspaceInviteResponseTypedDict
    ]
    r"""Success"""


class GrantUserAccessToWorkspaceResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    workspace_invite_response: Optional[
        shared_workspaceinviteresponse.WorkspaceInviteResponse
    ] = None
    r"""Success"""
