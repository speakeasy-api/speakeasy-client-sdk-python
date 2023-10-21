# Schemas
(*schemas*)

## Overview

REST APIs for managing Schema entities

### Available Operations

* [delete_schema](#delete_schema) - Delete a particular schema revision for an Api.
* [download_schema](#download_schema) - Download the latest schema for a particular apiID.
* [download_schema_revision](#download_schema_revision) - Download a particular schema revision for an Api.
* [get_schema](#get_schema) - Get information about the latest schema.
* [get_schema_diff](#get_schema_diff) - Get a diff of two schema revisions for an Api.
* [get_schema_revision](#get_schema_revision) - Get information about a particular schema revision for an Api.
* [get_schemas](#get_schemas) - Get information about all schemas associated with a particular apiID.
* [register_schema](#register_schema) - Register a schema.

## delete_schema

Delete a particular schema revision for an Api.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.DeleteSchemaRequest(
    api_id='string',
    revision_id='string',
    version_id='string',
)

res = s.schemas.delete_schema(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteSchemaRequest](../../models/operations/deleteschemarequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteSchemaResponse](../../models/operations/deleteschemaresponse.md)**


## download_schema

Download the latest schema for a particular apiID.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.DownloadSchemaRequest(
    api_id='string',
    version_id='string',
)

res = s.schemas.download_schema(req)

if res.schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.DownloadSchemaRequest](../../models/operations/downloadschemarequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.DownloadSchemaResponse](../../models/operations/downloadschemaresponse.md)**


## download_schema_revision

Download a particular schema revision for an Api.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.DownloadSchemaRevisionRequest(
    api_id='string',
    revision_id='string',
    version_id='string',
)

res = s.schemas.download_schema_revision(req)

if res.schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.DownloadSchemaRevisionRequest](../../models/operations/downloadschemarevisionrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.DownloadSchemaRevisionResponse](../../models/operations/downloadschemarevisionresponse.md)**


## get_schema

Returns information about the last uploaded schema for a particular API version. 
This won't include the schema itself, that can be retrieved via the downloadSchema operation.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetSchemaRequest(
    api_id='string',
    version_id='string',
)

res = s.schemas.get_schema(req)

if res.schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetSchemaRequest](../../models/operations/getschemarequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetSchemaResponse](../../models/operations/getschemaresponse.md)**


## get_schema_diff

Get a diff of two schema revisions for an Api.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetSchemaDiffRequest(
    api_id='string',
    base_revision_id='string',
    target_revision_id='string',
    version_id='string',
)

res = s.schemas.get_schema_diff(req)

if res.schema_diff is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetSchemaDiffRequest](../../models/operations/getschemadiffrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetSchemaDiffResponse](../../models/operations/getschemadiffresponse.md)**


## get_schema_revision

Returns information about the last uploaded schema for a particular schema revision. 
This won't include the schema itself, that can be retrieved via the downloadSchema operation.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetSchemaRevisionRequest(
    api_id='string',
    revision_id='string',
    version_id='string',
)

res = s.schemas.get_schema_revision(req)

if res.schema is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.GetSchemaRevisionRequest](../../models/operations/getschemarevisionrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.GetSchemaRevisionResponse](../../models/operations/getschemarevisionresponse.md)**


## get_schemas

Returns information the schemas associated with a particular apiID. 
This won't include the schemas themselves, they can be retrieved via the downloadSchema operation.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetSchemasRequest(
    api_id='string',
    version_id='string',
)

res = s.schemas.get_schemas(req)

if res.schemata is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetSchemasRequest](../../models/operations/getschemasrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetSchemasResponse](../../models/operations/getschemasresponse.md)**


## register_schema

Allows uploading a schema for a particular API version.
This will be used to populate ApiEndpoints and used as a base for any schema generation if present.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.RegisterSchemaRequest(
    request_body=operations.RegisterSchemaRequestBody(
        file=operations.RegisterSchemaRequestBodyFile(
            content='mg|mf".]!\'.encode(),
            file='string',
        ),
    ),
    api_id='string',
    version_id='string',
)

res = s.schemas.register_schema(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.RegisterSchemaRequest](../../models/operations/registerschemarequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.RegisterSchemaResponse](../../models/operations/registerschemaresponse.md)**

