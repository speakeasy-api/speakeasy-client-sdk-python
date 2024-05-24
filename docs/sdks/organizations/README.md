# Organizations
(*organizations*)

### Available Operations

* [create_free_trial](#create_free_trial) - Create a free trial for an organization
* [get_organization_usage](#get_organization_usage) - Get billing usage summary for a particular organization
* [get_organizations](#get_organizations) - Get organizations for a user

## create_free_trial

Creates a free trial for an organization

### Example Usage

```python
import speakeasy
from speakeasy.models import shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)


res = s.organizations.create_free_trial()

if res is not None:
    # handle response
    pass

```


### Response

**[operations.CreateFreeTrialResponse](../../models/operations/createfreetrialresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_organization_usage

Returns a billing usage summary by target languages for a particular organization

### Example Usage

```python
import speakeasy
from speakeasy.models import shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)


res = s.organizations.get_organization_usage()

if res.organization_usage_response is not None:
    # handle response
    pass

```


### Response

**[operations.GetOrganizationUsageResponse](../../models/operations/getorganizationusageresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_organizations

Returns a list of organizations a user has access too

### Example Usage

```python
import speakeasy
from speakeasy.models import shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)


res = s.organizations.get_organizations()

if res.organizations is not None:
    # handle response
    pass

```


### Response

**[operations.GetOrganizationsResponse](../../models/operations/getorganizationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
