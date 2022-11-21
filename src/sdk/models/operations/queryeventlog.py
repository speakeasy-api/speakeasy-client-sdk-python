from dataclasses import dataclass, field
from typing import List,Optional
from sdk.models import shared


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
    bounded_requests: Optional[List[shared.BoundedRequest]] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    
