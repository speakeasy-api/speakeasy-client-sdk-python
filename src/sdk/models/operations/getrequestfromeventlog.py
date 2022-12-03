from dataclasses import dataclass, field
from typing import Optional
from sdk.models import shared
from sdk.models import shared


@dataclass
class GetRequestFromEventLogPathParams:
    request_id: str = field(metadata={'path_param': { 'field_name': 'requestID', 'style': 'simple', 'explode': False }})
    

@dataclass
class GetRequestFromEventLogRequest:
    path_params: GetRequestFromEventLogPathParams = field()
    

@dataclass
class GetRequestFromEventLogResponse:
    content_type: str = field()
    status_code: int = field()
    error: Optional[shared.Error] = field(default=None)
    unbounded_request: Optional[shared.UnboundedRequest] = field(default=None)
    
