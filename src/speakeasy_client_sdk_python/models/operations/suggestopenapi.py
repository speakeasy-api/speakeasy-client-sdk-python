"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
import io
import pydantic
from speakeasy_client_sdk_python.models.shared import (
    suggestoptsold as shared_suggestoptsold,
)
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import (
    FieldMetadata,
    HeaderMetadata,
    MultipartFormMetadata,
    RequestMetadata,
)
from typing import IO, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


class SchemaTypedDict(TypedDict):
    content: Union[bytes, IO[bytes], io.BufferedReader]
    file_name: str
    content_type: NotRequired[str]


class Schema(BaseModel):
    content: Annotated[
        Union[bytes, IO[bytes], io.BufferedReader],
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(content=True)),
    ]

    file_name: Annotated[
        str, pydantic.Field(alias="schema"), FieldMetadata(multipart=True)
    ]

    content_type: Annotated[
        Optional[str],
        pydantic.Field(alias="Content-Type"),
        FieldMetadata(multipart=True),
    ] = None


class SuggestOpenAPIRequestBodyTypedDict(TypedDict):
    r"""The schema file to upload provided as a multipart/form-data file segment."""

    schema_: SchemaTypedDict
    opts: NotRequired[shared_suggestoptsold.SuggestOptsOldTypedDict]


class SuggestOpenAPIRequestBody(BaseModel):
    r"""The schema file to upload provided as a multipart/form-data file segment."""

    schema_: Annotated[
        Schema,
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(file=True)),
    ]

    opts: Annotated[
        Optional[shared_suggestoptsold.SuggestOptsOld],
        FieldMetadata(multipart=MultipartFormMetadata(json=True)),
    ] = None


class SuggestOpenAPIRequestTypedDict(TypedDict):
    x_session_id: str
    request_body: SuggestOpenAPIRequestBodyTypedDict
    r"""The schema file to upload provided as a multipart/form-data file segment."""


class SuggestOpenAPIRequest(BaseModel):
    x_session_id: Annotated[
        str,
        pydantic.Field(alias="x-session-id"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ]

    request_body: Annotated[
        SuggestOpenAPIRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="multipart/form-data")),
    ]
    r"""The schema file to upload provided as a multipart/form-data file segment."""


class SuggestOpenAPIResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    schema_: NotRequired[httpx.Response]
    r"""An overlay containing the suggested spec modifications."""


class SuggestOpenAPIResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    schema_: Optional[httpx.Response] = None
    r"""An overlay containing the suggested spec modifications."""
