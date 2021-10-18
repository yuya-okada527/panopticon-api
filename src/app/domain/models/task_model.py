from typing import Optional

from domain.enums.task_enum import TaskStatusEnum
from pydantic import validator
from sqlmodel import Field, SQLModel


class TaskCreate(SQLModel):
    name: str = Field(min_length=1, max_length=64)
    status: str = Field(regex=TaskStatusEnum.status_regex())

    @validator("name")
    def name_must_not_be_blank(cls, v):
        if v.strip() == "":
            raise ValueError("must not be blank")
        return v


class TaskUpdate(SQLModel):
    name: Optional[str] = Field(None, min_length=1, max_length=64)
    status: Optional[str] = Field(None, regex=TaskStatusEnum.status_regex())

    @validator("name")
    def name_must_not_be_blank(cls, v):
        if v and v.strip() == "":
            raise ValueError("must not be blank")
        return v
