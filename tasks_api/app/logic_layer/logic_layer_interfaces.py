from pydantic import BaseModel


class SetNewTimerInput(BaseModel):
    hours: int
    minutes: int
    seconds: int
    url: str


class TaskModel(BaseModel):
    id: str
    time_left: int
