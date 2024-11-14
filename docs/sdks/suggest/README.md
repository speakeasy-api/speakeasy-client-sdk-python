# Suggest
(*suggest*)

## Overview

REST APIs for managing LLM OAS suggestions

### Available Operations

* [suggest](#suggest) - Generate suggestions for improving an OpenAPI document.
* [suggest_items](#suggest_items) - Generate generic suggestions for a list of items.
* [suggest_open_api](#suggest_open_api) - (DEPRECATED) Generate suggestions for improving an OpenAPI document.
* [suggest_open_api_registry](#suggest_open_api_registry) - Generate suggestions for improving an OpenAPI document stored in the registry.

## suggest

Get suggestions from an LLM model for improving an OpenAPI document.

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)

res = s.suggest.suggest(request={
    "x_session_id": "<id>",
    "suggest_request_body": {
        "diagnostics": [
            {
                "message": "<value>",
                "path": [
                    "/opt/include",
                    "/opt/share",
                ],
                "type": "<value>",
            },
            {
                "message": "<value>",
                "path": [
                    "/rescue",
                ],
                "type": "<value>",
            },
        ],
        "oas_summary": {
            "info": {
                "description": "amid traffic the unfortunately underneath what father lovely out",
                "license": {},
                "summary": "<value>",
                "title": "<value>",
                "version": "<value>",
            },
            "operations": [
                {
                    "description": "times dull than except",
                    "method": "<value>",
                    "operation_id": "<id>",
                    "path": "/mnt",
                    "tags": [
                        "<value>",
                        "<value>",
                    ],
                },
            ],
        },
        "suggestion_type": shared.SuggestRequestBodySuggestionType.DIAGNOSTICS_ONLY,
    },
})

if res.schema_ is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.SuggestRequest](../../models/operations/suggestrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[operations.SuggestResponse](../../models/operations/suggestresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## suggest_items

Generate generic suggestions for a list of items.

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)

res = s.suggest.suggest_items(request={
    "items": [
        "<value>",
    ],
    "prompt": "<value>",
})

if res.strings is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.SuggestItemsRequestBody](../../models/shared/suggestitemsrequestbody.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.SuggestItemsResponse](../../models/operations/suggestitemsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## suggest_open_api

Get suggestions from an LLM model for improving an OpenAPI document.

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)

res = s.suggest.suggest_open_api(request={
    "x_session_id": "<id>",
    "request_body": {
        "schema_": {
            "content": open("example.file", "rb"),
            "file_name": "example.file",
        },
    },
})

if res.schema_ is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.SuggestOpenAPIRequest](../../models/operations/suggestopenapirequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.SuggestOpenAPIResponse](../../models/operations/suggestopenapiresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## suggest_open_api_registry

Get suggestions from an LLM model for improving an OpenAPI document stored in the registry.

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)

res = s.suggest.suggest_open_api_registry(request={
    "x_session_id": "<id>",
    "namespace_name": "<value>",
    "revision_reference": "<value>",
})

if res.schema_ is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.SuggestOpenAPIRegistryRequest](../../models/operations/suggestopenapiregistryrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.SuggestOpenAPIRegistryResponse](../../models/operations/suggestopenapiregistryresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |