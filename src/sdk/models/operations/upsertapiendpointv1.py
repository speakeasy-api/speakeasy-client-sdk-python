from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class UpsertAPIEndpointV1PathParams:
    api_endpoint_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiEndpointID', 'style': 'simple', 'explode': False }})
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class UpsertAPIEndpointV1Request:
    path_params: UpsertAPIEndpointV1PathParams = field(default=None)
    request: shared.APIEndpoint = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class UpsertAPIEndpointV1Responses:
    api_endpoint: Optional[shared.APIEndpoint] = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    raw_response: bytes = field(default=None)
    

@dataclass
class UpsertAPIEndpointV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, UpsertAPIEndpointV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
