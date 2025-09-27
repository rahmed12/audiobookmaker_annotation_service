from typing import Dict
from .base import Extractor
_REGISTRY: Dict[str, Extractor] = {}
def register(engine: Extractor) -> None: _REGISTRY[engine.name] = engine
def get(name: str) -> Extractor:
    if name not in _REGISTRY:
        raise ValueError(f"Unknown engine '{name}'. Available: {list(_REGISTRY)}")
    return _REGISTRY[name]
def all_names() -> list[str]: return list(_REGISTRY.keys())