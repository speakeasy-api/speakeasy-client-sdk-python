from dataclasses import dataclass, field
from typing import Optional
from .. import shared


@dataclass
class GetSchemaRevisionPathParams:
    api_id: str = field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    revision_id: str = field(metadata={'path_param': { 'field_name': 'revisionID', 'style': 'simple', 'explode': False }})
    version_id: str = field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetSchemaRevisionRequest:
    path_params: GetSchemaRevisionPathParams = field()
    

@dataclass
class GetSchemaRevisionResponse:
    content_type: str = field()
    status_code: int = field()
    error: Optional[shared.Error] = field(default=None)
    schema: Optional[shared.Schema] = field(default=None)
    
