# flake8: noqa
import os
import sys
from pathlib import Path

from sqlmodel import Session
from sqlmodel.sql.expression import select

app_path = os.path.join(Path(__file__).resolve().parents[1], "app")

sys.path.append(app_path)


from domain.models.task_model import ENGINE, Task, create_db_and_tables

# TODO もう少し軽量な方法を検討
INITIAL_DATA = {
    "tasks": [Task(name="task1", status="todo"), Task(name="task2", status="doing")]
}


def seed_tables(session: Session):
    for task in INITIAL_DATA["tasks"]:
        session.add(task)
        session.commit()


if __name__ == "__main__":
    create_db_and_tables(ENGINE)
    with Session(ENGINE) as session:
        seed_tables(session)
