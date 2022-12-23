from dataclasses import dataclass, field
from typing import Optional
from .. import shared


@dataclass
class GetAPIEndpointPathParams:
    api_endpoint_id: str = field(metadata={'path_param': { 'field_name': 'apiEndpointID', 'style': 'simple', 'explode': False }})
    api_id: str = field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetAPIEndpointRequest:
    path_params: GetAPIEndpointPathParams = field()
    

@dataclass
class GetAPIEndpointResponse:
    content_type: str = field()
    status_code: int = field()
    api_endpoint: Optional[shared.APIEndpoint] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    
