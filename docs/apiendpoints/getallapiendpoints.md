# get_all_api_endpoints
Available in: `api_endpoints`

Get all Api endpoints for a particular apiID.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAllAPIEndpointsRequest(
    api_id="ab",
)

res = s.api_endpoints.get_all_api_endpoints(req)

if res.api_endpoints is not None:
    # handle response
```