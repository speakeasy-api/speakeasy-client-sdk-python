# upsert_api_endpoint
Available in: `api_endpoints`

Upsert an ApiEndpoint. If the ApiEndpoint does not exist it will be created, otherwise it will be updated.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpsertAPIEndpointRequest(
    api_endpoint_input=shared.APIEndpointInput(
        api_endpoint_id="repellendus",
        description="sapiente",
        display_name="quo",
        method="odit",
        path="at",
        version_id="at",
    ),
    api_endpoint_id="maiores",
    api_id="molestiae",
    version_id="quod",
)

res = s.api_endpoints.upsert_api_endpoint(req)

if res.api_endpoint is not None:
    # handle response
```