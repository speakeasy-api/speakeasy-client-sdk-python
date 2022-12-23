from dataclasses import dataclass, field
from typing import Optional
from .. import shared


@dataclass
class QueryEventLogQueryParams:
    filters: Optional[shared.Filters] = field(default=None, metadata={'query_param': { 'field_name': 'filters', 'serialization': 'json' }})
    

@dataclass
class QueryEventLogRequest:
    query_params: QueryEventLogQueryParams = field()
    

@dataclass
class QueryEventLogResponse:
    content_type: str = field()
    status_code: int = field()
    bounded_requests: Optional[list[shared.BoundedRequest]] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    
