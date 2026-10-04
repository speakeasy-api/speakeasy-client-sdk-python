# PublishingTokens

## Overview

### Available Operations

* [create](#create) - Create a publishing token for a workspace
* [delete](#delete) - Delete a specific publishing token
* [get](#get) - Get a specific publishing token
* [list](#list) - Get publishing tokens for a workspace
* [resolve_metadata](#resolve_metadata) - Get metadata about the token
* [resolve_target](#resolve_target) - Get a specific publishing token target
* [update](#update) - Updates the validitity period of a publishing token

## create

Creates a publishing token for the current workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="createPublishingToken" method="post" path="/v1/publishing-tokens" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.publishing_tokens.create()

    assert res.publishing_token is not None

    # Handle response
    print(res.publishing_token)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.CreatePublishingTokenRequestBody](../../models/operations/createpublishingtokenrequestbody.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.CreatePublishingTokenResponse](../../models/operations/createpublishingtokenresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## delete

Delete a particular publishing token.

### Example Usage

<!-- UsageSnippet language="python" operationID="deletePublishingToken" method="delete" path="/v1/publishing-tokens/{tokenID}" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.publishing_tokens.delete(request={
        "token_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.DeletePublishingTokenRequest](../../models/operations/deletepublishingtokenrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.DeletePublishingTokenResponse](../../models/operations/deletepublishingtokenresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## get

Get information about a particular publishing token.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPublishingTokenByID" method="get" path="/v1/publishing-tokens/{tokenID}" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.publishing_tokens.get(request={
        "token_id": "<id>",
    })

    assert res.publishing_token is not None

    # Handle response
    print(res.publishing_token)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetPublishingTokenByIDRequest](../../models/operations/getpublishingtokenbyidrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GetPublishingTokenByIDResponse](../../models/operations/getpublishingtokenbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## list

Returns a publishing token for the current workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="getPublishingToken" method="get" path="/v1/publishing-tokens" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.publishing_tokens.list()

    assert res.classes is not None

    # Handle response
    print(res.classes)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetPublishingTokenResponse](../../models/operations/getpublishingtokenresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## resolve_metadata

Get information about a particular publishing token.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPublishingTokenPublicMetadata" method="get" path="/v1/publishing-tokens/{tokenID}/metadata" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.publishing_tokens.resolve_metadata(request={
        "token_id": "<id>",
    })

    assert res.object is not None

    # Handle response
    print(res.object)

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetPublishingTokenPublicMetadataRequest](../../models/operations/getpublishingtokenpublicmetadatarequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |
| `retries`                                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                         | :heavy_minus_sign:                                                                                                       | Configuration to override the default retry behavior of the client.                                                      |

### Response

**[operations.GetPublishingTokenPublicMetadataResponse](../../models/operations/getpublishingtokenpublicmetadataresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## resolve_target

Get information about a particular publishing token target.

### Example Usage

<!-- UsageSnippet language="python" operationID="getPublishingTokenTargetByID" method="get" path="/v1/publishing-tokens/{tokenID}/target" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.publishing_tokens.resolve_target(request={
        "token_id": "<id>",
    })

    assert res.res is not None

    # Handle response
    print(res.res)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetPublishingTokenTargetByIDRequest](../../models/operations/getpublishingtokentargetbyidrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.GetPublishingTokenTargetByIDResponse](../../models/operations/getpublishingtokentargetbyidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## update

Updates the validity period of a particular publishing token.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePublishingTokenExpiration" method="put" path="/v1/publishing-tokens/{tokenID}" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.publishing_tokens.update(request={
        "token_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.UpdatePublishingTokenExpirationRequest](../../models/operations/updatepublishingtokenexpirationrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |
| `retries`                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                       | :heavy_minus_sign:                                                                                                     | Configuration to override the default retry behavior of the client.                                                    |

### Response

**[operations.UpdatePublishingTokenExpirationResponse](../../models/operations/updatepublishingtokenexpirationresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |