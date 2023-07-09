from sqlalchemy.orm import relationship
from sqlalchemy import UUID, Boolean, Column, Integer, ForeignKey, DateTime, String

from data_access_layer.postgres.base_model import Base

from uuid import uuid4


class Task(Base):
    __tablename__ = "task"

    id = Column(
        UUID(as_uuid=True),
        unique=True,
        default=uuid4,
        primary_key=True,
    )
    url = Column(String, nullable=False)
    attempts = Column(Integer, nullable=False, primary_key=False, unique=False)
    status = Column(String, nullable=False)
    execute_at = Column(DateTime, nullable=False)
    retriable = Column(Boolean, nullable=False, default=True)
    changed_at = Column(DateTime, nullable=True)
    executions = relationship("TaskExecution", back_populates="task")


class TaskExecution(Base):
    __tablename__ = "task_execution"

    id = Column(
        UUID(as_uuid=True),
        unique=True,
        default=uuid4,
        primary_key=True,
    )

    task_id = Column(
        UUID(as_uuid=True),
        ForeignKey("task.id"),
        nullable=False,
        primary_key=False,
        unique=False,
    )

    task = relationship("Task", back_populates="executions")
    end = Column(DateTime, nullable=True)
    worker = Column(String, nullable=False)
    start = Column(DateTime, nullable=False)
    response = Column(String, nullable=True)
