from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class GetValidEmbedAccessTokensResponse:content_type: str = field(default=None)
    embed_tokens: Optional[list[shared.EmbedToken]] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    status_code: int = field(default=None)
    
