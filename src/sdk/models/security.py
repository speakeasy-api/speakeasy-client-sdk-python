from dataclasses import dataclass, field


@dataclass
class Scheme1:
    api_key: str = field(default=None, metadata={'security': { 'field_name': 'x-api-key', 'type': 'apiKey', 'in': 'header' }})
    

@dataclass
class Security:
    scheme1: Scheme1 = field(default=None, metadata={'security': { 'scheme': True }})
    
