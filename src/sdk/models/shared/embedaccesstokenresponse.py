from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from sdk import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EmbedAccessTokenResponse:
    r"""EmbedAccessTokenResponse
    An EmbedAccessTokenResponse contains a token that can be used to embed a Speakeasy dashboard.
    """
    
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('access_token') }})
    