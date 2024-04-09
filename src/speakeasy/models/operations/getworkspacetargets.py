"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import targetsdk as shared_targetsdk
from datetime import datetime
from typing import List, Optional


@dataclasses.dataclass
class GetWorkspaceTargetsGlobals:
    workspace_id: Optional[str] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'workspaceID', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetWorkspaceTargetsRequest:
    after_last_event_created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'after_last_event_created_at', 'style': 'form', 'explode': True }})
    r"""Filter to only return targets with events created after this timestamp"""
    workspace_id: Optional[str] = dataclasses.field(default=None, metadata={'path_param': { 'field_name': 'workspaceID', 'style': 'simple', 'explode': False }})
    r"""Unique identifier of the workspace."""
    



@dataclasses.dataclass
class GetWorkspaceTargetsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    target_sdk_list: Optional[List[shared_targetsdk.TargetSDK]] = dataclasses.field(default=None)
    r"""Success"""
    

