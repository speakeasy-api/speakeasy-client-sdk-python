from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class RevokeEmbedAccessTokenPathParams:
    token_id: str = field(default=None, metadata={'path_param': { 'field_name': 'tokenID', 'style': 'simple', 'explode': False }})
    

@dataclass
class RevokeEmbedAccessTokenRequest:
    path_params: RevokeEmbedAccessTokenPathParams = field(default=None)
    

@dataclass
class RevokeEmbedAccessTokenResponse:
    content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    status_code: int = field(default=None)
    
