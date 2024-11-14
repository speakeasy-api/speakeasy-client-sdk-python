"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from speakeasy_client_sdk_python.models.shared import (
    clievent as shared_clievent,
    interactiontype as shared_interactiontype,
)
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
)
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SearchWorkspaceEventsGlobalsTypedDict(TypedDict):
    workspace_id: NotRequired[str]


class SearchWorkspaceEventsGlobals(BaseModel):
    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None


class SearchWorkspaceEventsRequestTypedDict(TypedDict):
    workspace_id: NotRequired[str]
    r"""Unique identifier of the workspace."""
    source_revision_digest: NotRequired[str]
    r"""Unique identifier of the source revision digest."""
    lint_report_digest: NotRequired[str]
    r"""Unique identifier of the lint report digest."""
    openapi_diff_report_digest: NotRequired[str]
    r"""Unique identifier of the openapi diff report digest."""
    interaction_type: NotRequired[shared_interactiontype.InteractionType]
    r"""Specified interaction type for events."""
    generate_gen_lock_id: NotRequired[str]
    r"""A specific gen lock ID for the events."""
    execution_id: NotRequired[str]
    r"""Shared execution ID for cli events across a single action."""


class SearchWorkspaceEventsRequest(BaseModel):
    workspace_id: Annotated[
        Optional[str],
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ] = None
    r"""Unique identifier of the workspace."""

    source_revision_digest: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Unique identifier of the source revision digest."""

    lint_report_digest: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Unique identifier of the lint report digest."""

    openapi_diff_report_digest: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Unique identifier of the openapi diff report digest."""

    interaction_type: Annotated[
        Optional[shared_interactiontype.InteractionType],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Specified interaction type for events."""

    generate_gen_lock_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A specific gen lock ID for the events."""

    execution_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Shared execution ID for cli events across a single action."""


class SearchWorkspaceEventsResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    cli_event_batch: NotRequired[List[shared_clievent.CliEventTypedDict]]
    r"""Success"""


class SearchWorkspaceEventsResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    cli_event_batch: Optional[List[shared_clievent.CliEvent]] = None
    r"""Success"""
