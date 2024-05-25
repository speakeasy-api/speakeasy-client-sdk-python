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
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)


res = s.reports.get_changes_report_signed_url(request=operations.GetChangesReportSignedURLRequest(
    document_checksum='<value>',
))

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
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)


res = s.reports.get_linting_report_signed_url(request=operations.GetLintingReportSignedURLRequest(
    document_checksum='<value>',
))

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
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
)


res = s.reports.upload_report(request=operations.UploadReportRequestBody(
    data=shared.Report(),
    file=operations.File(
        content='0xA329C0ad85'.encode(),
        file_name='your_file_here',
    ),
))

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
