# Suggest
(*suggest*)

## Overview

REST APIs for managing LLM OAS suggestions

### Available Operations

* [apply_operation_i_ds](#apply_operation_i_ds) - Apply operation ID suggestions and download result.
* [suggest_operation_i_ds](#suggest_operation_i_ds) - Generate operation ID suggestions.
* [suggest_operation_i_ds_registry](#suggest_operation_i_ds_registry) - Generate operation ID suggestions.

## apply_operation_i_ds

Apply operation ID suggestions and download result.

### Example Usage

```python
import os
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.suggest.apply_operation_i_ds(request={
    "x_session_id": "<value>",
})

if res.two_hundred_application_json_schema is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.ApplyOperationIDsRequest](../../models/operations/applyoperationidsrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.ApplyOperationIDsResponse](../../models/operations/applyoperationidsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## suggest_operation_i_ds

Get suggestions from an LLM model for improving the operationIDs in the provided schema.

### Example Usage

```python
import os
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.suggest.suggest_operation_i_ds(request={
    "request_body": {
        "schema": {
            "content": open("<file_path>", "rb"),
            "file_name": "your_file_here",
        },
    },
    "x_session_id": "<value>",
})

if res.suggested_operation_i_ds is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.SuggestOperationIDsRequest](../../models/operations/suggestoperationidsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.SuggestOperationIDsResponse](../../models/operations/suggestoperationidsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## suggest_operation_i_ds_registry

Get suggestions from an LLM model for improving the operationIDs in the provided schema.

### Example Usage

```python
import os
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.suggest.suggest_operation_i_ds_registry(request={
    "namespace_name": "<value>",
    "revision_reference": "<value>",
    "x_session_id": "<value>",
})

if res.suggested_operation_i_ds is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.SuggestOperationIDsRegistryRequest](../../models/operations/suggestoperationidsregistryrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.SuggestOperationIDsRegistryResponse](../../models/operations/suggestoperationidsregistryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
