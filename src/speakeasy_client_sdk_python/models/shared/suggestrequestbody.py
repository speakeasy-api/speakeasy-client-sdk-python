"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .diagnostic import Diagnostic, DiagnosticTypedDict
from .oassummary import OASSummary, OASSummaryTypedDict
from enum import Enum
from speakeasy_client_sdk_python.types import BaseModel
from typing import List, TypedDict


class SuggestRequestBodySuggestionType(str, Enum):
    METHOD_NAMES = "method-names"
    DIAGNOSTICS_ONLY = "diagnostics-only"


class SuggestRequestBodyTypedDict(TypedDict):
    diagnostics: List[DiagnosticTypedDict]
    oas_summary: OASSummaryTypedDict
    suggestion_type: SuggestRequestBodySuggestionType


class SuggestRequestBody(BaseModel):
    diagnostics: List[Diagnostic]

    oas_summary: OASSummary

    suggestion_type: SuggestRequestBodySuggestionType
