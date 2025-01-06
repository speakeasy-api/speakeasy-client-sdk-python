"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accounttype import AccountType
from datetime import datetime
from pydantic import model_serializer
from pydantic.functional_validators import PlainValidator
from speakeasy_client_sdk_python.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from speakeasy_client_sdk_python.utils import validate_open_enum
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class OrganizationTypedDict(TypedDict):
    r"""A speakeasy organization"""

    account_type: AccountType
    created_at: datetime
    id: str
    name: str
    slug: str
    sso_activated: bool
    telemetry_disabled: bool
    updated_at: datetime
    free_trial_expiry: NotRequired[Nullable[datetime]]
    internal: NotRequired[bool]
    sso_connection_id: NotRequired[Nullable[str]]


class Organization(BaseModel):
    r"""A speakeasy organization"""

    account_type: Annotated[AccountType, PlainValidator(validate_open_enum(False))]

    created_at: datetime

    id: str

    name: str

    slug: str

    sso_activated: bool

    telemetry_disabled: bool

    updated_at: datetime

    free_trial_expiry: OptionalNullable[datetime] = UNSET

    internal: Optional[bool] = None

    sso_connection_id: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["free_trial_expiry", "internal", "sso_connection_id"]
        nullable_fields = ["free_trial_expiry", "sso_connection_id"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
