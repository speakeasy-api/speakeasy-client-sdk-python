from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import api as shared_api
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class GetAllAPIVersionsOp:
    r"""GetAllAPIVersionsOp
    Configuration for filter operations
    """
    
    and_: bool = dataclasses.field(metadata={'query_param': { 'field_name': 'and' }})
    

@dataclasses.dataclass
class GetAllAPIVersionsRequest:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    metadata: Optional[dict[str, list[str]]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'metadata', 'style': 'deepObject', 'explode': True }})
    op: Optional[GetAllAPIVersionsOp] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'op', 'style': 'deepObject', 'explode': True }})
    

@dataclasses.dataclass
class GetAllAPIVersionsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    apis: Optional[list[shared_api.API]] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    