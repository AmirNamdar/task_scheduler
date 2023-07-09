from data_access_layer.postgres.concrete_data_access import (
    PostgresTasksDataAccess,
    PostgresTaskExecutionDataAccess,
)
from data_access_layer.abstract_data_access import (
    AbstractTasksDBAccess,
    AbstractTaskExecutionDBAccess,
)


class TasksDBAccess:
    """
    Easily change db or driver by abstracting the data access layer
    """

    task: AbstractTasksDBAccess = PostgresTasksDataAccess
    task_execution: AbstractTaskExecutionDBAccess = PostgresTaskExecutionDataAccess
