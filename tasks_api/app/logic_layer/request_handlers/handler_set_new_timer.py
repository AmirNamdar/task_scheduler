from logic_layer.errors import (
    InvalidHoursError,
    InvalidMinutesError,
    InvalidSecondsError,
    InvalidUrlError,
)
from logic_layer.logic_layer_interfaces import SetNewTimerInput
from logic_layer.logic_layer_interfaces import TaskModel

from utils.validators import DataValidator


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
    @staticmethod
    def handle(input: SetNewTimerInput) -> TaskModel:
        """Handle SetNewTimerInput
        :param input: SetNewTimerInput
        :return: None
        :raises: InvalidInputError
        """
        SetNewTimerRequestValidator.validate(input)
        # 2. create timer
        # 3. return timer id and time left
        # TODO
        return TaskModel(id="1", time_left=14401)
