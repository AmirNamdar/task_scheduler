import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import UUID, Column, Integer, ForeignKey, DateTime, String

from data_access_layer.postgres.base_model import Base

from uuid import uuid4


class Task(Base):
    __tablename__ = "task"
    __table_args__ = {"schema": "tasks"}

    id = Column(
        UUID(as_uuid=True),
        unique=True,
        default=uuid4,
        primary_key=True,
    )

    attempts = Column(Integer, nullable=False, primary_key=False, unique=False)
    status = Column(String, nullable=False)
    run_at = Column(DateTime, nullable=False)
    changed_at = Column(DateTime, nullable=True)


class TaskExecution(Base):
    __tablename__ = "task_execution"
    __table_args__ = {"schema": "tasks"}

    id = Column(
        UUID(as_uuid=True),
        unique=True,
        default=uuid4,
        primary_key=True,
    )

    task_id = Column(
        UUID(as_uuid=True),
        ForeignKey("tasks.task.id"),
        nullable=False,
        primary_key=False,
        unique=False,
    )

    task = relationship("Task", back_populates="task_execution")
    end = Column(DateTime, nullable=True)
    worker = Column(String, nullable=False)
    start = Column(DateTime, nullable=False)
    response = Column(String, nullable=True)
