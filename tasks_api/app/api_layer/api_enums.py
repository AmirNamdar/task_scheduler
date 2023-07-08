from enum import Enum


class BaseEnum(Enum):
    # in case we want to add some common functionality to all enums
    pass


class APITags(str, BaseEnum):
    TIMERS = "Timers"


class ResourcePrefix(str, BaseEnum):
    TIMERS = "/timers"


class ApiRoutes(str, BaseEnum):
    ROOT = "/"
