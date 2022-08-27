from dataclasses import dataclass, field
from typing import List,Optional
from .apiendpoint import APIEndpoint
from .error import Error

@dataclass
class GetAllAPIEndpointsV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetAllAPIEndpointsV1Request:
    path_params: GetAllAPIEndpointsV1PathParams = field(default=None)
    

@dataclass
class GetAllAPIEndpointsV1Responses:
    api_endpoint: Optional[List[APIEndpoint]] = field(default=None)
    error: Optional[Error] = field(default=None)
    raw_response: bytes = field(default=None)
    

@dataclass
class GetAllAPIEndpointsV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetAllAPIEndpointsV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
