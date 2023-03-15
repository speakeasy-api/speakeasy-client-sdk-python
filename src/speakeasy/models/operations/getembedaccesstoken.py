from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import embedaccesstokenresponse as shared_embedaccesstokenresponse
from ..shared import error as shared_error
from ..shared import filters as shared_filters
from typing import Optional


@dataclasses.dataclass
class GetEmbedAccessTokenRequest:
    description: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'description', 'style': 'form', 'explode': True }})
    duration: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'duration', 'style': 'form', 'explode': True }})
    filters: Optional[shared_filters.Filters] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filters', 'serialization': 'json' }})
    

@dataclasses.dataclass
class GetEmbedAccessTokenResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    embed_access_token_response: Optional[shared_embedaccesstokenresponse.EmbedAccessTokenResponse] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    