from dataclasses import dataclass, field
from typing import Optional
from .. import shared


@dataclass
class GetAllAPIVersionsPathParams:
    api_id: str = field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetAllAPIVersionsOp:
    and_: bool = field(metadata={'query_param': { 'field_name': 'and' }})
    

@dataclass
class GetAllAPIVersionsQueryParams:
    metadata: Optional[dict[str, list[str]]] = field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    op: Optional[GetAllAPIVersionsOp] = field(default=None, metadata={'query_param': { 'field_name': 'op', 'style': 'deepObject', 'explode': True }})
    

@dataclass
class GetAllAPIVersionsRequest:
    path_params: GetAllAPIVersionsPathParams = field()
    query_params: GetAllAPIVersionsQueryParams = field()
    

@dataclass
class GetAllAPIVersionsResponse:
    content_type: str = field()
    status_code: int = field()
    apis: Optional[list[shared.API]] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    
