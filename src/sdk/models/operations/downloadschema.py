from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class DownloadSchemaPathParams:api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class DownloadSchemaRequest:path_params: DownloadSchemaPathParams = field(default=None)
    

@dataclass
class DownloadSchemaResponse:content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    schema: Optional[bytes] = field(default=None)
    status_code: int = field(default=None)
    
