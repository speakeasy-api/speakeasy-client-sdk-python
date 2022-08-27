from dataclasses import dataclass, field
from typing import Optional
from .error import Error

@dataclass
class DeleteAPIEndpointV1PathParams:
    api_endpoint_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiEndpointID', 'style': 'simple', 'explode': False }})
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class DeleteAPIEndpointV1Request:
    path_params: DeleteAPIEndpointV1PathParams = field(default=None)
    

@dataclass
class DeleteAPIEndpointV1Responses:
    error: Optional[Error] = field(default=None)
    raw_response: bytes = field(default=None)
    

@dataclass
class DeleteAPIEndpointV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, DeleteAPIEndpointV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
