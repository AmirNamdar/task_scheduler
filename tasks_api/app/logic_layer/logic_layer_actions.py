from logic_layer.logic_layer_interfaces import SetNewTimerInput
from logic_layer.request_handlers.handler_set_new_timer import HandlerScheduleNewTask
from logic_layer.logic_layer_interfaces import (
    TaskModel,
)

# This class acts as the getway to the logic layer on terms of:
#  api for available actions, can be consumed both by web apps or cli apps
#  error handling and logging for the logic layer

# each actions is responsible for validating its input and output


class LogicLayer:
    @staticmethod
    def schedule_task(input: SetNewTimerInput) -> TaskModel:
        """Schedule a new task
        :param input: SetNewTimerInput
        :return: task id
        """
        try:
            return HandlerScheduleNewTask.handle(input)
        except Exception as exc:
            raise exc
