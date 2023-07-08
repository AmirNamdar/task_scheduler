from typing import AsyncGenerator

from fastapi import HTTPException
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor


from config import get_settings

settings = get_settings()

url = settings.asyncpg_url
print(f"Connecting to {url}")

engine = create_async_engine(
    settings.asyncpg_url,
    future=True,
    echo=True,
)

# expire_on_commit=False will prevent attributes from being expired
# after commit.
AsyncSessionFactory = sessionmaker(
    engine, autoflush=False, expire_on_commit=False, class_=AsyncSession
)


# Dependency
async def get_db() -> AsyncGenerator:
    async with AsyncSessionFactory() as session:
        # logger.debug(f"ASYNC Pool: {engine.pool.status()}")
        yield session
