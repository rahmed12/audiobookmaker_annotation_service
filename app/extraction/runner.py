import asyncpg
from typing import List, Dict, Any
from app.extraction.registry import registry
from app.domain.models import Annotation

async def run_extraction(extractor_name: str, text: str, book_id: int, conn: asyncpg.Connection) -> List[Annotation]:
    extractor_class = registry.get_extractor(extractor_name)
    extractor = extractor_class()
    extracted_data = await extractor.extract(text)

    annotations = []
    for data in extracted_data:
        annotation = Annotation(book_id=book_id, **data)
        # In a real scenario, you'd save this to the database
        # For now, just append to the list
        annotations.append(annotation)
    return annotations