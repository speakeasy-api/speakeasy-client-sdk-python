# find_api_endpoint
Available in: `api_endpoints`

Find an ApiEndpoint via its displayName (set by operationId from a registered OpenAPI schema).
This is useful for finding the ID of an ApiEndpoint to use in the /v1/apis/{apiID}/version/{versionID}/api_endpoints/{apiEndpointID} endpoints.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.FindAPIEndpointRequest(
    api_id="molestiae",
    display_name="minus",
    version_id="placeat",
)

res = s.api_endpoints.find_api_endpoint(req)

if res.api_endpoint is not None:
    # handle response
```