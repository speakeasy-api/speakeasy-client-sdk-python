# api_endpoints

## Overview

REST APIs for managing ApiEndpoint entities

### Available Operations

* [delete_api_endpoint](#delete_api_endpoint) - Delete an ApiEndpoint.
* [find_api_endpoint](#find_api_endpoint) - Find an ApiEndpoint via its displayName.
* [generate_open_api_spec_for_api_endpoint](#generate_open_api_spec_for_api_endpoint) - Generate an OpenAPI specification for a particular ApiEndpoint.
* [generate_postman_collection_for_api_endpoint](#generate_postman_collection_for_api_endpoint) - Generate a Postman collection for a particular ApiEndpoint.
* [get_all_api_endpoints](#get_all_api_endpoints) - Get all Api endpoints for a particular apiID.
* [get_all_for_version_api_endpoints](#get_all_for_version_api_endpoints) - Get all ApiEndpoints for a particular apiID and versionID.
* [get_api_endpoint](#get_api_endpoint) - Get an ApiEndpoint.
* [upsert_api_endpoint](#upsert_api_endpoint) - Upsert an ApiEndpoint.

## delete_api_endpoint

Delete an ApiEndpoint. This will also delete all associated Request Logs (if using a Postgres datastore).

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.DeleteAPIEndpointRequest(
    api_endpoint_id="delectus",
    api_id="tempora",
    version_id="suscipit",
)

res = s.api_endpoints.delete_api_endpoint(req)

if res.status_code == 200:
    # handle response
```

## find_api_endpoint

Find an ApiEndpoint via its displayName (set by operationId from a registered OpenAPI schema).
This is useful for finding the ID of an ApiEndpoint to use in the /v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID} endpoints.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.FindAPIEndpointRequest(
    api_id="molestiae",
    display_name="minus",
    version_id="placeat",
)

res = s.api_endpoints.find_api_endpoint(req)

if res.api_endpoint is not None:
    # handle response
```

## generate_open_api_spec_for_api_endpoint

This endpoint will generate a new operation in any registered OpenAPI document if the operation does not already exist in the document.
Returns the original document and the newly generated document allowing a diff to be performed to see what has changed.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GenerateOpenAPISpecForAPIEndpointRequest(
    api_endpoint_id="voluptatum",
    api_id="iusto",
    version_id="excepturi",
)

res = s.api_endpoints.generate_open_api_spec_for_api_endpoint(req)

if res.generate_open_api_spec_diff is not None:
    # handle response
```

## generate_postman_collection_for_api_endpoint

Generates a postman collection that allows the endpoint to be called from postman variables produced for any path/query/header parameters included in the OpenAPI document.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GeneratePostmanCollectionForAPIEndpointRequest(
    api_endpoint_id="nisi",
    api_id="recusandae",
    version_id="temporibus",
)

res = s.api_endpoints.generate_postman_collection_for_api_endpoint(req)

if res.postman_collection is not None:
    # handle response
```

## get_all_api_endpoints

Get all Api endpoints for a particular apiID.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAllAPIEndpointsRequest(
    api_id="ab",
)

res = s.api_endpoints.get_all_api_endpoints(req)

if res.api_endpoints is not None:
    # handle response
```

## get_all_for_version_api_endpoints

Get all ApiEndpoints for a particular apiID and versionID.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAllForVersionAPIEndpointsRequest(
    api_id="quis",
    version_id="veritatis",
)

res = s.api_endpoints.get_all_for_version_api_endpoints(req)

if res.api_endpoints is not None:
    # handle response
```

## get_api_endpoint

Get an ApiEndpoint.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAPIEndpointRequest(
    api_endpoint_id="deserunt",
    api_id="perferendis",
    version_id="ipsam",
)

res = s.api_endpoints.get_api_endpoint(req)

if res.api_endpoint is not None:
    # handle response
```

## upsert_api_endpoint

Upsert an ApiEndpoint. If the ApiEndpoint does not exist it will be created, otherwise it will be updated.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpsertAPIEndpointRequest(
    api_endpoint_input=shared.APIEndpointInput(
        api_endpoint_id="repellendus",
        description="sapiente",
        display_name="quo",
        method="odit",
        path="at",
        version_id="at",
    ),
    api_endpoint_id="maiores",
    api_id="molestiae",
    version_id="quod",
)

res = s.api_endpoints.upsert_api_endpoint(req)

if res.api_endpoint is not None:
    # handle response
```
