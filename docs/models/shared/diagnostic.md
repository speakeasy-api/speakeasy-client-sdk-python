# Diagnostic


## Fields

| Field                                 | Type                                  | Required                              | Description                           |
| ------------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------- |
| `help_message`                        | *Optional[str]*                       | :heavy_minus_sign:                    | Help message for how to fix the issue |
| `message`                             | *str*                                 | :heavy_check_mark:                    | Message describing the issue          |
| `path`                                | List[*str*]                           | :heavy_check_mark:                    | Schema path to the issue              |
| `type`                                | *str*                                 | :heavy_check_mark:                    | Issue type                            |