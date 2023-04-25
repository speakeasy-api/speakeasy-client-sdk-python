# generate_postman_collection
Available in: `apis`

Generates a postman collection containing all endpoints for a particular API. Includes variables produced for any path/query/header parameters included in the OpenAPI document.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GeneratePostmanCollectionRequest(
    api_id="dolorum",
    version_id="dicta",
)

res = s.apis.generate_postman_collection(req)

if res.postman_collection is not None:
    # handle response
```