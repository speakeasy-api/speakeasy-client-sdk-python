from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class DeleteSchemaPathParams:api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    revision_id: str = field(default=None, metadata={'path_param': { 'field_name': 'revisionID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class DeleteSchemaRequest:path_params: DeleteSchemaPathParams = field(default=None)
    

@dataclass
class DeleteSchemaResponse:content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    status_code: int = field(default=None)
    
