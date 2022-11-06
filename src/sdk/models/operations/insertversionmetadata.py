from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class InsertVersionMetadataPathParams:api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class InsertVersionMetadataRequest:path_params: InsertVersionMetadataPathParams = field(default=None)
    request: shared.VersionMetadata = field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class InsertVersionMetadataResponse:content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    status_code: int = field(default=None)
    version_metadata: Optional[shared.VersionMetadata] = field(default=None)
    
