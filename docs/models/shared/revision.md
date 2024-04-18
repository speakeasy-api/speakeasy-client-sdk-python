# Revision


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             | Example                                                                 |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `created_at`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)    | :heavy_check_mark:                                                      | N/A                                                                     |                                                                         |
| `digest`                                                                | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     | sha256:6d1ef012b5674ad8a127ecfa9b5e6f5178d171b90ee462846974177fd9bdd39f |
| `id`                                                                    | *str*                                                                   | :heavy_check_mark:                                                      | Format {namespace_id}/{revision_digest}                                 |                                                                         |
| `namespace_name`                                                        | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |                                                                         |
| `tags`                                                                  | List[*str*]                                                             | :heavy_check_mark:                                                      | N/A                                                                     |                                                                         |
| `updated_at`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)    | :heavy_check_mark:                                                      | N/A                                                                     |                                                                         |