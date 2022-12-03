from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared
from sdk.models import shared


@dataclass
class GenerateRequestPostmanCollectionPathParams:
    request_id: str = field(metadata={'path_param': { 'field_name': 'requestID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GenerateRequestPostmanCollectionRequest:
    path_params: GenerateRequestPostmanCollectionPathParams = field()
    

@dataclass
class GenerateRequestPostmanCollectionResponse:
    content_type: str = field()
    status_code: int = field()
    error: Optional[shared.Error] = field(default=None)
    postman_collection: Optional[bytes] = field(default=None)
    
