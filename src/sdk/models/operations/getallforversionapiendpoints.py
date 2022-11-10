from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class GetAllForVersionAPIEndpointsPathParams:
    api_id: str = field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetAllForVersionAPIEndpointsRequest:
    path_params: GetAllForVersionAPIEndpointsPathParams = field()
    

@dataclass
class GetAllForVersionAPIEndpointsResponse:
    content_type: str = field()
    status_code: int = field()
    api_endpoints: Optional[list[shared.APIEndpoint]] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    
