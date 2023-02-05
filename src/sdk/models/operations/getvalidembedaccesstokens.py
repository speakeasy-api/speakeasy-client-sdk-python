import dataclasses
from ..shared import embedtoken as shared_embedtoken
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class GetValidEmbedAccessTokensResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    embed_tokens: Optional[list[shared_embedtoken.EmbedToken]] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    