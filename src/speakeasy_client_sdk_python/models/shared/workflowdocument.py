"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from speakeasy_client_sdk_python.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AuthTypedDict(TypedDict):
    header: str
    secret: str


class Auth(BaseModel):
    header: str

    secret: str


class WorkflowDocumentTypedDict(TypedDict):
    r"""A document referenced by a workflow"""

    location: str
    auth: NotRequired[AuthTypedDict]


class WorkflowDocument(BaseModel):
    r"""A document referenced by a workflow"""

    location: str

    auth: Optional[Auth] = None
