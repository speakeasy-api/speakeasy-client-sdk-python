from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class GetVersionMetadataPathParams:api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetVersionMetadataRequest:path_params: GetVersionMetadataPathParams = field(default=None)
    

@dataclass
class GetVersionMetadataResponse:content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    status_code: int = field(default=None)
    version_metadata: Optional[list[shared.VersionMetadata]] = field(default=None)
    
