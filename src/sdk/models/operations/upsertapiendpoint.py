from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class UpsertAPIEndpointPathParams:api_endpoint_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiEndpointID', 'style': 'simple', 'explode': False }})
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class UpsertAPIEndpointRequest:path_params: UpsertAPIEndpointPathParams = field(default=None)
    request: shared.APIEndpoint = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class UpsertAPIEndpointResponse:api_endpoint: Optional[shared.APIEndpoint] = field(default=None)
    content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    status_code: int = field(default=None)
    
