"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
import pydantic
from speakeasy_client_sdk_python.models.shared import suggestedoperationids as shared_suggestedoperationids, suggestoperationidsopts as shared_suggestoperationidsopts
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, HeaderMetadata, PathParamMetadata, QueryParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class SuggestOperationIDsRegistryRequestTypedDict(TypedDict):
    x_session_id: str
    namespace_name: str
    revision_reference: str
    r"""Tag or digest"""
    limit: NotRequired[float]
    r"""Max number of suggestions to request"""
    suggest_operation_i_ds_opts: NotRequired[shared_suggestoperationidsopts.SuggestOperationIDsOptsTypedDict]
    r"""The schema file to upload provided as a multipart/form-data file segment."""
    

class SuggestOperationIDsRegistryRequest(BaseModel):
    x_session_id: Annotated[str, pydantic.Field(alias="x-session-id"), FieldMetadata(header=HeaderMetadata(style="simple", explode=False))]
    namespace_name: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    revision_reference: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Tag or digest"""
    limit: Annotated[Optional[float], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Max number of suggestions to request"""
    suggest_operation_i_ds_opts: Annotated[Optional[shared_suggestoperationidsopts.SuggestOperationIDsOpts], FieldMetadata(request=RequestMetadata(media_type="application/json"))] = None
    r"""The schema file to upload provided as a multipart/form-data file segment."""
    

class SuggestOperationIDsRegistryResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    suggested_operation_i_ds: NotRequired[shared_suggestedoperationids.SuggestedOperationIDsTypedDict]
    r"""OK"""
    

class SuggestOperationIDsRegistryResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    suggested_operation_i_ds: Optional[shared_suggestedoperationids.SuggestedOperationIDs] = None
    r"""OK"""
    
