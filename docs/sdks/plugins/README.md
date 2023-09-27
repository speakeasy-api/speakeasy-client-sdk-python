# Plugins
(*plugins*)

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
from speakeasy.models import shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)


res = s.plugins.get_plugins()

if res.plugins is not None:
    # handle response
```


### Response

**[operations.GetPluginsResponse](../../models/operations/getpluginsresponse.md)**


## run_plugin

Run a plugin

### Example Usage

```python
import speakeasy
from speakeasy.models import operations, shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = operations.RunPluginRequest(
    filters=shared.Filters(
        filters=[
            shared.Filter(
                key='aspernatur',
                operator='perferendis',
                value='ad',
            ),
        ],
        limit=617636,
        offset=149675,
        operator='iste',
    ),
    plugin_id='dolor',
)

res = s.plugins.run_plugin(req)

if res.bounded_requests is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.RunPluginRequest](../../models/operations/runpluginrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.RunPluginResponse](../../models/operations/runpluginresponse.md)**


## upsert_plugin

Upsert a plugin

### Example Usage

```python
import speakeasy
import dateutil.parser
from speakeasy.models import shared

s = speakeasy.Speakeasy(
    security=shared.Security(
        api_key="",
    ),
)

req = shared.Plugin(
    code='natus',
    created_at=dateutil.parser.isoparse('2022-01-21T12:46:00.641Z'),
    eval_hash='saepe',
    plugin_id='fuga',
    title='Ms.',
    updated_at=dateutil.parser.isoparse('2022-05-22T05:33:50.280Z'),
    workspace_id='iure',
)

res = s.plugins.upsert_plugin(req)

if res.plugin is not None:
    # handle response
```

### Parameters

| Parameter                                      | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `request`                                      | [shared.Plugin](../../models/shared/plugin.md) | :heavy_check_mark:                             | The request object to use for the request.     |


### Response

**[operations.UpsertPluginResponse](../../models/operations/upsertpluginresponse.md)**

