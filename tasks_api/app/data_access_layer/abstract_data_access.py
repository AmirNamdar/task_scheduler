from datetime import datetime

from utils.enums import TaskStatus


class AbstractTasksDBAccess:
    @staticmethod
    async def create(
        execute_at: datetime,
        url: str,
        retriable: bool,
        db_session,
        status: TaskStatus = TaskStatus.SCHEDULED,
    ):
        pass


class AbstractTaskExecutionDBAccess:
    @staticmethod
    def create():
        pass
