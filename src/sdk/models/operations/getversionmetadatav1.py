from dataclasses import dataclass, field
from typing import List,Optional
from sdk.models import shared

@dataclass
class GetVersionMetadataV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetVersionMetadataV1Request:
    path_params: GetVersionMetadataV1PathParams = field(default=None)
    

@dataclass
class GetVersionMetadataV1Responses:
    error: Optional[shared.Error] = field(default=None)
    raw_response: bytes = field(default=None)
    version_metadata: Optional[List[shared.VersionMetadata]] = field(default=None)
    

@dataclass
class GetVersionMetadataV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, GetVersionMetadataV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
