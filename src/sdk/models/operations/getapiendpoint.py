import dataclasses
from typing import Optional
from ..shared import apiendpoint as shared_apiendpoint
from ..shared import error as shared_error


@dataclasses.dataclass
class GetAPIEndpointPathParams:
    api_endpoint_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiEndpointID', 'style': 'simple', 'explode': False }})
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetAPIEndpointRequest:
    path_params: GetAPIEndpointPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetAPIEndpointResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    api_endpoint: Optional[shared_apiendpoint.APIEndpoint] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    
