import dataclasses
from typing import Optional
from ..shared import error as shared_error


@dataclasses.dataclass
class GeneratePostmanCollectionForAPIEndpointPathParams:
    api_endpoint_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiEndpointID', 'style': 'simple', 'explode': False }})
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GeneratePostmanCollectionForAPIEndpointRequest:
    path_params: GeneratePostmanCollectionForAPIEndpointPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GeneratePostmanCollectionForAPIEndpointResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    postman_collection: Optional[bytes] = dataclasses.field(default=None)
    
