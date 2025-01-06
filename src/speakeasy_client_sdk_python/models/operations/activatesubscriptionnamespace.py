"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
import pydantic
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class ActivateSubscriptionNamespaceRequestTypedDict(TypedDict):
    subscription_id: str
    r"""The existing subscription ID"""
    namespace_name: str
    r"""The namespace name"""


class ActivateSubscriptionNamespaceRequest(BaseModel):
    subscription_id: Annotated[
        str,
        pydantic.Field(alias="subscriptionID"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The existing subscription ID"""

    namespace_name: Annotated[
        str,
        pydantic.Field(alias="namespaceName"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The namespace name"""


class ActivateSubscriptionNamespaceResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""


class ActivateSubscriptionNamespaceResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
