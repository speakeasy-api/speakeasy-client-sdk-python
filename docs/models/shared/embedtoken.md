# EmbedToken

A representation of an embed token granted for working with Speakeasy components.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Creation timestamp.                                                  |
| `created_by`                                                         | *str*                                                                | :heavy_check_mark:                                                   | The ID of the user that created this token.                          |
| `description`                                                        | *str*                                                                | :heavy_check_mark:                                                   | A detailed description of the EmbedToken.                            |
| `expires_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The time this token expires.                                         |
| `filters`                                                            | *str*                                                                | :heavy_check_mark:                                                   | The filters applied to this token.                                   |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | The ID of this EmbedToken.                                           |
| `last_used`                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The last time this token was used.                                   |
| `revoked_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | The time this token was revoked.                                     |
| `revoked_by`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The ID of the user that revoked this token.                          |
| `workspace_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | The workspace ID this token belongs to.                              |