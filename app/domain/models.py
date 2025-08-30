from typing import Optional
from pydantic import BaseModel

class Annotation(BaseModel):
    id: Optional[int] = None
    text: str
    start_offset: int
    end_offset: int
    label: str
    book_id: int