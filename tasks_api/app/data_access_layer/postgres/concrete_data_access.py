from datetime import datetime

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from data_access_layer.abstract_data_access import (
    AbstractTasksDBAccess,
    AbstractTaskExecutionDBAccess,
)
from data_access_layer.postgres.models import Task
from data_access_layer.postgres.database import get_db
from utils.enums import TaskStatus


class PostgresTasksDataAccess(AbstractTasksDBAccess):
    @staticmethod
    async def create(
        execute_at: datetime,
        url: str,
        retriable: bool,
        status: TaskStatus = TaskStatus.SCHEDULED,
        db_session: AsyncSession = Depends(get_db),
    ):
        try:
            task = Task(
                execute_at=execute_at, url=url, status=status, retriable=retriable
            )
            await task.save(db_session)
            return task
        except Exception as exc:
            raise exc


class PostgresTaskExecutionDataAccess(AbstractTaskExecutionDBAccess):
    @staticmethod
    def create():
        pass
