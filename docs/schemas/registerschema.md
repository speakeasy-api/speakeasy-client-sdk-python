# register_schema
Available in: `schemas`

Allows uploading a schema for a particular API version.
This will be used to populate ApiEndpoints and used as a base for any schema generation if present.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.RegisterSchemaRequest(
    request_body=operations.RegisterSchemaRequestBody(
        file=operations.RegisterSchemaRequestBodyFile(
            content="quae".encode(),
            file="ipsum",
        ),
    ),
    api_id="quidem",
    version_id="molestias",
)

res = s.schemas.register_schema(req)

if res.status_code == 200:
    # handle response
```