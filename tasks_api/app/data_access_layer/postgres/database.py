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
    url,
    future=True,
    echo=True,
)

# expire_on_commit=False will prevent attributes from being expired
# after commit.
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
SQLAlchemyInstrumentor().instrument(engine=engine.sync_engine)


# Dependency
async def get_db() -> AsyncGenerator:
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except SQLAlchemyError as sql_ex:
            await session.rollback()
            raise sql_ex
        except HTTPException as http_ex:
            await session.rollback()
            raise http_ex
        finally:
            await session.close()
