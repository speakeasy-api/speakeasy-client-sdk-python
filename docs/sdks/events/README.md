# Events
(*events*)

## Overview

REST APIs for capturing event data

### Available Operations

* [post_workspace_events](#post_workspace_events) - Post events for a specific workspace

## post_workspace_events

Sends an array of events to be stored for a particular workspace.

### Example Usage

```python
import dateutil.parser
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
    workspace_id='string',
)

req = operations.PostWorkspaceEventsRequest(
    request_body=[
        shared.CliEvent(
            created_at=dateutil.parser.isoparse('2024-11-21T06:58:42.120Z'),
            execution_id='string',
            id='<ID>',
            interaction_type=shared.InteractionType.CLI_EXEC,
            local_started_at=dateutil.parser.isoparse('2024-05-07T12:35:47.182Z'),
            speakeasy_api_key_name='string',
            speakeasy_version='string',
            success=False,
            workspace_id='string',
        ),
    ],
)

res = s.events.post_workspace_events(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.PostWorkspaceEventsRequest](../../models/operations/postworkspaceeventsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |


### Response

**[operations.PostWorkspaceEventsResponse](../../models/operations/postworkspaceeventsresponse.md)**
### Errors

| Error Object     | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4x-5xx           | */*              |
