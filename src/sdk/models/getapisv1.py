from dataclasses import dataclass, field
from typing import List,Optional
from .api import API
from .error import Error

@dataclass
class GetApisV1Op:
    and_: bool = field(default=None, metadata={'query_param': { 'field_name': 'and' }})
    

@dataclass
class GetApisV1QueryParams:
    metadata: Optional[dict[str, List[str]]] = field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    op: Optional[GetApisV1Op] = field(default=None, metadata={'query_param': { 'field_name': 'op', 'style': 'deepObject', 'explode': True }})
    

@dataclass
class GetApisV1Request:
    query_params: GetApisV1QueryParams = field(default=None)
    

@dataclass
class GetApisV1Responses:
    api: Optional[List[API]] = field(default=None)
    error: Optional[Error] = field(default=None)
    raw_response: bytes = field(default=None)
    

@dataclass
class GetApisV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetApisV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
