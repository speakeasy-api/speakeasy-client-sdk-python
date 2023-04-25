# generate_postman_collection_for_api_endpoint
Available in: `api_endpoints`

Generates a postman collection that allows the endpoint to be called from postman variables produced for any path/query/header parameters included in the OpenAPI document.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GeneratePostmanCollectionForAPIEndpointRequest(
    api_endpoint_id="nisi",
    api_id="recusandae",
    version_id="temporibus",
)

res = s.api_endpoints.generate_postman_collection_for_api_endpoint(req)

if res.postman_collection is not None:
    # handle response
```