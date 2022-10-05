from dataclasses import dataclass, field
from typing import List,Optional
from sdk.models import shared


@dataclass
class GetValidEmbedAccessTokensResponses:
    embed_tokens: Optional[List[shared.EmbedToken]] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    

@dataclass
class GetValidEmbedAccessTokensResponse:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetValidEmbedAccessTokensResponses]] = field(default=None)
    status_code: int = field(default=None)
    
