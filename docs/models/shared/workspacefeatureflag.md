# WorkspaceFeatureFlag

enum value workspace feature flag

## Example Usage

```python
from speakeasy_client_sdk_python.models.shared import WorkspaceFeatureFlag

value = WorkspaceFeatureFlag.SCHEMA_REGISTRY

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                   | Value                  |
| ---------------------- | ---------------------- |
| `SCHEMA_REGISTRY`      | schema_registry        |
| `CHANGES_REPORT`       | changes_report         |
| `SKIP_SCHEMA_REGISTRY` | skip_schema_registry   |
| `WEBHOOKS`             | webhooks               |