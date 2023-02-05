import dataclasses
from ..shared import apiendpoint as shared_apiendpoint
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class FindAPIEndpointPathParams:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    display_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'displayName', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FindAPIEndpointRequest:
    path_params: FindAPIEndpointPathParams = dataclasses.field()
    

@dataclasses.dataclass
class FindAPIEndpointResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    api_endpoint: Optional[shared_apiendpoint.APIEndpoint] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    