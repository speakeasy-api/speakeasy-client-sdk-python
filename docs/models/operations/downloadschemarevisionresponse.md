# DownloadSchemaRevisionResponse


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `content_type`                                               | *str*                                                        | :heavy_check_mark:                                           | HTTP response content type for this operation                |
| `status_code`                                                | *int*                                                        | :heavy_check_mark:                                           | HTTP response status code for this operation                 |
| `raw_response`                                               | [httpx.Response](https://www.python-httpx.org/api/#response) | :heavy_check_mark:                                           | Raw HTTP response; suitable for custom response parsing      |
| `two_hundred_application_json_schema`                        | *Optional[httpx.Response]*                                   | :heavy_minus_sign:                                           | OK                                                           |
| `two_hundred_application_x_yaml_schema`                      | *Optional[httpx.Response]*                                   | :heavy_minus_sign:                                           | OK                                                           |
| `error`                                                      | *Optional[errors.Error]*                                     | :heavy_minus_sign:                                           | Default error response                                       |