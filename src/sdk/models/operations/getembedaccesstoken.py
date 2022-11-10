from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class GetEmbedAccessTokenQueryParams:
    description: Optional[str] = field(default=None, metadata={'query_param': { 'field_name': 'description', 'style': 'form', 'explode': True }})
    duration: Optional[int] = field(default=None, metadata={'query_param': { 'field_name': 'duration', 'style': 'form', 'explode': True }})
    filters: Optional[shared.Filters] = field(default=None, metadata={'query_param': { 'field_name': 'filters', 'serialization': 'json' }})
    

@dataclass
class GetEmbedAccessTokenRequest:
    query_params: GetEmbedAccessTokenQueryParams = field()
    

@dataclass
class GetEmbedAccessTokenResponse:
    content_type: str = field()
    status_code: int = field()
    embed_access_token_response: Optional[shared.EmbedAccessTokenResponse] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    
