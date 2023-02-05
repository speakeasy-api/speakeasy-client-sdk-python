import dataclasses
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class DownloadSchemaRevisionPathParams:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    revision_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'revisionID', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DownloadSchemaRevisionRequest:
    path_params: DownloadSchemaRevisionPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DownloadSchemaRevisionResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    schema: Optional[bytes] = dataclasses.field(default=None)
    