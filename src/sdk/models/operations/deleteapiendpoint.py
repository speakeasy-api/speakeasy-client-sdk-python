from dataclasses import dataclass, field
from typing import Optional
from .. import shared


@dataclass
class DeleteAPIEndpointPathParams:
    api_endpoint_id: str = field(metadata={'path_param': { 'field_name': 'apiEndpointID', 'style': 'simple', 'explode': False }})
    api_id: str = field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class DeleteAPIEndpointRequest:
    path_params: DeleteAPIEndpointPathParams = field()
    

@dataclass
class DeleteAPIEndpointResponse:
    content_type: str = field()
    status_code: int = field()
    error: Optional[shared.Error] = field(default=None)
    
