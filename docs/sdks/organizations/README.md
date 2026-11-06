# Organizations

## Overview

REST APIs for managing Organizations (speakeasy L1 Tenancy construct)

### Available Operations

* [create](#create) - Create an organization
* [create_billing_add_ons](#create_billing_add_ons) - Create billing add ons
* [create_free_trial](#create_free_trial) - Create a free trial for an organization
* [delete_billing_add_on](#delete_billing_add_on) - Delete billing add ons
* [get](#get) - Get organization
* [get_all](#get_all) - Get organizations for a user
* [get_billing_add_ons](#get_billing_add_ons) - Get billing add ons
* [get_usage](#get_usage) - Get billing usage summary for a particular organization

## create

Creates an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="createOrganization" method="post" path="/v1/organization" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared
from speakeasy_client_sdk_python.utils import parse_datetime


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.organizations.create(request={
        "account_type": shared.AccountType.SCALE_UP,
        "created_at": parse_datetime("2026-10-26T09:05:00.560Z"),
        "id": "<id>",
        "name": "<value>",
        "slug": "<value>",
        "sso_activated": False,
        "telemetry_disabled": False,
        "updated_at": parse_datetime("2024-12-22T08:00:51.380Z"),
    })

    assert res.organization is not None

    # Handle response
    print(res.organization)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.Organization](../../models/shared/organization.md)          | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreateOrganizationResponse](../../models/operations/createorganizationresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## create_billing_add_ons

Create billing add ons

### Example Usage

<!-- UsageSnippet language="python" operationID="createBillingAddOns" method="post" path="/v1/organization/add_ons" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.organizations.create_billing_add_ons(request={
        "add_ons": [
            shared.BillingAddOn.CUSTOM_CODE_REGIONS,
        ],
    })

    assert res.organization_billing_add_on_response is not None

    # Handle response
    print(res.organization_billing_add_on_response)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [shared.OrganizationBillingAddOnRequest](../../models/shared/organizationbillingaddonrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateBillingAddOnsResponse](../../models/operations/createbillingaddonsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4XX              | \*/\*            |

## create_free_trial

Creates a free trial for an organization

### Example Usage

<!-- UsageSnippet language="python" operationID="createFreeTrial" method="post" path="/v1/organization/free_trial" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.organizations.create_free_trial()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreateFreeTrialResponse](../../models/operations/createfreetrialresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## delete_billing_add_on

Delete billing add ons

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteBillingAddOn" method="delete" path="/v1/organization/add_ons/{add_on}" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.organizations.delete_billing_add_on(request={
        "add_on": shared.BillingAddOn.SDK_TESTING,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.DeleteBillingAddOnRequest](../../models/operations/deletebillingaddonrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.DeleteBillingAddOnResponse](../../models/operations/deletebillingaddonresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4XX              | \*/\*            |

## get

Get information about a particular organization.

### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganization" method="get" path="/v1/organization/{organizationID}" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.organizations.get(request={
        "organization_id": "<id>",
    })

    assert res.organization is not None

    # Handle response
    print(res.organization)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetOrganizationRequest](../../models/operations/getorganizationrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetOrganizationResponse](../../models/operations/getorganizationresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## get_all

Returns a list of organizations a user has access too

### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganizations" method="get" path="/v1/organizations" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.organizations.get_all()

    assert res.organizations is not None

    # Handle response
    print(res.organizations)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetOrganizationsResponse](../../models/operations/getorganizationsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## get_billing_add_ons

Get billing add ons

### Example Usage

<!-- UsageSnippet language="python" operationID="getBillingAddOns" method="get" path="/v1/organization/add_ons" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.organizations.get_billing_add_ons()

    assert res.organization_billing_add_on_response is not None

    # Handle response
    print(res.organization_billing_add_on_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetBillingAddOnsResponse](../../models/operations/getbillingaddonsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4XX              | \*/\*            |

## get_usage

Returns a billing usage summary by target languages for a particular organization

### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganizationUsage" method="get" path="/v1/organization/usage" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.organizations.get_usage()

    assert res.organization_usage_response is not None

    # Handle response
    print(res.organization_usage_response)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetOrganizationUsageResponse](../../models/operations/getorganizationusageresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |