# generate_open_api_spec
Available in: `apis`

This endpoint will generate any missing operations in any registered OpenAPI document if the operation does not already exist in the document.
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


req = operations.GenerateOpenAPISpecRequest(
    api_id="totam",
    version_id="porro",
)

res = s.apis.generate_open_api_spec(req)

if res.generate_open_api_spec_diff is not None:
    # handle response
```