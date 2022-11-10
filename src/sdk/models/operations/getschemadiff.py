from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class GetSchemaDiffPathParams:
    api_id: str = field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    base_revision_id: str = field(metadata={'path_param': { 'field_name': 'baseRevisionID', 'style': 'simple', 'explode': False }})
    target_revision_id: str = field(metadata={'path_param': { 'field_name': 'targetRevisionID', 'style': 'simple', 'explode': False }})
    version_id: str = field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetSchemaDiffRequest:
    path_params: GetSchemaDiffPathParams = field()
    

@dataclass
class GetSchemaDiffResponse:
    content_type: str = field()
    status_code: int = field()
    error: Optional[shared.Error] = field(default=None)
    schema_diff: Optional[shared.SchemaDiff] = field(default=None)
    
