from dataclasses import dataclass, field
from typing import List,Optional
from sdk.models import shared


@dataclass
class GetAllAPIVersionsV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetAllAPIVersionsV1Op:
    and_: bool = field(default=None, metadata={'query_param': { 'field_name': 'and' }})
    

@dataclass
class GetAllAPIVersionsV1QueryParams:
    metadata: Optional[dict[str, List[str]]] = field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    op: Optional[GetAllAPIVersionsV1Op] = field(default=None, metadata={'query_param': { 'field_name': 'op', 'style': 'deepObject', 'explode': True }})
    

@dataclass
class GetAllAPIVersionsV1Request:
    path_params: GetAllAPIVersionsV1PathParams = field(default=None)
    query_params: GetAllAPIVersionsV1QueryParams = field(default=None)
    

@dataclass
class GetAllAPIVersionsV1Responses:
    api: Optional[List[shared.API]] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    raw_response: bytes = field(default=None)
    

@dataclass
class GetAllAPIVersionsV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetAllAPIVersionsV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
