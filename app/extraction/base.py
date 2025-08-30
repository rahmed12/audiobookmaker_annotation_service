from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseExtractor(ABC):
    @abstractmethod
    async def extract(self, text: str, **kwargs) -> List[Dict[str, Any]]:
        pass