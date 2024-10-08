"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accounttype import AccountType
from datetime import datetime
from pydantic.functional_validators import PlainValidator
from speakeasy_client_sdk_python.types import BaseModel
from speakeasy_client_sdk_python.utils import validate_open_enum
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class OrganizationTypedDict(TypedDict):
    r"""A speakeasy organization"""
    
    account_type: AccountType
    id: str
    name: str
    telemetry_disabled: bool
    created_at: NotRequired[datetime]
    free_trial_expiry: NotRequired[datetime]
    slug: NotRequired[str]
    updated_at: NotRequired[datetime]
    

class Organization(BaseModel):
    r"""A speakeasy organization"""
    
    account_type: Annotated[AccountType, PlainValidator(validate_open_enum(False))]
    id: str
    name: str
    telemetry_disabled: bool
    created_at: Optional[datetime] = None
    free_trial_expiry: Optional[datetime] = None
    slug: Optional[str] = None
    updated_at: Optional[datetime] = None
    
