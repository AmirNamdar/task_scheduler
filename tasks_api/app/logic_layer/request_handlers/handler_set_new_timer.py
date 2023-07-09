from datetime import datetime, timedelta
from logic_layer.errors import (
    InvalidHoursError,
    InvalidMinutesError,
    InvalidSecondsError,
    InvalidUrlError,
)
from logic_layer.logic_layer_interfaces import TaskModel
from utils.validators import DataValidator
from data_access_layer.tasks_db_access import TasksDBAccess
from logic_layer.logic_layer_interfaces import SetNewTimerInput


class SetNewTimerRequestValidator:
    @staticmethod
    def validate(input: SetNewTimerInput):
        """Validate SetNewTimerInput
        :param input: SetNewTimerInput
        :return: None
        :raises: InvalidInputError
        """
        if input.hours < 0 or input.hours > 23:
            raise InvalidHoursError()

        if input.minutes < 0 or input.minutes > 59:
            raise InvalidMinutesError()

        if input.seconds < 0 or input.seconds > 59:
            raise InvalidSecondsError()

        if not DataValidator.is_valid_url(input.url):
            raise InvalidUrlError()

        # If needed we can also check that the task isn't already scheduled


class HandlerScheduleNewTask:
    @classmethod
    async def handle(cls, input: SetNewTimerInput, db_session) -> TaskModel:
        """Handle SetNewTimerInput
        :param input: SetNewTimerInput
        :return: TaskModel
        :raises: InvalidInputError
        """
        SetNewTimerRequestValidator.validate(input)

        execute_at = cls._get_execute_at(input)
        # TODO: should return agnostic dataclass, not sqlalchemy model
        task = await TasksDBAccess.task.create(
            url=input.url,
            execute_at=execute_at,
            retriable=input.retriable,
            db_session=db_session,
        )

        return TaskModel(id=str(task.id), time_left=task.time_left_in_seconds)

    @staticmethod
    def _get_execute_at(input: SetNewTimerInput) -> datetime:
        now = datetime.now()
        if now.hour > input.hours or (
            now.hour == input.hours and now.minute > input.minutes
        ):
            execute_at = now + timedelta(days=1)
        else:
            execute_at = datetime(
                year=now.year,
                month=now.month,
                day=now.day,
                hour=input.hours,
                minute=input.minutes,
                second=input.seconds,
            )
        return execute_at
