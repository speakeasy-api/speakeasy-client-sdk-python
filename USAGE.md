<!-- Start SDK Example Usage -->
```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.GetApisRequest(
    metadata={
        "key": [
            'string',
        ],
    },
    op=operations.QueryParamOp(
        and_=False,
    ),
)

res = s.apis.get_apis(req)

if res.classes is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->