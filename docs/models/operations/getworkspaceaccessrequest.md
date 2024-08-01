# GetWorkspaceAccessRequest


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `gen_lock_id`                                | *Optional[str]*                              | :heavy_minus_sign:                           | Unique identifier of the generation target.  |
| `target_type`                                | *Optional[str]*                              | :heavy_minus_sign:                           | The type of the generated target.            |
| `passive`                                    | *Optional[bool]*                             | :heavy_minus_sign:                           | Skip side-effects like incrementing metrics. |