from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class EmbedAccessTokenResponse:
    r"""EmbedAccessTokenResponse
    An EmbedAccessTokenResponse contains a token that can be used to embed a Speakeasy dashboard.
    """
    
    access_token: str = field(metadata={'dataclasses_json': { 'field_name': 'access_token' }})
    
