import dataclasses
from ..shared import api as shared_api
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class GetAllAPIVersionsPathParams:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetAllAPIVersionsOp:
    and_: bool = dataclasses.field(metadata={'query_param': { 'field_name': 'and' }})
    

@dataclasses.dataclass
class GetAllAPIVersionsQueryParams:
    metadata: Optional[dict[str, list[str]]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    op: Optional[GetAllAPIVersionsOp] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'op', 'style': 'deepObject', 'explode': True }})
    

@dataclasses.dataclass
class GetAllAPIVersionsRequest:
    path_params: GetAllAPIVersionsPathParams = dataclasses.field()
    query_params: GetAllAPIVersionsQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetAllAPIVersionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    apis: Optional[list[shared_api.API]] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    