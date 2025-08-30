import os

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@host:port/dbname")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "super-secret-key")

settings = Settings()