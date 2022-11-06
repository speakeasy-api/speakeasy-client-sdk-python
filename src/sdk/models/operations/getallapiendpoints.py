from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class GetAllAPIEndpointsPathParams:api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetAllAPIEndpointsRequest:path_params: GetAllAPIEndpointsPathParams = field(default=None)
    

@dataclass
class GetAllAPIEndpointsResponse:api_endpoints: Optional[list[shared.APIEndpoint]] = field(default=None)
    content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    status_code: int = field(default=None)
    
