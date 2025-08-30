from typing import Dict, Type
from app.extraction.base import BaseExtractor

class ExtractorRegistry:
    def __init__(self):
        self._extractors: Dict[str, Type[BaseExtractor]] = {}

    def register(self, name: str, extractor: Type[BaseExtractor]):
        self._extractors[name] = extractor

    def get_extractor(self, name: str) -> Type[BaseExtractor]:
        extractor = self._extractors.get(name)
        if not extractor:
            raise ValueError(f"Extractor '{name}' not found in registry.")
        return extractor

registry = ExtractorRegistry()