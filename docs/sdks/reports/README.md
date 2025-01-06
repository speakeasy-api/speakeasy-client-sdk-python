# Reports
(*reports*)

## Overview

REST APIs for managing reports (lint reports, change reports, etc)

### Available Operations

* [get_changes_report_signed_url](#get_changes_report_signed_url) - Get the signed access url for the change reports for a particular document.
* [get_linting_report_signed_url](#get_linting_report_signed_url) - Get the signed access url for the linting reports for a particular document.
* [upload_report](#upload_report) - Upload a report.

## get_changes_report_signed_url

Get the signed access url for the change reports for a particular document.

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.reports.get_changes_report_signed_url(request={
        "document_checksum": "<value>",
    })

    assert res.signed_access is not None

    # Handle response
    print(res.signed_access)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetChangesReportSignedURLRequest](../../models/operations/getchangesreportsignedurlrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.GetChangesReportSignedURLResponse](../../models/operations/getchangesreportsignedurlresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_linting_report_signed_url

Get the signed access url for the linting reports for a particular document.

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.reports.get_linting_report_signed_url(request={
        "document_checksum": "<value>",
    })

    assert res.signed_access is not None

    # Handle response
    print(res.signed_access)

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.GetLintingReportSignedURLRequest](../../models/operations/getlintingreportsignedurlrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

### Response

**[operations.GetLintingReportSignedURLResponse](../../models/operations/getlintingreportsignedurlresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## upload_report

Upload a report.

### Example Usage

```python
from speakeasy_client_sdk_python import Speakeasy
from speakeasy_client_sdk_python.models import shared

with Speakeasy(
    security=shared.Security(
        api_key="<YOUR_API_KEY_HERE>",
    ),
) as speakeasy:

    res = speakeasy.reports.upload_report(request={
        "data": {},
        "file": {
            "content": open("example.file", "rb"),
            "file_name": "example.file",
        },
    })

    assert res.uploaded_report is not None

    # Handle response
    print(res.uploaded_report)

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UploadReportRequestBody](../../models/operations/uploadreportrequestbody.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |
| `retries`                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                         | :heavy_minus_sign:                                                                       | Configuration to override the default retry behavior of the client.                      |

### Response

**[operations.UploadReportResponse](../../models/operations/uploadreportresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |