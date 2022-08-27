from dataclasses import dataclass, field
from typing import Optional
from .apiendpoint import APIEndpoint
from .error import Error

@dataclass
class GetAPIEndpointV1PathParams:
    api_endpoint_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiEndpointID', 'style': 'simple', 'explode': False }})
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetAPIEndpointV1Request:
    path_params: GetAPIEndpointV1PathParams = field(default=None)
    

@dataclass
class GetAPIEndpointV1Responses:
    api_endpoint: Optional[APIEndpoint] = field(default=None)
    error: Optional[Error] = field(default=None)
    raw_response: bytes = field(default=None)
    

@dataclass
class GetAPIEndpointV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetAPIEndpointV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
