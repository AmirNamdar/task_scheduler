from api_layer.responses.docs.utils import APIDocsUtils
from api_layer.responses.route_responses import ResponseGeneratorScheduleNewTask
from logic_layer.logic_layer_interfaces import TaskModel

RESPONSES = [
    ResponseGeneratorScheduleNewTask.success(task=TaskModel(id="1", time_left=14401)),
    ResponseGeneratorScheduleNewTask.invalid_input(),
    ResponseGeneratorScheduleNewTask.unexpected_error(),
]

SCHEDULE_NEW_TASK_RESPONSES = APIDocsUtils.get_responses_dict(RESPONSES)
