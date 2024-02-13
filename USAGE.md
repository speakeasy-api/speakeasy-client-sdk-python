<!-- Start SDK Example Usage [usage] -->
```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
    workspace_id='string',
)

req = operations.GetApisRequest()

res = s.apis.get_apis(req)

if res.apis is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->