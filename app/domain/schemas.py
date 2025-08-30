from pydantic import BaseModel, Field

class ExtractRequest(BaseModel):
    book_id: str


class ExtractResponse(BaseModel):
    book_id: str
    engine: str
