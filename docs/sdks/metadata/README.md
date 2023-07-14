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
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
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

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.DeleteVersionMetadataRequest](../../models/operations/deleteversionmetadatarequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.DeleteVersionMetadataResponse](../../models/operations/deleteversionmetadataresponse.md)**


## get_version_metadata

Get all metadata for a particular apiID and versionID.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
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

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetVersionMetadataRequest](../../models/operations/getversionmetadatarequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetVersionMetadataResponse](../../models/operations/getversionmetadataresponse.md)**


## insert_version_metadata

Insert metadata for a particular apiID and versionID.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
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

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.InsertVersionMetadataRequest](../../models/operations/insertversionmetadatarequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.InsertVersionMetadataResponse](../../models/operations/insertversionmetadataresponse.md)**

