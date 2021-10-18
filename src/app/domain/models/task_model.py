from domain.enums.task_enum import TaskStatusEnum
from sqlmodel import Field, SQLModel


class TaskCreate(SQLModel):
    # TODO スペースのみをバリデーション
    name: str = Field(min_length=1, max_length=64)
    status: str = Field(regex=TaskStatusEnum.status_regex())
