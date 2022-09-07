from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared

@dataclass
class RegisterSchemaV1PathParams:
    api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class RegisterSchemaV1RequestBodyFile:
    content: bytes = field(default=None, metadata={'multipart_form': { 'content': True }})
    file: str = field(default=None, metadata={'multipart_form': { 'field_name': 'file' }})
    

@dataclass
class RegisterSchemaV1RequestBody:
    file: RegisterSchemaV1RequestBodyFile = field(default=None, metadata={'multipart_form': { 'file': True }})
    

@dataclass
class RegisterSchemaV1Request:
    path_params: RegisterSchemaV1PathParams = field(default=None)
    request: RegisterSchemaV1RequestBody = field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclass
class RegisterSchemaV1Responses:
    error: Optional[shared.Error] = field(default=None)
    raw_response: bytes = field(default=None)
    

@dataclass
class RegisterSchemaV1Response:
    content_type: str = field(default=None)
    responses: dict[int, dict[str, RegisterSchemaV1Responses]] = field(default=None)
    status_code: int = field(default=None)
    
