from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class FindAPIEndpointV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    display_name: str = field(default=None, metadata={'path_param': { 'field_name': 'displayName', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class FindAPIEndpointV1Request:
    path_params: FindAPIEndpointV1PathParams = field(default=None)
    

@dataclass
class FindAPIEndpointV1Responses:
    api_endpoint: Optional[shared.APIEndpoint] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    raw_response: bytes = field(default=None)
    

@dataclass
class FindAPIEndpointV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, FindAPIEndpointV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
