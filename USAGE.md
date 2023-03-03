<!-- Start SDK Example Usage -->
```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy()
s.config_security(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    )
)
   
req = operations.GetApisRequest(
    query_params=operations.GetApisQueryParams(
        metadata={
            "deserunt": [
                "nulla",
                "id",
                "vero",
            ],
            "perspiciatis": [
                "nihil",
                "fuga",
                "facilis",
                "eum",
            ],
            "iusto": [
                "saepe",
                "inventore",
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