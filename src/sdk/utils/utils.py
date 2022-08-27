import json
from dataclasses import (Field, dataclass, field, fields, is_dataclass,
                         make_dataclass)
from typing import List, Tuple

import requests
from dataclasses_json import DataClassJsonMixin


def configure_security_client(client: requests.Session, security: dataclass):
    schemes: Tuple[Field, ...] = fields(security)
    for scheme_field in schemes:
        metadata = scheme_field.metadata.get('security')
        if metadata is None:
            continue
        if metadata.get('scheme'):
            scheme = getattr(security, scheme_field.name)
            securityTypes: Tuple[Field, ...] = fields(scheme)
            for security_type_field in securityTypes:
                security_metadata = security_type_field.metadata.get(
                    'security')
                if security_metadata is None:
                    continue
                if security_metadata.get('type') == 'apiKey' and security_metadata.get('in') == 'header':
                    headerName = security_metadata.get('field_name')
                    if headerName is None:
                        continue
                    client.headers[headerName] = getattr(
                        scheme, security_type_field.name)


def generate_url(server_url: str, path: str, path_params: dataclass) -> str:
    param_fields: Tuple[Field, ...] = fields(path_params)
    for f in param_fields:
        param_metadata = f.metadata.get('path_param')
        if not param_metadata:
            continue
        if param_metadata.get('style', 'simple') == 'simple':
            param = getattr(path_params, f.name)
            # only the below types currently supported
            if isinstance(param, (str, int, float, bool)):
                path = path.replace(
                    '{' + param_metadata.get('field_name', f.name) + '}', str(param), 1)

    return server_url.removesuffix("/") + path


def get_query_params(query_params: dataclass) -> dict[str, List[str]]:
    params: dict[str, List[str]] = {}

    param_fields: Tuple[Field, ...] = fields(query_params)
    for f in param_fields:
        param_metadata = f.metadata.get('query_param')
        if not param_metadata:
            continue
        # only the below serialization types currently supported
        if param_metadata.get('style', 'form') != 'deepObject':
            continue
        obj = getattr(query_params, f.name)
        if is_dataclass(obj):
            obj_fields: Tuple[Field, ...] = fields(obj)
            for obj_field in obj_fields:
                obj_param_metadata = obj_field.metadata.get('query_param')
                if not obj_param_metadata:
                    continue
                params[f'{param_metadata.get("field_name", f.name)}[{obj_param_metadata.get("field_name", obj_field.name)}]'] = [
                    getattr(obj, obj_field.name)]
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, list):
                    params[f'{param_metadata.get("field_name", f.name)}[{key}]'] = value
                else:
                    params[f'{param_metadata.get("field_name", f.name)}[{key}]'] = [
                        value]

    return params


def serialize_request_body(request: dataclass) -> Tuple[str, any, any]:
    if request is None:
        return None, None, None

    request_val = getattr(request, "request")
    if request_val is None:
        raise Exception("request body not found")

    request_fields: Tuple[Field, ...] = fields(request)
    request_metadata = None

    for f in request_fields:
        if f.name == "request":
            request_metadata = f.metadata.get('request')
            break

    if not request_metadata is None:
        # single request
        return serialize_content_type(request_metadata, request_val)

    request_fields: Tuple[Field, ...] = fields(request_val)
    for f in request_fields:
        req = getattr(request_val, f.name)
        if req is None:
            continue

        request_metadata = f.metadata.get('request')
        if request_metadata is None:
            raise Exception(
                f'missing request tag on request body field {f.name}')

        return serialize_content_type(request_metadata, req)


def serialize_content_type(metadata, request: dataclass) -> Tuple[str, any, any]:
    media_type = metadata.get('media_type', 'application/octet-stream')

    if media_type == 'application/json':
        return media_type, marshal_json(request).encode(), None
    elif media_type == 'multipart/form-data':
        form: List[List[any]] = []
        request_fields: Tuple[Field, ...] = fields(request)
        for f in request_fields:
            field_metadata = f.metadata.get('multipart_form')
            if field_metadata is None:
                continue
            if field_metadata.get("file") is True:
                file = getattr(request, f.name)
                file_fields = fields(file)

                file_name = ""
                field_name = ""
                content = bytes()

                for file_field in file_fields:
                    file_metadata = file_field.metadata.get('multipart_form')
                    if file_metadata is None:
                        continue
                    if file_metadata.get("content") is True:
                        content = getattr(file, file_field.name)
                    else:
                        field_name = file_metadata.get(
                            "field_name", file_field.name)
                        file_name = getattr(file, file_field.name)
                if field_name == "" or file_name == "" or content == bytes():
                    raise Exception('invalid multipart/form-data file')

                form.append([field_name, [file_name, content]])
            else:
                form.append([field_metadata.get("field_name", f.name), [
                            None, getattr(request, f.name)]])
        return media_type, None, form
    else:
        if isinstance(request, (bytes, bytearray)):
            return media_type, request, None
        else:
            raise Exception(
                f"invalid request body type {type(request)} for mediaType {metadata['media_type']}")


def unmarshal_json(data, t):
    Unmarhsal = make_dataclass('Unmarhsal', [('res', t)],
                               bases=(DataClassJsonMixin,))
    d = json.loads(data)
    out = Unmarhsal.from_dict({"res": d})
    return out.res


def marshal_json(c):
    Marshal = make_dataclass('Marshal', [('res', type(c))],
                             bases=(DataClassJsonMixin,))
    m = Marshal(res=c)
    d = m.to_dict()
    return json.dumps(d["res"])
