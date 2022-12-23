from dataclasses import dataclass, field
from typing import Optional
from .. import shared


@dataclass
class GetValidEmbedAccessTokensResponse:
    content_type: str = field()
    status_code: int = field()
    embed_tokens: Optional[list[shared.EmbedToken]] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    
