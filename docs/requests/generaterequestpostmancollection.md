# generate_request_postman_collection
Available in: `requests`

Generates a Postman collection for a particular request. 
Allowing it to be replayed with the same inputs that were captured by the SDK.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GenerateRequestPostmanCollectionRequest(
    request_id="quo",
)

res = s.requests.generate_request_postman_collection(req)

if res.postman_collection is not None:
    # handle response
```