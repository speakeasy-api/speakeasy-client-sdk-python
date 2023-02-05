import dataclasses
from ..shared import api as shared_api
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class GetApisOp:
    and_: bool = dataclasses.field(metadata={'query_param': { 'field_name': 'and' }})
    

@dataclasses.dataclass
class GetApisQueryParams:
    metadata: Optional[dict[str, list[str]]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    op: Optional[GetApisOp] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'op', 'style': 'deepObject', 'explode': True }})
    

@dataclasses.dataclass
class GetApisRequest:
    query_params: GetApisQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GetApisResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    apis: Optional[list[shared_api.API]] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    