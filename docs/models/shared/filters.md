# Filters

Filters are used to query requests.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `filters`                                            | List[[shared.Filter](../../models/shared/filter.md)] | :heavy_check_mark:                                   | A list of filters to apply to the query.             |
| `limit`                                              | *int*                                                | :heavy_check_mark:                                   | The maximum number of results to return.             |
| `offset`                                             | *int*                                                | :heavy_check_mark:                                   | The offset to start the query from.                  |
| `operator`                                           | *str*                                                | :heavy_check_mark:                                   | The operator to use when combining filters.          |