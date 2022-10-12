from dataclasses import dataclass, field
from typing import List,Optional
from sdk.models import shared


@dataclass
class GetAllAPIVersionsPathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetAllAPIVersionsOp:
    and_: bool = field(default=None, metadata={'query_param': { 'field_name': 'and' }})
    

@dataclass
class GetAllAPIVersionsQueryParams:
    metadata: Optional[dict[str, List[str]]] = field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    op: Optional[GetAllAPIVersionsOp] = field(default=None, metadata={'query_param': { 'field_name': 'op', 'style': 'deepObject', 'explode': True }})
    

@dataclass
class GetAllAPIVersionsRequest:
    path_params: GetAllAPIVersionsPathParams = field(default=None)
    query_params: GetAllAPIVersionsQueryParams = field(default=None)
    

@dataclass
class GetAllAPIVersionsResponse:
    apis: Optional[List[shared.API]] = field(default=None)
    content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    status_code: int = field(default=None)
    
