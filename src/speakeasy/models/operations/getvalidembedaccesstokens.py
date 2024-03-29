"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.errors import error as errors_error
from ...models.shared import embedtoken as shared_embedtoken
from typing import List, Optional


@dataclasses.dataclass
class GetValidEmbedAccessTokensResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    embed_tokens: Optional[List[shared_embedtoken.EmbedToken]] = dataclasses.field(default=None)
    r"""OK"""
    error: Optional[errors_error.Error] = dataclasses.field(default=None)
    r"""Default error response"""
    

