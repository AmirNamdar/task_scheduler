from typing import Any

from asyncpg import UniqueViolationError
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import as_declarative, declared_attr

from data_access_layer.errors import DBLayerError


@as_declarative()
class BaseReadOnly:
    id: Any
    __name__: str
    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()

    async def save(self, db_session: AsyncSession):
        """

        :param db_session:
        :return:
        """
        try:
            db_session.add(self)
            return await db_session.commit()
        except SQLAlchemyError as exc:
            raise DBLayerError(message=repr(exc)) from exc

    async def delete(self, db_session: AsyncSession):
        """

        :param db_session:
        :return:
        """
        try:
            await db_session.delete(self)
            await db_session.commit()
            return True
        except SQLAlchemyError as exc:
            raise DBLayerError(message=repr(exc)) from exc

    async def update(self, db: AsyncSession, **kwargs):
        """

        :param db:
        :param kwargs
        :return:
        """
        try:
            for k, v in kwargs.items():
                setattr(self, k, v)
            return await db.commit()
        except SQLAlchemyError as exc:
            raise DBLayerError(message=repr(exc)) from exc

    async def save_or_update(self, db: AsyncSession):
        try:
            db.add(self)
            return await db.commit()
        except IntegrityError as exc:
            if isinstance(exc.orig, UniqueViolationError):
                return await db.merge(self)
            else:
                raise DBLayerError(message=repr(exc)) from exc
        finally:
            await db.close()
            pass
