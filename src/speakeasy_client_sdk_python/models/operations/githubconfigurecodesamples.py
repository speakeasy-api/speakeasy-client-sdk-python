"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import httpx
from speakeasy_client_sdk_python.models.shared import (
    githubconfigurecodesamplesresponse as shared_githubconfigurecodesamplesresponse,
)
from speakeasy_client_sdk_python.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class GithubConfigureCodeSamplesResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    github_configure_code_samples_response: NotRequired[
        shared_githubconfigurecodesamplesresponse.GithubConfigureCodeSamplesResponseTypedDict
    ]
    r"""OK"""


class GithubConfigureCodeSamplesResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""

    status_code: int
    r"""HTTP response status code for this operation"""

    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""

    github_configure_code_samples_response: Optional[
        shared_githubconfigurecodesamplesresponse.GithubConfigureCodeSamplesResponse
    ] = None
    r"""OK"""
