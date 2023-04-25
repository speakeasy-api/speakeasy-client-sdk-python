# generate_open_api_spec_for_api_endpoint
Available in: `api_endpoints`

This endpoint will generate a new operation in any registered OpenAPI document if the operation does not already exist in the document.
Returns the original document and the newly generated document allowing a diff to be performed to see what has changed.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GenerateOpenAPISpecForAPIEndpointRequest(
    api_endpoint_id="voluptatum",
    api_id="iusto",
    version_id="excepturi",
)

res = s.api_endpoints.generate_open_api_spec_for_api_endpoint(req)

if res.generate_open_api_spec_diff is not None:
    # handle response
```