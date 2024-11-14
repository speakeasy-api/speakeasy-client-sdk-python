# RegistrySubscription

A subscription to a registry event


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `event_type`                                                         | [shared.EventType](../../models/shared/eventtype.md)                 | :heavy_check_mark:                                                   | N/A                                                                  |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `namespace_name`                                                     | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `subscription_settings`                                              | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `subscription_type`                                                  | [shared.SubscriptionType](../../models/shared/subscriptiontype.md)   | :heavy_check_mark:                                                   | N/A                                                                  |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `workspace_id`                                                       | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `deleted_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `tags`                                                               | List[*str*]                                                          | :heavy_minus_sign:                                                   | N/A                                                                  |