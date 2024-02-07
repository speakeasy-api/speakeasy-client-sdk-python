# RunPluginRequest


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `plugin_id`                                                | *str*                                                      | :heavy_check_mark:                                         | The ID of the plugin to run.                               |
| `filters`                                                  | [Optional[shared.Filters]](../../models/shared/filters.md) | :heavy_minus_sign:                                         | The filter to apply to the query.                          |