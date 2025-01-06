# Subscriptions
(*subscriptions*)

## Overview

REST APIs for managing subscriptions

### Available Operations

* [activate_subscription_namespace](#activate_subscription_namespace) - Activate an ignored namespace for a subscription
* [ignore_subscription_namespace](#ignore_subscription_namespace) - Ignored a namespace for a subscription

## activate_subscription_namespace

Activate an ignored namespace for a subscription

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.subscriptions.activate_subscription_namespace(request={
        "subscription_id": "<id>",
        "namespace_name": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.ActivateSubscriptionNamespaceRequest](../../models/operations/activatesubscriptionnamespacerequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.ActivateSubscriptionNamespaceResponse](../../models/operations/activatesubscriptionnamespaceresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## ignore_subscription_namespace

Ignored a namespace for a subscription

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.subscriptions.ignore_subscription_namespace(request={
        "subscription_id": "<id>",
        "namespace_name": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.IgnoreSubscriptionNamespaceRequest](../../models/operations/ignoresubscriptionnamespacerequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.IgnoreSubscriptionNamespaceResponse](../../models/operations/ignoresubscriptionnamespaceresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |