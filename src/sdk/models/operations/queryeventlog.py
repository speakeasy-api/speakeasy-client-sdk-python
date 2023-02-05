import dataclasses
from ..shared import boundedrequest as shared_boundedrequest
from ..shared import error as shared_error
from ..shared import filters as shared_filters
from typing import Optional


@dataclasses.dataclass
class QueryEventLogQueryParams:
    filters: Optional[shared_filters.Filters] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filters', 'serialization': 'json' }})
    

@dataclasses.dataclass
class QueryEventLogRequest:
    query_params: QueryEventLogQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class QueryEventLogResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bounded_requests: Optional[list[shared_boundedrequest.BoundedRequest]] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    