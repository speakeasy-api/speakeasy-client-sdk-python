from dataclasses import dataclass, field
from typing import List,Optional
from sdk.models import shared


@dataclass
class GetAllForVersionAPIEndpointsV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetAllForVersionAPIEndpointsV1Request:
    path_params: GetAllForVersionAPIEndpointsV1PathParams = field(default=None)
    

@dataclass
class GetAllForVersionAPIEndpointsV1Responses:
    api_endpoints: Optional[List[shared.APIEndpoint]] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    

@dataclass
class GetAllForVersionAPIEndpointsV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetAllForVersionAPIEndpointsV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
