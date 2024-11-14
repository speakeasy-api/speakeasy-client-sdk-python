"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
import pydantic
from speakeasy_client_sdk_python.models.shared import (
    api as shared_api,
    api_input as shared_api_input,
)
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import (
    FieldMetadata,
    PathParamMetadata,
    RequestMetadata,
)
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpsertAPIRequestTypedDict(TypedDict):
    api_id: str
    r"""The ID of the Api to upsert."""
    api: shared_api_input.APIInputTypedDict
    r"""A JSON representation of the Api to upsert"""


class UpsertAPIRequest(BaseModel):
    api_id: Annotated[
        str,
        pydantic.Field(alias="apiID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The ID of the Api to upsert."""

    api: Annotated[
        shared_api_input.APIInput,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""A JSON representation of the Api to upsert"""


class UpsertAPIResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    api: NotRequired[shared_api.APITypedDict]
    r"""OK"""


class UpsertAPIResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    api: Optional[shared_api.API] = None
    r"""OK"""
