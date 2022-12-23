from dataclasses import dataclass, field
from typing import Optional
from .. import shared


@dataclass
class RevokeEmbedAccessTokenPathParams:
    token_id: str = field(metadata={'path_param': { 'field_name': 'tokenID', 'style': 'simple', 'explode': False }})
    

@dataclass
class RevokeEmbedAccessTokenRequest:
    path_params: RevokeEmbedAccessTokenPathParams = field()
    

@dataclass
class RevokeEmbedAccessTokenResponse:
    content_type: str = field()
    status_code: int = field()
    error: Optional[shared.Error] = field(default=None)
    
