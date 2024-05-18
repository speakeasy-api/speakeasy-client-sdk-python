# OrganizationUsageResponse

A billing summary of organization usage


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `allowed_languages`                                                        | List[*str*]                                                                | :heavy_check_mark:                                                         | List of allowed languages                                                  |
| `total_allowed_languages`                                                  | *int*                                                                      | :heavy_check_mark:                                                         | Total number of allowed languages, -1 if unlimited                         |
| `usage`                                                                    | List[[shared.OrganizationUsage](../../models/shared/organizationusage.md)] | :heavy_check_mark:                                                         | N/A                                                                        |
| `free_trial_expiry`                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_minus_sign:                                                         | Expiry date of the free trial, will be null if no trial                    |