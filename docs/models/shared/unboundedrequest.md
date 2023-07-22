# UnboundedRequest

An UnboundedRequest represents the HAR content capture by Speakeasy when logging a request.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Creation timestamp.                                                  |
| `har`                                                                | *str*                                                                | :heavy_check_mark:                                                   | The HAR content of the request.                                      |
| `har_size_bytes`                                                     | *int*                                                                | :heavy_check_mark:                                                   | The size of the HAR content in bytes.                                |
| `request_id`                                                         | *str*                                                                | :heavy_check_mark:                                                   | The ID of this request.                                              |
| `workspace_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | The workspace ID this request was made to.                           |