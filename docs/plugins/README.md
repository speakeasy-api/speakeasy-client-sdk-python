# plugins

## Overview

REST APIs for managing and running plugins

### Available Operations

* [get_plugins](#get_plugins) - Get all plugins for the current workspace.
* [run_plugin](#run_plugin) - Run a plugin
* [upsert_plugin](#upsert_plugin) - Upsert a plugin

## get_plugins

Get all plugins for the current workspace.

### Example Usage

```python
import speakeasy


s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


res = s.plugins.get_plugins()

if res.plugins is not None:
    # handle response
```

## run_plugin

Run a plugin

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = operations.RunPluginRequest(
    filters=shared.Filters(
        filters=[
            shared.Filter(
                key='repellat',
                operator='mollitia',
                value='occaecati',
            ),
        ],
        limit=253291,
        offset=414369,
        operator='quam',
    ),
    plugin_id='molestiae',
)

res = s.plugins.run_plugin(req)

if res.bounded_requests is not None:
    # handle response
```

## upsert_plugin

Upsert a plugin

### Example Usage

```python
import speakeasy
import dateutil.parser
from speakeasy.models import shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="YOUR_API_KEY_HERE",
    ),
)


req = shared.Plugin(
    code='velit',
    created_at=dateutil.parser.isoparse('2022-09-06T22:51:09.401Z'),
    eval_hash='quis',
    plugin_id='vitae',
    title='Miss',
    updated_at=dateutil.parser.isoparse('2022-05-14T10:37:30.872Z'),
    workspace_id='odit',
)

res = s.plugins.upsert_plugin(req)

if res.plugin is not None:
    # handle response
```
