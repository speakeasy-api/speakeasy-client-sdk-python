# schemas

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
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteSchemaRequest(
    api_id="ipsa",
    revision_id="omnis",
    version_id="voluptate",
)

res = s.schemas.delete_schema(req)

if res.status_code == 200:
    # handle response
```

## download_schema

Download the latest schema for a particular apiID.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadSchemaRequest(
    api_id="cum",
    version_id="perferendis",
)

res = s.schemas.download_schema(req)

if res.schema is not None:
    # handle response
```

## download_schema_revision

Download a particular schema revision for an Api.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.DownloadSchemaRevisionRequest(
    api_id="doloremque",
    revision_id="reprehenderit",
    version_id="ut",
)

res = s.schemas.download_schema_revision(req)

if res.schema is not None:
    # handle response
```

## get_schema

Returns information about the last uploaded schema for a particular API version. 
This won't include the schema itself, that can be retrieved via the downloadSchema operation.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSchemaRequest(
    api_id="maiores",
    version_id="dicta",
)

res = s.schemas.get_schema(req)

if res.schema is not None:
    # handle response
```

## get_schema_diff

Get a diff of two schema revisions for an Api.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSchemaDiffRequest(
    api_id="corporis",
    base_revision_id="dolore",
    target_revision_id="iusto",
    version_id="dicta",
)

res = s.schemas.get_schema_diff(req)

if res.schema_diff is not None:
    # handle response
```

## get_schema_revision

Returns information about the last uploaded schema for a particular schema revision. 
This won't include the schema itself, that can be retrieved via the downloadSchema operation.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSchemaRevisionRequest(
    api_id="harum",
    revision_id="enim",
    version_id="accusamus",
)

res = s.schemas.get_schema_revision(req)

if res.schema is not None:
    # handle response
```

## get_schemas

Returns information the schemas associated with a particular apiID. 
This won't include the schemas themselves, they can be retrieved via the downloadSchema operation.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSchemasRequest(
    api_id="commodi",
    version_id="repudiandae",
)

res = s.schemas.get_schemas(req)

if res.schemata is not None:
    # handle response
```

## register_schema

Allows uploading a schema for a particular API version.
This will be used to populate ApiEndpoints and used as a base for any schema generation if present.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.RegisterSchemaRequest(
    request_body=operations.RegisterSchemaRequestBody(
        file=operations.RegisterSchemaRequestBodyFile(
            content="quae".encode(),
            file="ipsum",
        ),
    ),
    api_id="quidem",
    version_id="molestias",
)

res = s.schemas.register_schema(req)

if res.status_code == 200:
    # handle response
```
