import dataclasses
from ..shared import error as shared_error
from ..shared import schemadiff as shared_schemadiff
from typing import Optional


@dataclasses.dataclass
class GetSchemaDiffPathParams:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    base_revision_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'baseRevisionID', 'style': 'simple', 'explode': False }})
    target_revision_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'targetRevisionID', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetSchemaDiffRequest:
    path_params: GetSchemaDiffPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetSchemaDiffResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    schema_diff: Optional[shared_schemadiff.SchemaDiff] = dataclasses.field(default=None)
    