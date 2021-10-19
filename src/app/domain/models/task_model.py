from typing import Optional

from core.config import DB_SETTINGS
from domain.enums.task_enum import TaskStatusEnum
from pydantic import validator
from sqlmodel import Field, Session, SQLModel, create_engine

# DBエンジン
ENGINE = create_engine(DB_SETTINGS.db_url, echo=DB_SETTINGS.echo)


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    status: str


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


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)
    # TODO 初期データ作成


async def get_session():
    with Session(ENGINE) as session:
        yield session
