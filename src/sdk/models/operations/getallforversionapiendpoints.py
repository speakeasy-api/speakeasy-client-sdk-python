from dataclasses import dataclass, field
from typing import List,Optional
from sdk.models import shared


@dataclass
class GetAllForVersionAPIEndpointsPathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetAllForVersionAPIEndpointsRequest:
    path_params: GetAllForVersionAPIEndpointsPathParams = field(default=None)
    

@dataclass
class GetAllForVersionAPIEndpointsResponse:
    api_endpoints: Optional[List[shared.APIEndpoint]] = field(default=None)
    content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    status_code: int = field(default=None)
    
