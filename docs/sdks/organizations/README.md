# Organizations
(*organizations*)

### Available Operations

* [get_organizations](#get_organizations) - Get organizations for a user

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
