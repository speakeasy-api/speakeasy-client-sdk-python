# get_schemas
Available in: `schemas`

Returns information the schemas associated with a particular apiID. 
This won't include the schemas themselves, they can be retrieved via the downloadSchema operation.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSchemasRequest(
    api_id="commodi",
    version_id="repudiandae",
)

res = s.schemas.get_schemas(req)

if res.schemata is not None:
    # handle response
```