import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from urllib.parse import quote_plus


class Settings(BaseSettings):
    pg_dsn: str = Field(default=(
        "postgresql://postgres:${DB_PASSWORD_INGEST}"
        "@host.docker.internal:${DB_PORT_INGEST}/audiobook_ingestdb"
    ),
    alias="PG_DSN")

    storage_root: str = Field(default=".", alias="STORAGE_ROOT")
    default_engine: str = Field(default="rules", alias="ENGINE")
    buffer_chars: int = Field(default=2000, alias="BUFFER_CHARS")
    overlap_chars: int = Field(default=200, alias="OVERLAP_CHARS")
    passes: int = Field(default=2, alias="PASSES")
    model_id: str = Field(default="gemini-2.5-flash", alias="MODEL_ID")
    max_workers: int = Field(default=8, alias="MAX_WORKERS")
    export_jsonl: bool = Field(default=False, alias="EXPORT_JSONL")
    export_dir: str = Field(default="./out", alias="EXPORT_DIR")
    enable_status_updates: bool = Field(default=True, alias="ENABLE_STATUS_UPDATES")
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    def model_post_init(self, __context):
        # Replace ${DB_PORT_INGEST} manually if still present
        if "${DB_PORT_INGEST}" in self.pg_dsn:
            port = os.getenv("DB_PORT_INGEST", "0000")
            self.pg_dsn = self.pg_dsn.replace("${DB_PORT_INGEST}", port)

        if "${DB_PASSWORD_INGEST}" in self.pg_dsn:
            pwrd = quote_plus(os.getenv("DB_PASSWORD_INGEST", "1234"))
            self.pg_dsn = self.pg_dsn.replace("${DB_PASSWORD_INGEST}", pwrd)
            



settings = Settings()