"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from speakeasy_client_sdk_python.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class LicenseTypedDict(TypedDict):
    identifier: NotRequired[str]
    

class License(BaseModel):
    identifier: Optional[str] = None
    

class OASInfoTypedDict(TypedDict):
    description: str
    license: LicenseTypedDict
    summary: str
    title: str
    version: str
    

class OASInfo(BaseModel):
    description: str
    license: License
    summary: str
    title: str
    version: str
    