# Github
(*github*)

## Overview

REST APIs for managing the github integration

### Available Operations

* [check_access](#check_access)
* [check_publishing_p_rs](#check_publishing_p_rs)
* [check_publishing_secrets](#check_publishing_secrets)
* [configure_code_samples](#configure_code_samples)
* [configure_mintlify_repo](#configure_mintlify_repo)
* [configure_target](#configure_target)
* [get_action](#get_action)
* [get_setup](#get_setup)
* [link_github](#link_github)
* [store_publishing_secrets](#store_publishing_secrets)
* [trigger_action](#trigger_action)

## check_access

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.github.check_access(request={
        "org": "<value>",
        "repo": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CheckGithubAccessRequest](../../models/operations/checkgithubaccessrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CheckGithubAccessResponse](../../models/operations/checkgithubaccessresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## check_publishing_p_rs

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.github.check_publishing_p_rs(request={
        "generate_gen_lock_id": "<id>",
        "org": "<value>",
        "repo": "<value>",
    })

    assert res.github_publishing_pr_response is not None

    # Handle response
    print(res.github_publishing_pr_response)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.GithubCheckPublishingPRsRequest](../../models/operations/githubcheckpublishingprsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.GithubCheckPublishingPRsResponse](../../models/operations/githubcheckpublishingprsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## check_publishing_secrets

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.github.check_publishing_secrets(request={
        "generate_gen_lock_id": "<id>",
    })

    assert res.github_missing_publishing_secrets_response is not None

    # Handle response
    print(res.github_missing_publishing_secrets_response)

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GithubCheckPublishingSecretsRequest](../../models/operations/githubcheckpublishingsecretsrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |
| `retries`                                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                 | :heavy_minus_sign:                                                                                               | Configuration to override the default retry behavior of the client.                                              |

### Response

**[operations.GithubCheckPublishingSecretsResponse](../../models/operations/githubcheckpublishingsecretsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## configure_code_samples

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.github.configure_code_samples(request={
        "org": "<value>",
        "repo": "<value>",
        "target_name": "<value>",
    })

    assert res.github_configure_code_samples_response is not None

    # Handle response
    print(res.github_configure_code_samples_response)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [shared.GithubConfigureCodeSamplesRequest](../../models/shared/githubconfigurecodesamplesrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.GithubConfigureCodeSamplesResponse](../../models/operations/githubconfigurecodesamplesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## configure_mintlify_repo

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.github.configure_mintlify_repo(request={
        "input": "<value>",
        "org": "<value>",
        "overlays": [
            "<value>",
        ],
        "repo": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [shared.GithubConfigureMintlifyRepoRequest](../../models/shared/githubconfiguremintlifyreporequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.GithubConfigureMintlifyRepoResponse](../../models/operations/githubconfiguremintlifyreporesponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## configure_target

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.github.configure_target(request={
        "org": "<value>",
        "repo_name": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.GithubConfigureTargetRequest](../../models/shared/githubconfiguretargetrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.GithubConfigureTargetResponse](../../models/operations/githubconfiguretargetresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## get_action

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.github.get_action(request={
        "org": "<value>",
        "repo": "<value>",
    })

    assert res.github_get_action_response is not None

    # Handle response
    print(res.github_get_action_response)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetGitHubActionRequest](../../models/operations/getgithubactionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GetGitHubActionResponse](../../models/operations/getgithubactionresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## get_setup

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.github.get_setup(request={
        "org": "<value>",
        "repo": "<value>",
        "generate_gen_lock_id": "<id>",
    })

    assert res.github_setup_state_response is not None

    # Handle response
    print(res.github_setup_state_response)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetGithubSetupStateRequest](../../models/operations/getgithubsetupstaterequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[operations.GetGithubSetupStateResponse](../../models/operations/getgithubsetupstateresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## link_github

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.github.link_github(request={})

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.LinkGithubAccessRequest](../../models/operations/linkgithubaccessrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.LinkGithubAccessResponse](../../models/operations/linkgithubaccessresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## store_publishing_secrets

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.github.store_publishing_secrets(request={
        "generate_gen_lock_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [shared.GithubStorePublishingSecretsRequest](../../models/shared/githubstorepublishingsecretsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.GithubStorePublishingSecretsResponse](../../models/operations/githubstorepublishingsecretsresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |

## trigger_action

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.github.trigger_action(request={
        "gen_lock_id": "<id>",
        "org": "<value>",
        "repo_name": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.GithubTriggerActionRequest](../../models/shared/githubtriggeractionrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |
| `retries`                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                       | :heavy_minus_sign:                                                                     | Configuration to override the default retry behavior of the client.                    |

### Response

**[operations.GithubTriggerActionResponse](../../models/operations/githubtriggeractionresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 4XX              | application/json |
| errors.SDKError  | 5XX              | \*/\*            |