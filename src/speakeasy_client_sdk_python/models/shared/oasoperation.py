"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from speakeasy_client_sdk_python.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class OASOperationTypedDict(TypedDict):
    description: str
    method: str
    operation_id: str
    path: str
    tags: List[str]
    group_override: NotRequired[str]
    method_name_override: NotRequired[str]


class OASOperation(BaseModel):
    description: str

    method: str

    operation_id: str

    path: str

    tags: List[str]

    group_override: Optional[str] = None

    method_name_override: Optional[str] = None
