# metadata

## Overview

REST APIs for managing Version Metadata entities

### Available Operations

* [delete_version_metadata](#delete_version_metadata) - Delete metadata for a particular apiID and versionID.
* [get_version_metadata](#get_version_metadata) - Get all metadata for a particular apiID and versionID.
* [insert_version_metadata](#insert_version_metadata) - Insert metadata for a particular apiID and versionID.

## delete_version_metadata

Delete metadata for a particular apiID and versionID.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteVersionMetadataRequest(
    api_id='excepturi',
    meta_key='accusantium',
    meta_value='iure',
    version_id='culpa',
)

res = s.metadata.delete_version_metadata(req)

if res.status_code == 200:
    # handle response
```

## get_version_metadata

Get all metadata for a particular apiID and versionID.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetVersionMetadataRequest(
    api_id='doloribus',
    version_id='sapiente',
)

res = s.metadata.get_version_metadata(req)

if res.version_metadata is not None:
    # handle response
```

## insert_version_metadata

Insert metadata for a particular apiID and versionID.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.InsertVersionMetadataRequest(
    version_metadata_input=shared.VersionMetadataInput(
        meta_key='architecto',
        meta_value='mollitia',
    ),
    api_id='dolorem',
    version_id='culpa',
)

res = s.metadata.insert_version_metadata(req)

if res.version_metadata is not None:
    # handle response
```
