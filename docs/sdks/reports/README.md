# Reports
(*reports*)

## Overview

REST APIs for managing reports

### Available Operations

* [get_changes_report_signed_url](#get_changes_report_signed_url) - Get the signed access url for the change reports for a particular document.
* [get_linting_report_signed_url](#get_linting_report_signed_url) - Get the signed access url for the linting reports for a particular document.
* [upload_report](#upload_report) - Upload a report.

## get_changes_report_signed_url

Get the signed access url for the change reports for a particular document.

### Example Usage

```python
import os
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.reports.get_changes_report_signed_url(request={
    "document_checksum": "<value>",
})

if res.signed_access is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetChangesReportSignedURLRequest](../../models/operations/getchangesreportsignedurlrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetChangesReportSignedURLResponse](../../models/operations/getchangesreportsignedurlresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_linting_report_signed_url

Get the signed access url for the linting reports for a particular document.

### Example Usage

```python
import os
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.reports.get_linting_report_signed_url(request={
    "document_checksum": "<value>",
})

if res.signed_access is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetLintingReportSignedURLRequest](../../models/operations/getlintingreportsignedurlrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.GetLintingReportSignedURLResponse](../../models/operations/getlintingreportsignedurlresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## upload_report

Upload a report.

### Example Usage

```python
import os
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

s = Speakeasy(
    security=shared.Security(
        api_key=os.getenv("API_KEY", ""),
    ),
)


res = s.reports.upload_report(request={
    "data": {},
    "file": {
        "content": open("<file_path>", "rb"),
        "file_name": "your_file_here",
    },
})

if res.uploaded_report is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UploadReportRequestBody](../../models/operations/uploadreportrequestbody.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.UploadReportResponse](../../models/operations/uploadreportresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
