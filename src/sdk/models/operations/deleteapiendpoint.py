from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class DeleteAPIEndpointPathParams:api_endpoint_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiEndpointID', 'style': 'simple', 'explode': False }})
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class DeleteAPIEndpointRequest:path_params: DeleteAPIEndpointPathParams = field(default=None)
    

@dataclass
class DeleteAPIEndpointResponse:content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    status_code: int = field(default=None)
    
