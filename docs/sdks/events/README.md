# Events
(*events*)

## Overview

REST APIs for managing events captured by a speakeasy binary (CLI, GitHub Action etc)

### Available Operations

* [get_events_by_target](#get_events_by_target) - Load recent events for a particular workspace
* [get_targets](#get_targets) - Load targets for a particular workspace
* [get_targets_deprecated](#get_targets_deprecated) - Load targets for a particular workspace
* [post](#post) - Post events for a specific workspace
* [search](#search) - Search events for a particular workspace by any field

## get_events_by_target

Load recent events for a particular workspace

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.events.get_events_by_target(request={
        "target_id": "<id>",
        "workspace_id": "<id>",
    })

    assert res.cli_event_batch is not None

    # Handle response
    print(res.cli_event_batch)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetWorkspaceEventsByTargetRequest](../../models/operations/getworkspaceeventsbytargetrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.GetWorkspaceEventsByTargetResponse](../../models/operations/getworkspaceeventsbytargetresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4XX              | \*/\*            |

## get_targets

Load targets for a particular workspace

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.events.get_targets(request={})

    assert res.target_sdk_list is not None

    # Handle response
    print(res.target_sdk_list)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetWorkspaceTargetsRequest](../../models/operations/getworkspacetargetsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetWorkspaceTargetsResponse](../../models/operations/getworkspacetargetsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4XX              | \*/\*            |

## get_targets_deprecated

Load targets for a particular workspace

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.events.get_targets_deprecated(request={
        "workspace_id": "<id>",
    })

    assert res.target_sdk_list is not None

    # Handle response
    print(res.target_sdk_list)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetWorkspaceTargetsDeprecatedRequest](../../models/operations/getworkspacetargetsdeprecatedrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.GetWorkspaceTargetsDeprecatedResponse](../../models/operations/getworkspacetargetsdeprecatedresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4XX              | \*/\*            |

## post

Sends an array of events to be stored for a particular workspace.

### Example Usage

```python
import dateutil.parser
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.events.post(request={
        "request_body": [
            {
                "created_at": dateutil.parser.isoparse("2025-03-02T10:07:28.113Z"),
                "execution_id": "<id>",
                "id": "<id>",
                "interaction_type": shared.InteractionType.AUTHENTICATE,
                "local_started_at": dateutil.parser.isoparse("2025-08-12T17:54:17.538Z"),
                "speakeasy_api_key_name": "<value>",
                "speakeasy_version": "<value>",
                "success": True,
                "workspace_id": "<id>",
            },
        ],
        "workspace_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PostWorkspaceEventsRequest](../../models/operations/postworkspaceeventsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.PostWorkspaceEventsResponse](../../models/operations/postworkspaceeventsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4XX              | \*/\*            |

## search

Search events for a particular workspace by any field

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.events.search(request={
        "workspace_id": "<id>",
    })

    assert res.cli_event_batch is not None

    # Handle response
    print(res.cli_event_batch)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.SearchWorkspaceEventsRequest](../../models/operations/searchworkspaceeventsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.SearchWorkspaceEventsResponse](../../models/operations/searchworkspaceeventsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4XX              | \*/\*            |