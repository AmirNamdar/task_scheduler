import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    otlp_exporter_url: str = os.getenv("OTLP_EXPORTER_URL", "")

    pg_user: str = os.getenv("POSTGRES_USER", "")
    pg_pass: str = os.getenv("POSTGRES_PASSWORD", "")
    pg_host: str = os.getenv("POSTGRES_HOST", "")
    pg_database: str = os.getenv("POSTGRES_DB", "")
    asyncpg_url: str = (
        f"postgresql+asyncpg://{pg_user}:{pg_pass}@{pg_host}:5432/{pg_database}"
    )


@lru_cache()
def get_settings():
    logger.info("Loading config settings from the environment...")
    return Settings()
