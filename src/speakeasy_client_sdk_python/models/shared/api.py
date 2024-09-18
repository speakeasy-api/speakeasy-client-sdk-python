"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from speakeasy_client_sdk_python.types import BaseModel
from typing import Dict, List, Optional, TypedDict
from typing_extensions import NotRequired


class APITypedDict(TypedDict):
    r"""An Api is representation of a API (a collection of API Endpoints) within the Speakeasy Platform."""

    api_id: str
    r"""The ID of this Api. This is a human-readable name (subject to change)."""
    created_at: datetime
    r"""Creation timestamp."""
    description: str
    r"""A detailed description of the Api."""
    updated_at: datetime
    r"""Last update timestamp."""
    version_id: str
    r"""The version ID of this Api. This is semantic version identifier."""
    workspace_id: str
    r"""The workspace ID this Api belongs to."""
    matched: NotRequired[bool]
    r"""Determines if all the endpoints within the Api are found in the OpenAPI spec associated with the Api."""
    meta_data: NotRequired[Dict[str, List[str]]]
    r"""A set of values associated with a meta_data key. This field is only set on get requests."""


class API(BaseModel):
    r"""An Api is representation of a API (a collection of API Endpoints) within the Speakeasy Platform."""

    api_id: str
    r"""The ID of this Api. This is a human-readable name (subject to change)."""

    created_at: datetime
    r"""Creation timestamp."""

    description: str
    r"""A detailed description of the Api."""

    updated_at: datetime
    r"""Last update timestamp."""

    version_id: str
    r"""The version ID of this Api. This is semantic version identifier."""

    workspace_id: str
    r"""The workspace ID this Api belongs to."""

    matched: Optional[bool] = None
    r"""Determines if all the endpoints within the Api are found in the OpenAPI spec associated with the Api."""

    meta_data: Optional[Dict[str, List[str]]] = None
    r"""A set of values associated with a meta_data key. This field is only set on get requests."""
