# SchemaStore

## Overview

### Available Operations

* [create_schema_store_item](#create_schema_store_item) - Create a schema in the schema store
* [get_schema_store_item](#get_schema_store_item) - Get a OAS schema from the schema store

## create_schema_store_item

Create a schema in the schema store

### Example Usage

<!-- UsageSnippet language="python" operationID="createSchemaStoreItem" method="post" path="/v1/schema_store" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import operations, shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.schema_store.create_schema_store_item(request={
        "format_": operations.Format.YAML,
        "package_name": "<value>",
        "sdk_classname": "<value>",
        "spec": "<value>",
    })

    assert res.schema_store_item is not None

    # Handle response
    print(res.schema_store_item)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.CreateSchemaStoreItemRequestBody](../../models/operations/createschemastoreitemrequestbody.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.CreateSchemaStoreItemResponse](../../models/operations/createschemastoreitemresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## get_schema_store_item

Get a OAS schema from the schema store

### Example Usage

<!-- UsageSnippet language="python" operationID="getSchemaStoreItem" method="get" path="/v1/schema_store" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.schema_store.get_schema_store_item()

    assert res.schema_store_item is not None

    # Handle response
    print(res.schema_store_item)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetSchemaStoreItemRequestBody](../../models/operations/getschemastoreitemrequestbody.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GetSchemaStoreItemResponse](../../models/operations/getschemastoreitemresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |