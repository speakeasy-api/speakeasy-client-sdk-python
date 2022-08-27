from dataclasses import dataclass, field
from typing import Optional
from .api import API
from .api import API
from .error import Error

@dataclass
class UpsertAPIV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    

@dataclass
class UpsertAPIV1Request:
    path_params: UpsertAPIV1PathParams = field(default=None)
    request: API = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class UpsertAPIV1Responses:
    api: Optional[API] = field(default=None)
    error: Optional[Error] = field(default=None)
    raw_response: bytes = field(default=None)
    

@dataclass
class UpsertAPIV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, UpsertAPIV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
