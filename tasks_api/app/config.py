import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    otlp_exporter_url: str = os.getenv("OTLP_EXPORTER_URL", "")


@lru_cache()
def get_settings():
    logger.info("Loading config settings from the environment...")
    return Settings()
