# get_api_endpoint
Available in: `api_endpoints`

Get an ApiEndpoint.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetAPIEndpointRequest(
    api_endpoint_id="deserunt",
    api_id="perferendis",
    version_id="ipsam",
)

res = s.api_endpoints.get_api_endpoint(req)

if res.api_endpoint is not None:
    # handle response
```