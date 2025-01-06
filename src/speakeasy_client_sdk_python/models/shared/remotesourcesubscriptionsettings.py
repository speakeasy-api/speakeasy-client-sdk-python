"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from speakeasy_client_sdk_python.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class RemoteSourceSubscriptionSettingsTypedDict(TypedDict):
    base_spec_namespaces: List[str]
    output_namespace: str
    overlay_namespaces: List[str]
    ignored_namespaces: NotRequired[List[str]]


class RemoteSourceSubscriptionSettings(BaseModel):
    base_spec_namespaces: List[str]

    output_namespace: str

    overlay_namespaces: List[str]

    ignored_namespaces: Optional[List[str]] = None
