# UpdatePublishingTokenExpirationRequestBody

The publishing token to update


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `token_name`                                                         | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The new name for the publishing token.                               |
| `valid_until`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | The new expiration date for the publishing token.                    |