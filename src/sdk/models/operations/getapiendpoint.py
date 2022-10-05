from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class GetAPIEndpointPathParams:
    api_endpoint_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiEndpointID', 'style': 'simple', 'explode': False }})
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetAPIEndpointRequest:
    path_params: GetAPIEndpointPathParams = field(default=None)
    

@dataclass
class GetAPIEndpointResponses:
    api_endpoint: Optional[shared.APIEndpoint] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    

@dataclass
class GetAPIEndpointResponse:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetAPIEndpointResponses]] = field(default=None)
    status_code: int = field(default=None)
    
