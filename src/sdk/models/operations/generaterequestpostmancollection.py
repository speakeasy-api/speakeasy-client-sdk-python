import dataclasses
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class GenerateRequestPostmanCollectionPathParams:
    request_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'requestID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GenerateRequestPostmanCollectionRequest:
    path_params: GenerateRequestPostmanCollectionPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GenerateRequestPostmanCollectionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    postman_collection: Optional[bytes] = dataclasses.field(default=None)
    