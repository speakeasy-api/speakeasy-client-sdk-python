# Workspaces
(*workspaces*)

## Overview

REST APIs for managing Workspaces (speakeasy tenancy)

### Available Operations

* [create](#create) - Create a workspace
* [create_token](#create_token) - Create a token for a particular workspace
* [delete_token](#delete_token) - Delete a token for a particular workspace
* [get](#get) - Get workspace by context
* [get_all](#get_all) - Get workspaces for a user
* [get_by_id](#get_by_id) - Get workspace
* [get_feature_flags](#get_feature_flags) - Get workspace feature flags
* [get_settings](#get_settings) - Get workspace settings
* [get_team](#get_team) - Get team members for a particular workspace
* [get_tokens](#get_tokens) - Get tokens for a particular workspace
* [grant_access](#grant_access) - Grant a user access to a particular workspace
* [revoke_access](#revoke_access) - Revoke a user's access to a particular workspace
* [set_feature_flags](#set_feature_flags) - Set workspace feature flags
* [update](#update) - Update workspace details
* [update_settings](#update_settings) - Update workspace settings

## create

Creates a workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="createWorkspace" method="post" path="/v1/workspace" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared
from speakeasy_client_sdk_python.utils import parse_datetime


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.workspaces.create(request={
        "created_at": parse_datetime("2023-11-18T13:41:10.525Z"),
        "id": "<id>",
        "name": "<value>",
        "organization_id": "<id>",
        "slug": "<value>",
        "updated_at": parse_datetime("2024-11-21T08:36:32.740Z"),
        "verified": True,
    })

    assert res.workspace is not None

    # Handle response
    print(res.workspace)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [shared.Workspace](../../models/shared/workspace.md)                | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.CreateWorkspaceResponse](../../models/operations/createworkspaceresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## create_token

Create a token for a particular workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="createWorkspaceToken" method="post" path="/v1/workspace/{workspace_id}/tokens" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared
from speakeasy_client_sdk_python.utils import parse_datetime


with Speakeasy(
    workspace_id="<id>",
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.workspaces.create_token(request={
        "workspace_token": {
            "alg": "<value>",
            "created_at": parse_datetime("2024-10-04T10:23:04.522Z"),
            "id": "<id>",
            "key": "<key>",
            "name": "<value>",
            "workspace_id": "<id>",
        },
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateWorkspaceTokenRequest](../../models/operations/createworkspacetokenrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.CreateWorkspaceTokenResponse](../../models/operations/createworkspacetokenresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## delete_token

Delete a token for a particular workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteWorkspaceToken" method="delete" path="/v1/workspace/{workspace_id}/tokens/{tokenID}" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    workspace_id="<id>",
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.workspaces.delete_token(request={
        "token_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.DeleteWorkspaceTokenRequest](../../models/operations/deleteworkspacetokenrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.DeleteWorkspaceTokenResponse](../../models/operations/deleteworkspacetokenresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## get

Get information about a particular workspace by context.

### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspaceByContext" method="get" path="/v1/workspace" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.workspaces.get()

    assert res.workspace_and_organization is not None

    # Handle response
    print(res.workspace_and_organization)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetWorkspaceByContextResponse](../../models/operations/getworkspacebycontextresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## get_all

Returns a list of workspaces a user has access too

### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspaces" method="get" path="/v1/workspaces" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.workspaces.get_all()

    assert res.workspaces is not None

    # Handle response
    print(res.workspaces)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.GetWorkspacesResponse](../../models/operations/getworkspacesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## get_by_id

Get information about a particular workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspace" method="get" path="/v1/workspace/{workspace_id}" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    workspace_id="<id>",
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.workspaces.get_by_id(request={})

    assert res.workspace is not None

    # Handle response
    print(res.workspace)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetWorkspaceRequest](../../models/operations/getworkspacerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[operations.GetWorkspaceResponse](../../models/operations/getworkspaceresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## get_feature_flags

Get workspace feature flags

### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspaceFeatureFlags" method="get" path="/v1/workspace/{workspace_id}/feature_flags" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    workspace_id="<id>",
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.workspaces.get_feature_flags(request={})

    assert res.workspace_feature_flag_response is not None

    # Handle response
    print(res.workspace_feature_flag_response)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GetWorkspaceFeatureFlagsRequest](../../models/operations/getworkspacefeatureflagsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.GetWorkspaceFeatureFlagsResponse](../../models/operations/getworkspacefeatureflagsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4XX              | \*/\*            |

## get_settings

Get settings about a particular workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspaceSettings" method="get" path="/v1/workspace/{workspace_id}/settings" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    workspace_id="<id>",
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.workspaces.get_settings(request={})

    assert res.workspace_settings is not None

    # Handle response
    print(res.workspace_settings)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetWorkspaceSettingsRequest](../../models/operations/getworkspacesettingsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[operations.GetWorkspaceSettingsResponse](../../models/operations/getworkspacesettingsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## get_team

Get team members for a particular workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspaceTeam" method="get" path="/v1/workspace/{workspace_id}/team" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    workspace_id="<id>",
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.workspaces.get_team(request={})

    assert res.workspace_team_response is not None

    # Handle response
    print(res.workspace_team_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetWorkspaceTeamRequest](../../models/operations/getworkspaceteamrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.GetWorkspaceTeamResponse](../../models/operations/getworkspaceteamresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## get_tokens

Get tokens for a particular workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="getWorkspaceTokens" method="get" path="/v1/workspace/{workspace_id}/tokens" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    workspace_id="<id>",
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.workspaces.get_tokens(request={})

    assert res.classes is not None

    # Handle response
    print(res.classes)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetWorkspaceTokensRequest](../../models/operations/getworkspacetokensrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[operations.GetWorkspaceTokensResponse](../../models/operations/getworkspacetokensresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## grant_access

Grant a user access to a particular workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="grantUserAccessToWorkspace" method="put" path="/v1/workspace/{workspace_id}/team/email/{email}" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    workspace_id="<id>",
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.workspaces.grant_access(request={
        "email": "Idella24@gmail.com",
    })

    assert res.workspace_invite_response is not None

    # Handle response
    print(res.workspace_invite_response)

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GrantUserAccessToWorkspaceRequest](../../models/operations/grantuseraccesstoworkspacerequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |
| `retries`                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                             | :heavy_minus_sign:                                                                                           | Configuration to override the default retry behavior of the client.                                          |

### Response

**[operations.GrantUserAccessToWorkspaceResponse](../../models/operations/grantuseraccesstoworkspaceresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## revoke_access

Revoke a user's access to a particular workspace

### Example Usage

<!-- UsageSnippet language="python" operationID="revokeUserAccessToWorkspace" method="delete" path="/v1/workspace/{workspace_id}/team/{userId}" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    workspace_id="<id>",
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.workspaces.revoke_access(request={
        "user_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.RevokeUserAccessToWorkspaceRequest](../../models/operations/revokeuseraccesstoworkspacerequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[operations.RevokeUserAccessToWorkspaceResponse](../../models/operations/revokeuseraccesstoworkspaceresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## set_feature_flags

Set workspace feature flags

### Example Usage

<!-- UsageSnippet language="python" operationID="setWorkspaceFeatureFlags" method="post" path="/v1/workspace/feature_flags" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared


with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.workspaces.set_feature_flags(request={
        "feature_flags": [],
    })

    assert res.workspace_feature_flag_response is not None

    # Handle response
    print(res.workspace_feature_flag_response)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.WorkspaceFeatureFlagRequest](../../models/shared/workspacefeatureflagrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.SetWorkspaceFeatureFlagsResponse](../../models/operations/setworkspacefeatureflagsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 5XX              | application/json |
| errors.SDKError  | 4XX              | \*/\*            |

## update

Update information about a particular workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateWorkspaceDetails" method="post" path="/v1/workspace/{workspace_id}/details" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared
from speakeasy_client_sdk_python.utils import parse_datetime


with Speakeasy(
    workspace_id="<id>",
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.workspaces.update(request={
        "workspace": {
            "created_at": parse_datetime("2023-08-02T22:30:24.264Z"),
            "id": "<id>",
            "name": "<value>",
            "organization_id": "<id>",
            "slug": "<value>",
            "updated_at": parse_datetime("2025-01-24T03:53:13.581Z"),
            "verified": True,
        },
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateWorkspaceDetailsRequest](../../models/operations/updateworkspacedetailsrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.UpdateWorkspaceDetailsResponse](../../models/operations/updateworkspacedetailsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## update_settings

Update settings about a particular workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateWorkspaceSettings" method="put" path="/v1/workspace/{workspace_id}/settings" -->
```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared
from speakeasy_client_sdk_python.utils import parse_datetime


with Speakeasy(
    workspace_id="<id>",
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.workspaces.update_settings(request={
        "workspace_settings": {
            "created_at": parse_datetime("2025-03-09T15:48:09.330Z"),
            "updated_at": parse_datetime("2025-11-24T16:37:53.492Z"),
            "webhook_url": "https://wobbly-lid.org",
            "workspace_id": "<id>",
        },
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdateWorkspaceSettingsRequest](../../models/operations/updateworkspacesettingsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdateWorkspaceSettingsResponse](../../models/operations/updateworkspacesettingsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |