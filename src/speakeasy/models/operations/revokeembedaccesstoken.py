from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class RevokeEmbedAccessTokenRequest:
    token_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'tokenID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RevokeEmbedAccessTokenResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    