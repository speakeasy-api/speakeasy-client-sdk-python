import dataclasses
from ..shared import error as shared_error
from ..shared import versionmetadata as shared_versionmetadata
from typing import Optional


@dataclasses.dataclass
class GetVersionMetadataPathParams:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GetVersionMetadataRequest:
    path_params: GetVersionMetadataPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GetVersionMetadataResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    version_metadata: Optional[list[shared_versionmetadata.VersionMetadata]] = dataclasses.field(default=None)
    