from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class GetSchemaDiffPathParams:api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    base_revision_id: str = field(default=None, metadata={'path_param': { 'field_name': 'baseRevisionID', 'style': 'simple', 'explode': False }})
    target_revision_id: str = field(default=None, metadata={'path_param': { 'field_name': 'targetRevisionID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetSchemaDiffRequest:path_params: GetSchemaDiffPathParams = field(default=None)
    

@dataclass
class GetSchemaDiffResponse:content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    schema_diff: Optional[shared.SchemaDiff] = field(default=None)
    status_code: int = field(default=None)
    
