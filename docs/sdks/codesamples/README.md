# CodeSamples
(*code_samples*)

## Overview

REST APIs for retrieving Code Samples

### Available Operations

* [generate_code_sample_preview](#generate_code_sample_preview) - Generate Code Sample previews from a file and configuration parameters.
* [generate_code_sample_preview_asynchronous](#generate_code_sample_preview_asynchronous) - Initiate asynchronous Code Sample preview generation from a file and configuration parameters, receiving an async JobID response for polling.
* [get](#get) - Retrieve usage snippets from document stored in the registry
* [get_code_sample_preview_async](#get_code_sample_preview_async) - Poll for the result of an asynchronous Code Sample preview generation.

## generate_code_sample_preview

This endpoint generates Code Sample previews from a file and configuration parameters.

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.code_samples.generate_code_sample_preview(request={
        "languages": [
            "<value>",
            "<value>",
        ],
        "schema_file": {
            "content": open("example.file", "rb"),
            "file_name": "example.file",
        },
    })

    assert res.two_hundred_application_json_response_stream is not None

    # Handle response
    print(res.two_hundred_application_json_response_stream)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.CodeSampleSchemaInput](../../models/shared/codesampleschemainput.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.GenerateCodeSamplePreviewResponse](../../models/operations/generatecodesamplepreviewresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX, 5XX         | application/json |

## generate_code_sample_preview_asynchronous

This endpoint generates Code Sample previews from a file and configuration parameters, receiving an async JobID response for polling.

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.code_samples.generate_code_sample_preview_asynchronous(request={
        "languages": [
            "<value>",
            "<value>",
        ],
        "schema_file": {
            "content": open("example.file", "rb"),
            "file_name": "example.file",
        },
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.CodeSampleSchemaInput](../../models/shared/codesampleschemainput.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.GenerateCodeSamplePreviewAsyncResponse](../../models/operations/generatecodesamplepreviewasyncresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX, 5XX         | application/json |

## get

Retrieve usage snippets from document stored in the registry. Supports filtering by language and operation ID.

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.code_samples.get(request={
        "registry_url": "https://normal-making.name",
    })

    assert res.usage_snippets is not None

    # Handle response
    print(res.usage_snippets)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetCodeSamplesRequest](../../models/operations/getcodesamplesrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.GetCodeSamplesResponse](../../models/operations/getcodesamplesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## get_code_sample_preview_async

Poll for the result of an asynchronous Code Sample preview generation.

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.code_samples.get_code_sample_preview_async(request={
        "job_id": "<id>",
    })

    assert res.two_hundred_application_json_response_stream is not None

    # Handle response
    print(res.two_hundred_application_json_response_stream)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetCodeSamplePreviewAsyncRequest](../../models/operations/getcodesamplepreviewasyncrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.GetCodeSamplePreviewAsyncResponse](../../models/operations/getcodesamplepreviewasyncresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX, 5XX         | application/json |