# PreflightResponse


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `content_type`                                                           | *str*                                                                    | :heavy_check_mark:                                                       | HTTP response content type for this operation                            |
| `status_code`                                                            | *int*                                                                    | :heavy_check_mark:                                                       | HTTP response status code for this operation                             |
| `raw_response`                                                           | [httpx.Response](https://www.python-httpx.org/api/#response)             | :heavy_check_mark:                                                       | Raw HTTP response; suitable for custom response parsing                  |
| `preflight_token`                                                        | [Optional[shared.PreflightToken]](../../models/shared/preflighttoken.md) | :heavy_minus_sign:                                                       | OK                                                                       |