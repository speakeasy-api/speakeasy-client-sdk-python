"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import clievent as shared_clievent
from datetime import datetime
from typing import List, Optional


@dataclasses.dataclass
class GetWorkspaceEventsByTargetGlobals:
    workspace_id: Optional[str] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'workspaceID', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetWorkspaceEventsByTargetRequest:
    target_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'targetID', 'style': 'simple', 'explode': False }})
    r"""Filter to only return events corresponding to a particular gen_lock_id (gen_lock_id uniquely identifies a target)"""
    after_created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'after_created_at', 'style': 'form', 'explode': True }})
    r"""Filter to only return events created after this timestamp"""
    workspace_id: Optional[str] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'workspaceID', 'style': 'simple', 'explode': False }})
    r"""Unique identifier of the workspace."""
    



@dataclasses.dataclass
class GetWorkspaceEventsByTargetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    cli_event_batch: Optional[List[shared_clievent.CliEvent]] = dataclasses.field(default=None)
    r"""Success"""
    

