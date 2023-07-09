from typing import Union

from api_layer.api_enums import (
    ResourcePrefix,
    APITags,
    ApiRoutes,
)


from fastapi import APIRouter, Depends
from logic_layer.logic_layer_actions import LogicLayer
from api_layer.api_layer_interfaces import SetNewTimerAPIInput
from api_layer.responses.route_responses import ResponseGeneratorScheduleNewTask
from logic_layer.errors import InvalidInputError
from api_layer.responses.docs.schedule_new_task_responses import (
    SCHEDULE_NEW_TASK_RESPONSES,
)
from data_access_layer.postgres.database import get_db

timer_router = APIRouter(prefix=ResourcePrefix.TIMERS, tags=[APITags.TIMERS])


@timer_router.post(
    path=ApiRoutes.ROOT,
    description="Create a new timer",
    responses=SCHEDULE_NEW_TASK_RESPONSES,
)
async def set_new_timer(input: SetNewTimerAPIInput, db_session=Depends(get_db)):
    try:
        #  TODO:
        #  Test cases:
        #  invalid input: bad url
        #  invalid input 2: bad time
        #  valid input: assert response is correct

        data = await LogicLayer.schedule_task(input, db_session=db_session)
        return ResponseGeneratorScheduleNewTask.success(data)
    except InvalidInputError as exc:
        return ResponseGeneratorScheduleNewTask.invalid_input(exception=exc)
    except Exception as exc:
        return ResponseGeneratorScheduleNewTask.unexpected_error(exception=exc)


# @timer_router.get("/{timer_id}")
# async def get_timer_status(timer_id: str) -> TaskModel:
#     if timer_id == "1":
#         return TaskModel(id="1", time_left=14401)
#     pass
