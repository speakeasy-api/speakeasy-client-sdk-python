from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared
from sdk.models import shared


@dataclass
class DownloadSchemaRevisionPathParams:
    api_id: str = field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    revision_id: str = field(metadata={'path_param': { 'field_name': 'revisionID', 'style': 'simple', 'explode': False }})
    version_id: str = field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class DownloadSchemaRevisionRequest:
    path_params: DownloadSchemaRevisionPathParams = field()
    

@dataclass
class DownloadSchemaRevisionResponse:
    content_type: str = field()
    status_code: int = field()
    error: Optional[shared.Error] = field(default=None)
    schema: Optional[bytes] = field(default=None)
    
