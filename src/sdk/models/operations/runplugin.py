import dataclasses
from ..shared import boundedrequest as shared_boundedrequest
from ..shared import error as shared_error
from ..shared import filters as shared_filters
from typing import Optional


@dataclasses.dataclass
class RunPluginPathParams:
    plugin_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'pluginID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RunPluginQueryParams:
    filters: Optional[shared_filters.Filters] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filters', 'serialization': 'json' }})
    

@dataclasses.dataclass
class RunPluginRequest:
    path_params: RunPluginPathParams = dataclasses.field()
    query_params: RunPluginQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class RunPluginResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bounded_requests: Optional[list[shared_boundedrequest.BoundedRequest]] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    