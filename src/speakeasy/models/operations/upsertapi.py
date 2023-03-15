from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import api as shared_api
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class UpsertAPIRequest:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    api_input: shared_api.APIInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpsertAPIResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    api: Optional[shared_api.API] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    