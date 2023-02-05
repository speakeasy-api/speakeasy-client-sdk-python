import dataclasses
from ..shared import apiendpoint as shared_apiendpoint
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class GetAllAPIEndpointsPathParams:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetAllAPIEndpointsRequest:
    path_params: GetAllAPIEndpointsPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetAllAPIEndpointsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    api_endpoints: Optional[list[shared_apiendpoint.APIEndpoint]] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    