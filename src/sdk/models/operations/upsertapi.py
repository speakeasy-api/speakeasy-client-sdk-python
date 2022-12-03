from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared
from sdk.models import shared


@dataclass
class UpsertAPIPathParams:
    api_id: str = field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    

@dataclass
class UpsertAPIRequest:
    path_params: UpsertAPIPathParams = field()
    request: shared.APIInput = field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class UpsertAPIResponse:
    content_type: str = field()
    status_code: int = field()
    api: Optional[shared.API] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    
