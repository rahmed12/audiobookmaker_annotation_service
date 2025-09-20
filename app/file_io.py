from pathlib import Path
from .config import settings

def resolve_text_path(text_uri: str) -> Path:
    p = Path(text_uri)
    return p if p.is_absolute() else (Path(settings.storage_root) / p)

def read_text(text_uri: str) -> str:
    return resolve_text_path(text_uri).read_text(encoding="utf-8")