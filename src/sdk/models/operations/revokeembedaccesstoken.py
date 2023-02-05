import dataclasses
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class RevokeEmbedAccessTokenPathParams:
    token_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'tokenID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RevokeEmbedAccessTokenRequest:
    path_params: RevokeEmbedAccessTokenPathParams = dataclasses.field()
    

@dataclasses.dataclass
class RevokeEmbedAccessTokenResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    