"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .diagnostic import Diagnostic, DiagnosticTypedDict
from enum import Enum
from speakeasy_client_sdk_python.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class SuggestionType(str, Enum):
    METHOD_NAMES = "method-names"
    DIAGNOSTICS_ONLY = "diagnostics-only"


class SuggestOptsOldTypedDict(TypedDict):
    suggestion_type: SuggestionType
    diagnostics: NotRequired[List[DiagnosticTypedDict]]


class SuggestOptsOld(BaseModel):
    suggestion_type: SuggestionType

    diagnostics: Optional[List[Diagnostic]] = None
