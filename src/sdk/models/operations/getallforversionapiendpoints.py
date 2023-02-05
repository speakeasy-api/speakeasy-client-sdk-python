import dataclasses
from ..shared import apiendpoint as shared_apiendpoint
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class GetAllForVersionAPIEndpointsPathParams:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetAllForVersionAPIEndpointsRequest:
    path_params: GetAllForVersionAPIEndpointsPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetAllForVersionAPIEndpointsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    api_endpoints: Optional[list[shared_apiendpoint.APIEndpoint]] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    