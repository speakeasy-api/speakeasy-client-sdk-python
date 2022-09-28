from dataclasses import dataclass, field
from typing import List,Optional
from sdk.models import shared


@dataclass
class GetAllAPIEndpointsV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetAllAPIEndpointsV1Request:
    path_params: GetAllAPIEndpointsV1PathParams = field(default=None)
    

@dataclass
class GetAllAPIEndpointsV1Responses:
    api_endpoints: Optional[List[shared.APIEndpoint]] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    

@dataclass
class GetAllAPIEndpointsV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetAllAPIEndpointsV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
