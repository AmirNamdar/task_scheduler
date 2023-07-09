from enum import Enum


class TaskStatus(str, Enum):
    """Task status enumeration."""

    # Scheduled -> Queued -> Running -> Success/Fail
    SCHEDULED = "SCHEDULED"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"
