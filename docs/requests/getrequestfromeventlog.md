# get_request_from_event_log
Available in: `requests`

Get information about a particular request.

## Example Usage
```python
import speakeasy
from speakeasy.models import operations

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.GetRequestFromEventLogRequest(
    request_id="sequi",
)

res = s.requests.get_request_from_event_log(req)

if res.unbounded_request is not None:
    # handle response
```