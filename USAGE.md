<!-- Start SDK Example Usage -->
```python
import sdk
from sdk.models import operations, shared

s = sdk.SDK()
s.config_security(
    security=shared.Security(
        api_key=shared.SchemeAPIKey(
            api_key="YOUR_API_KEY_HERE",
        ),
    )
)
    
req = operations.GetApisRequest(
    query_params=operations.GetApisQueryParams(
        metadata={
            "voluptas": [
                "expedita",
                "consequuntur",
            ],
        },
        op=operations.GetApisOp(
            and_=False,
        ),
    ),
)
    
res = s.apis.get_apis(req)

if res.apis is not None:
    # handle response
```
<!-- End SDK Example Usage -->