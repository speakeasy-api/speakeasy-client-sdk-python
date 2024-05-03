# AddTags

Request body of tags to add to a revision


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `revision_digest`                          | *str*                                      | :heavy_check_mark:                         | revision digest to add tags too sha256:... |
| `tags`                                     | List[*str*]                                | :heavy_check_mark:                         | string tags to add to the revision         |