# apis

## Overview

REST APIs for managing Api entities

### Available Operations

* [delete_api](#delete_api) - Delete an Api.
* [generate_open_api_spec](#generate_open_api_spec) - Generate an OpenAPI specification for a particular Api.
* [generate_postman_collection](#generate_postman_collection) - Generate a Postman collection for a particular Api.
* [get_all_api_versions](#get_all_api_versions) - Get all Api versions for a particular ApiEndpoint.
* [get_apis](#get_apis) - Get a list of Apis for a given workspace
* [upsert_api](#upsert_api) - Upsert an Api

## delete_api

Delete a particular version of an Api. The will also delete all associated ApiEndpoints, Metadata, Schemas & Request Logs (if using a Postgres datastore).

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.DeleteAPIRequest(
    api_id='quod',
    version_id='esse',
)

res = s.apis.delete_api(req)

if res.status_code == 200:
    # handle response
```

## generate_open_api_spec

This endpoint will generate any missing operations in any registered OpenAPI document if the operation does not already exist in the document.
Returns the original document and the newly generated document allowing a diff to be performed to see what has changed.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GenerateOpenAPISpecRequest(
    api_id='totam',
    version_id='porro',
)

res = s.apis.generate_open_api_spec(req)

if res.generate_open_api_spec_diff is not None:
    # handle response
```

## generate_postman_collection

Generates a postman collection containing all endpoints for a particular API. Includes variables produced for any path/query/header parameters included in the OpenAPI document.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GeneratePostmanCollectionRequest(
    api_id='dolorum',
    version_id='dicta',
)

res = s.apis.generate_postman_collection(req)

if res.postman_collection is not None:
    # handle response
```

## get_all_api_versions

Get all Api versions for a particular ApiEndpoint.
Supports filtering the versions based on metadata attributes.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetAllAPIVersionsRequest(
    api_id='nam',
    metadata={
        "occaecati": [
            'deleniti',
        ],
        "hic": [
            'totam',
            'beatae',
            'commodi',
            'molestiae',
        ],
        "modi": [
            'impedit',
        ],
    },
    op=operations.GetAllAPIVersionsOp(
        and_=False,
    ),
)

res = s.apis.get_all_api_versions(req)

if res.apis is not None:
    # handle response
```

## get_apis

Get a list of all Apis and their versions for a given workspace.
Supports filtering the APIs based on metadata attributes.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetApisRequest(
    metadata={
        "esse": [
            'excepturi',
        ],
        "aspernatur": [
            'ad',
        ],
        "natus": [
            'iste',
        ],
    },
    op=operations.GetApisOp(
        and_=False,
    ),
)

res = s.apis.get_apis(req)

if res.apis is not None:
    # handle response
```

## upsert_api

Upsert an Api. If the Api does not exist, it will be created.
If the Api exists, it will be updated.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.UpsertAPIRequest(
    api_input=shared.APIInput(
        api_id='dolor',
        description='natus',
        meta_data={
            "hic": [
                'fuga',
                'in',
                'corporis',
                'iste',
            ],
            "iure": [
                'quidem',
                'architecto',
                'ipsa',
                'reiciendis',
            ],
        },
        version_id='est',
    ),
    api_id='mollitia',
)

res = s.apis.upsert_api(req)

if res.api is not None:
    # handle response
```
