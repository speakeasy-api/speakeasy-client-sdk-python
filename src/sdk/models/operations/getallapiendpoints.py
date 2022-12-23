from dataclasses import dataclass, field
from typing import Optional
from .. import shared


@dataclass
class GetAllAPIEndpointsPathParams:
    api_id: str = field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetAllAPIEndpointsRequest:
    path_params: GetAllAPIEndpointsPathParams = field()
    

@dataclass
class GetAllAPIEndpointsResponse:
    content_type: str = field()
    status_code: int = field()
    api_endpoints: Optional[list[shared.APIEndpoint]] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    
