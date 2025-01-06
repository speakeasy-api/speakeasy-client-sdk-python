"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from speakeasy_client_sdk_python.models.shared import clievent as shared_clievent
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    RequestMetadata,
)
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PostWorkspaceEventsGlobalsTypedDict(TypedDict):
    workspace_id: NotRequired[str]


class PostWorkspaceEventsGlobals(BaseModel):
    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None


class PostWorkspaceEventsRequestTypedDict(TypedDict):
    request_body: List[shared_clievent.CliEventTypedDict]
    workspace_id: NotRequired[str]
    r"""Unique identifier of the workspace."""


class PostWorkspaceEventsRequest(BaseModel):
    request_body: Annotated[
        List[shared_clievent.CliEvent],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None
    r"""Unique identifier of the workspace."""


class PostWorkspaceEventsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class PostWorkspaceEventsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
