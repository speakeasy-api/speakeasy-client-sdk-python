"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from speakeasy import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FeatureFlag:
    r"""A feature flag is a key-value pair that can be used to enable or disable features."""
    UNSET='__SPEAKEASY_UNSET__'
    feature_flag: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('feature_flag') }})
    trial_ends_at: Optional[datetime] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('trial_ends_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is FeatureFlag.UNSET }})
    
