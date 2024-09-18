"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from speakeasy_client_sdk_python.types import BaseModel
from typing import List, TypedDict


class AddTagsTypedDict(TypedDict):
    r"""Request body of tags to add to a revision"""

    revision_digest: str
    r"""revision digest to add tags too sha256:..."""
    tags: List[str]
    r"""string tags to add to the revision"""


class AddTags(BaseModel):
    r"""Request body of tags to add to a revision"""

    revision_digest: str
    r"""revision digest to add tags too sha256:..."""

    tags: List[str]
    r"""string tags to add to the revision"""
