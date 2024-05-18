# OrganizationUsage


## Fields

| Field                                    | Type                                     | Required                                 | Description                              |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `accessible`                             | *bool*                                   | :heavy_check_mark:                       | Indicates if the features are accessible |
| `accessible_features`                    | List[*str*]                              | :heavy_check_mark:                       | Features that are accessible             |
| `gen_lock_ids`                           | List[*str*]                              | :heavy_check_mark:                       | List of generation lock IDs              |
| `language`                               | *str*                                    | :heavy_check_mark:                       | The programming language used            |
| `number_of_operations`                   | *int*                                    | :heavy_check_mark:                       | Number of operations performed           |
| `used_features`                          | List[*str*]                              | :heavy_check_mark:                       | Features that have been used             |
| `workspaces`                             | List[*str*]                              | :heavy_check_mark:                       | List of workspace IDs                    |