"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from speakeasy_client_sdk_python.types import BaseModel
from typing import Dict, List, TypedDict


class SuggestedOperationIDsTypedDict(TypedDict):
    operation_ids: Dict[str, List[str]]
    

class SuggestedOperationIDs(BaseModel):
    operation_ids: Dict[str, List[str]]
    