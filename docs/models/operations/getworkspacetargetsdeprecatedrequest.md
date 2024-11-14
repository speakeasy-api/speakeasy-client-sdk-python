# GetWorkspaceTargetsDeprecatedRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `workspace_id`                                                         | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Unique identifier of the workspace.                                    |
| `after_last_event_created_at`                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)   | :heavy_minus_sign:                                                     | Filter to only return targets with events created after this timestamp |