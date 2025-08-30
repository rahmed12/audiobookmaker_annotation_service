from app.extraction.base import BaseExtractor
from typing import List, Dict, Any

class MockEngine(BaseExtractor):
    async def extract(self, text: str, **kwargs) -> List[Dict[str, Any]]:
        # This is a mock implementation for testing purposes
        print(f"Extracting with MockEngine: {text[:50]}...")
        return [
            {"text": "mock_entity_1", "start_offset": 0, "end_offset": 13, "label": "MOCK_LABEL"},
            {"text": "mock_entity_2", "start_offset": 14, "end_offset": 27, "label": "MOCK_LABEL"},
        ]