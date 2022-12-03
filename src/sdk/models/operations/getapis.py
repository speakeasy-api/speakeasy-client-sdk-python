from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared
from sdk.models import shared


@dataclass
class GetApisOp:
    and_: bool = field(metadata={'query_param': { 'field_name': 'and' }})
    

@dataclass
class GetApisQueryParams:
    metadata: Optional[dict[str, list[str]]] = field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    op: Optional[GetApisOp] = field(default=None, metadata={'query_param': { 'field_name': 'op', 'style': 'deepObject', 'explode': True }})
    

@dataclass
class GetApisRequest:
    query_params: GetApisQueryParams = field()
    

@dataclass
class GetApisResponse:
    content_type: str = field()
    status_code: int = field()
    apis: Optional[list[shared.API]] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    
