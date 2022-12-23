from dataclasses import dataclass, field
from typing import Optional
from .. import shared


@dataclass
class DeleteAPIPathParams:
    api_id: str = field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class DeleteAPIRequest:
    path_params: DeleteAPIPathParams = field()
    

@dataclass
class DeleteAPIResponse:
    content_type: str = field()
    status_code: int = field()
    error: Optional[shared.Error] = field(default=None)
    
