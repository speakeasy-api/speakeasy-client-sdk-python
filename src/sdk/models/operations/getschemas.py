from dataclasses import dataclass, field
from typing import Optional
from .. import shared


@dataclass
class GetSchemasPathParams:
    api_id: str = field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetSchemasRequest:
    path_params: GetSchemasPathParams = field()
    

@dataclass
class GetSchemasResponse:
    content_type: str = field()
    status_code: int = field()
    error: Optional[shared.Error] = field(default=None)
    schemata: Optional[list[shared.Schema]] = field(default=None)
    
