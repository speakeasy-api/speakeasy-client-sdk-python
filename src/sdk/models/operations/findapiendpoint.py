from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class FindAPIEndpointPathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    display_name: str = field(default=None, metadata={'path_param': { 'field_name': 'displayName', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class FindAPIEndpointRequest:
    path_params: FindAPIEndpointPathParams = field(default=None)
    

@dataclass
class FindAPIEndpointResponses:
    api_endpoint: Optional[shared.APIEndpoint] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    

@dataclass
class FindAPIEndpointResponse:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, FindAPIEndpointResponses]] = field(default=None)
    status_code: int = field(default=None)
    
