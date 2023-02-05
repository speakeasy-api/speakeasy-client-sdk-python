import dataclasses
from ..shared import apiendpoint as shared_apiendpoint
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class UpsertAPIEndpointPathParams:
    api_endpoint_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiEndpointID', 'style': 'simple', 'explode': False }})
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UpsertAPIEndpointRequest:
    path_params: UpsertAPIEndpointPathParams = dataclasses.field()
    request: shared_apiendpoint.APIEndpointInput = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpsertAPIEndpointResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    api_endpoint: Optional[shared_apiendpoint.APIEndpoint] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    