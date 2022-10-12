from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class GeneratePostmanCollectionForAPIEndpointPathParams:
    api_endpoint_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiEndpointID', 'style': 'simple', 'explode': False }})
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GeneratePostmanCollectionForAPIEndpointRequest:
    path_params: GeneratePostmanCollectionForAPIEndpointPathParams = field(default=None)
    

@dataclass
class GeneratePostmanCollectionForAPIEndpointResponse:
    content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    postman_collection: Optional[bytes] = field(default=None)
    status_code: int = field(default=None)
    
