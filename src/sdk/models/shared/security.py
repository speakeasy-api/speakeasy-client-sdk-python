from dataclasses import dataclass, field


@dataclass
class APIKey:
    api_key: str = field(default=None, metadata={'security': { 'field_name': 'x-api-key' }})
    

@dataclass
class Security:
    api_key: APIKey = field(default=None, metadata={'security': { 'scheme': True, 'type': 'apiKey', 'sub_type': 'header' }})
    
