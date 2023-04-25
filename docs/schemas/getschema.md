# get_schema
Available in: `schemas`

Returns information about the last uploaded schema for a particular API version. 
This won't include the schema itself, that can be retrieved via the downloadSchema operation.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSchemaRequest(
    api_id="maiores",
    version_id="dicta",
)

res = s.schemas.get_schema(req)

if res.schema is not None:
    # handle response
```