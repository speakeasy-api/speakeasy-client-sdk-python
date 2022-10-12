from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class GeneratePostmanCollectionPathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GeneratePostmanCollectionRequest:
    path_params: GeneratePostmanCollectionPathParams = field(default=None)
    

@dataclass
class GeneratePostmanCollectionResponse:
    content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    postman_collection: Optional[bytes] = field(default=None)
    status_code: int = field(default=None)
    
