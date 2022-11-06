from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class QueryEventLogQueryParams:filters: Optional[shared.Filters] = field(default=None, metadata={'query_param': { 'field_name': 'filters', 'serialization': 'json' }})
    

@dataclass
class QueryEventLogRequest:query_params: QueryEventLogQueryParams = field(default=None)
    

@dataclass
class QueryEventLogResponse:bounded_requests: Optional[list[shared.BoundedRequest]] = field(default=None)
    content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    status_code: int = field(default=None)
    
