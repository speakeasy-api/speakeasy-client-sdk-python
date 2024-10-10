<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)

res = s.apis.get_apis(request={})

if res.apis is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

async def main():
    s = Speakeasy(
        security=shared.Security(
            api_key="<YOUR_API_KEY_HERE>",
        ),
    )
    res = await s.apis.get_apis_async(request={})
    if res.apis is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->