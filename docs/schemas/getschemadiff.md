# get_schema_diff
Available in: `schemas`

Get a diff of two schema revisions for an Api.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetSchemaDiffRequest(
    api_id="corporis",
    base_revision_id="dolore",
    target_revision_id="iusto",
    version_id="dicta",
)

res = s.schemas.get_schema_diff(req)

if res.schema_diff is not None:
    # handle response
```