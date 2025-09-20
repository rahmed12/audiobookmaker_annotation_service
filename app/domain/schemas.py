from pydantic import BaseModel, Field

class ExtractRequest(BaseModel):
    book_id: str = Field(..., description="UUID of the book")
    mode: str = Field(default="full", pattern="^(full|chunked)$")
    engine: str | None = None
    buffer_chars: int | None = None
    overlap_chars: int | None = None
    passes: int | None = None
    export_jsonl: bool | None = None

class ExtractResponse(BaseModel):
    book_id: str
    engine: str
    mode: str
    chars: int
    spans_written: int
