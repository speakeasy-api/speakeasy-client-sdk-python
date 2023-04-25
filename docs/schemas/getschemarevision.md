# get_schema_revision
Available in: `schemas`

Returns information about the last uploaded schema for a particular schema revision. 
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


req = operations.GetSchemaRevisionRequest(
    api_id="harum",
    revision_id="enim",
    version_id="accusamus",
)

res = s.schemas.get_schema_revision(req)

if res.schema is not None:
    # handle response
```