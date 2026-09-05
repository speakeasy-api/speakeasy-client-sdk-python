# GenerateBumpType

Bump type of the lock file (calculated semver delta, custom change (manual release), or prerelease/graduate)

## Example Usage

```python
from speakeasy_client_sdk_python.models.shared import GenerateBumpType

value = GenerateBumpType.MAJOR
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `MAJOR`      | major        |
| `MINOR`      | minor        |
| `PATCH`      | patch        |
| `CUSTOM`     | custom       |
| `GRADUATE`   | graduate     |
| `PRERELEASE` | prerelease   |
| `NONE`       | none         |