from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class GetSchemaPathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetSchemaRequest:
    path_params: GetSchemaPathParams = field(default=None)
    

@dataclass
class GetSchemaResponse:
    content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    schema: Optional[shared.Schema] = field(default=None)
    status_code: int = field(default=None)
    
