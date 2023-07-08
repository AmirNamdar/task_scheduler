from fastapi import status
from typing import Optional

from api_layer.responses.base_responses import SuccessResponse, ErrorResponse
from logic_layer.logic_layer_interfaces import TaskModel
from logic_layer.errors import InvalidInputError


class ResponseMessages:
    UNAUTHORIZED = "Unauthorized"
    SOMETHING_WENT_WRONG = "Oops! Something went wrong."


class APIResponseGenerator:
    @staticmethod
    def unexpected_error(exception: Optional[Exception] = None) -> ErrorResponse:
        return ErrorResponse(
            message=ResponseMessages.SOMETHING_WENT_WRONG, exception=exception
        )

    @staticmethod
    def unauthorized(exception: Optional[Exception] = None) -> ErrorResponse:
        return ErrorResponse(
            exception=exception,
            message=ResponseMessages.UNAUTHORIZED,
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    @staticmethod
    def invalid_input(exception: Optional[InvalidInputError] = None) -> ErrorResponse:
        return ErrorResponse(
            exception=exception,
            message=getattr(exception, "message", None),
            field=getattr(exception, "field", None),
            status_code=status.HTTP_400_BAD_REQUEST,
        )


class ResponseGeneratorScheduleNewTask(APIResponseGenerator):
    @staticmethod
    def success(task: TaskModel) -> SuccessResponse:
        return SuccessResponse(data={"id": task.id, "time_left": task.time_left})
