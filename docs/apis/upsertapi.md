# upsert_api
Available in: `apis`

Upsert an Api. If the Api does not exist, it will be created.
If the Api exists, it will be updated.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.UpsertAPIRequest(
    api_input=shared.APIInput(
        api_id="dolor",
        description="natus",
        meta_data={
            "hic": [
                "fuga",
                "in",
                "corporis",
                "iste",
            ],
            "iure": [
                "quidem",
                "architecto",
                "ipsa",
                "reiciendis",
            ],
        },
        version_id="est",
    ),
    api_id="mollitia",
)

res = s.apis.upsert_api(req)

if res.api is not None:
    # handle response
```