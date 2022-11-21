from dataclasses import dataclass, field
from typing import List,Optional
from sdk.models import shared


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
    api_endpoints: Optional[List[shared.APIEndpoint]] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    
