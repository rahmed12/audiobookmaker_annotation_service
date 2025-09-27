from __future__ import annotations
from typing import Callable, List, Dict, Optional
from abc import ABC, abstractmethod

ProgressCb = Optional[Callable[[int, int, int, int], None]]

class Extractor(ABC):
    name: str
    @abstractmethod
    async def extract_full(self, *, text: str, passes: int, max_char_buffer: int) -> List[Dict]: ...
    @abstractmethod
    async def extract_chunked(self, *, text: str, buffer_chars: int, overlap_chars: int,
                              passes: int, resume_char_offset: int, on_progress: ProgressCb) -> List[Dict]: ...