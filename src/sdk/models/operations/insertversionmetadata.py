from dataclasses import dataclass, field
from typing import Optional
from .. import shared


@dataclass
class InsertVersionMetadataPathParams:
    api_id: str = field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class InsertVersionMetadataRequest:
    path_params: InsertVersionMetadataPathParams = field()
    request: shared.VersionMetadataInput = field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclass
class InsertVersionMetadataResponse:
    content_type: str = field()
    status_code: int = field()
    error: Optional[shared.Error] = field(default=None)
    version_metadata: Optional[shared.VersionMetadata] = field(default=None)
    
