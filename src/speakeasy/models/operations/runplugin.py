from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import boundedrequest as shared_boundedrequest
from ..shared import error as shared_error
from ..shared import filters as shared_filters
from typing import Optional


@dataclasses.dataclass
class RunPluginRequest:
    plugin_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'pluginID', 'style': 'simple', 'explode': False }})
    filters: Optional[shared_filters.Filters] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filters', 'serialization': 'json' }})
    

@dataclasses.dataclass
class RunPluginResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bounded_requests: Optional[list[shared_boundedrequest.BoundedRequest]] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    