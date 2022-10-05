from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class UpsertAPIPathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    

@dataclass
class UpsertAPIRequest:
    path_params: UpsertAPIPathParams = field(default=None)
    request: shared.API = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class UpsertAPIResponses:
    api: Optional[shared.API] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    

@dataclass
class UpsertAPIResponse:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, UpsertAPIResponses]] = field(default=None)
    status_code: int = field(default=None)
    
