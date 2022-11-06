from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared


@dataclass
class RegisterSchemaPathParams:api_id: str = field(default=None, metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    version_id: str = field(default=None, metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    

@dataclass
class RegisterSchemaRequestBodyFile:content: bytes = field(default=None, metadata={'multipart_form': { 'content': True }})
    file: str = field(default=None, metadata={'multipart_form': { 'field_name': 'file' }})
    

@dataclass
class RegisterSchemaRequestBody:file: RegisterSchemaRequestBodyFile = field(default=None, metadata={'multipart_form': { 'file': True }})
    

@dataclass
class RegisterSchemaRequest:path_params: RegisterSchemaPathParams = field(default=None)
    request: RegisterSchemaRequestBody = field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclass
class RegisterSchemaResponse:content_type: str = field(default=None)
    error: Optional[shared.Error] = field(default=None)
    status_code: int = field(default=None)
    
