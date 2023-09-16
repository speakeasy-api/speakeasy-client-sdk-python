# APIEndpoints

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
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.DeleteAPIEndpointRequest(
    api_endpoint_id='distinctio',
    api_id='quibusdam',
    version_id='unde',
)

res = s.api_endpoints.delete_api_endpoint(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteAPIEndpointRequest](../../models/operations/deleteapiendpointrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.DeleteAPIEndpointResponse](../../models/operations/deleteapiendpointresponse.md)**


## find_api_endpoint

Find an ApiEndpoint via its displayName (set by operationId from a registered OpenAPI schema).
This is useful for finding the ID of an ApiEndpoint to use in the /v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID} endpoints.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.FindAPIEndpointRequest(
    api_id='nulla',
    display_name='corrupti',
    version_id='illum',
)

res = s.api_endpoints.find_api_endpoint(req)

if res.api_endpoint is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.FindAPIEndpointRequest](../../models/operations/findapiendpointrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.FindAPIEndpointResponse](../../models/operations/findapiendpointresponse.md)**


## generate_open_api_spec_for_api_endpoint

This endpoint will generate a new operation in any registered OpenAPI document if the operation does not already exist in the document.
Returns the original document and the newly generated document allowing a diff to be performed to see what has changed.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GenerateOpenAPISpecForAPIEndpointRequest(
    api_endpoint_id='vel',
    api_id='error',
    version_id='deserunt',
)

res = s.api_endpoints.generate_open_api_spec_for_api_endpoint(req)

if res.generate_open_api_spec_diff is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.GenerateOpenAPISpecForAPIEndpointRequest](../../models/operations/generateopenapispecforapiendpointrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.GenerateOpenAPISpecForAPIEndpointResponse](../../models/operations/generateopenapispecforapiendpointresponse.md)**


## generate_postman_collection_for_api_endpoint

Generates a postman collection that allows the endpoint to be called from postman variables produced for any path/query/header parameters included in the OpenAPI document.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GeneratePostmanCollectionForAPIEndpointRequest(
    api_endpoint_id='suscipit',
    api_id='iure',
    version_id='magnam',
)

res = s.api_endpoints.generate_postman_collection_for_api_endpoint(req)

if res.postman_collection is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [operations.GeneratePostmanCollectionForAPIEndpointRequest](../../models/operations/generatepostmancollectionforapiendpointrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.GeneratePostmanCollectionForAPIEndpointResponse](../../models/operations/generatepostmancollectionforapiendpointresponse.md)**


## get_all_api_endpoints

Get all Api endpoints for a particular apiID.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetAllAPIEndpointsRequest(
    api_id='debitis',
)

res = s.api_endpoints.get_all_api_endpoints(req)

if res.api_endpoints is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetAllAPIEndpointsRequest](../../models/operations/getallapiendpointsrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetAllAPIEndpointsResponse](../../models/operations/getallapiendpointsresponse.md)**


## get_all_for_version_api_endpoints

Get all ApiEndpoints for a particular apiID and versionID.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetAllForVersionAPIEndpointsRequest(
    api_id='ipsa',
    version_id='delectus',
)

res = s.api_endpoints.get_all_for_version_api_endpoints(req)

if res.api_endpoints is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetAllForVersionAPIEndpointsRequest](../../models/operations/getallforversionapiendpointsrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetAllForVersionAPIEndpointsResponse](../../models/operations/getallforversionapiendpointsresponse.md)**


## get_api_endpoint

Get an ApiEndpoint.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetAPIEndpointRequest(
    api_endpoint_id='tempora',
    api_id='suscipit',
    version_id='molestiae',
)

res = s.api_endpoints.get_api_endpoint(req)

if res.api_endpoint is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetAPIEndpointRequest](../../models/operations/getapiendpointrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetAPIEndpointResponse](../../models/operations/getapiendpointresponse.md)**


## upsert_api_endpoint

Upsert an ApiEndpoint. If the ApiEndpoint does not exist it will be created, otherwise it will be updated.

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.UpsertAPIEndpointRequest(
    api_endpoint_input=shared.APIEndpointInput(
        api_endpoint_id='minus',
        description='placeat',
        display_name='voluptatum',
        method='iusto',
        path='excepturi',
        version_id='nisi',
    ),
    api_endpoint_id='recusandae',
    api_id='temporibus',
    version_id='ab',
)

res = s.api_endpoints.upsert_api_endpoint(req)

if res.api_endpoint is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.UpsertAPIEndpointRequest](../../models/operations/upsertapiendpointrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.UpsertAPIEndpointResponse](../../models/operations/upsertapiendpointresponse.md)**

