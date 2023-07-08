from typing import Optional
from utils.base_error import BaseError


# Base errors
class LogicLayerError(BaseError):
    def __init__(self, message: str):
        super().__init__(message)


class InvalidInputError(LogicLayerError):
    def __init__(self, field: str, message: Optional[str] = None):
        super().__init__(message=message or "Invalid input")
        self.field = field


# Specific errors
class InvalidHoursError(InvalidInputError):
    def __init__(self):
        super().__init__(field="hours")


class InvalidMinutesError(InvalidInputError):
    def __init__(self):
        super().__init__(field="minutes")


class InvalidSecondsError(InvalidInputError):
    def __init__(self):
        super().__init__(field="seconds")


class InvalidUrlError(InvalidInputError):
    def __init__(self):
        super().__init__(field="url", message="Malformed URL")
