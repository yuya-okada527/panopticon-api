from datetime import datetime

import pytest
from domain.models.task_model import Task, TaskCreate, TaskUpdate
from services.task_service import (
    create_task_service,
    delete_task_service,
    read_task_service,
    search_tasks_service,
    update_task_service,
)
from sqlmodel import Session


@pytest.mark.parametrize("args", [[0, 2, 5, 2], [1, 3, 4, 3], [3, 3, 5, 2]])
def test_search_tasks_service_offset_limit(session: Session, args):
    offset, limit, count, expected = args
    for i in range(count):
        task = Task(name=f"name{i}", status="todo")
        task.before_create()
        session.add(task)
    session.commit()
    _, hit_num = search_tasks_service(session=session, offset=offset, limit=limit)
    assert hit_num == expected


# TODO order_keysのテストを追加


def test_create_task_service(session: Session, freezer):
    freezer.move_to("2021-10-23")
    task = TaskCreate(name="name", status="todo")
    task_id = create_task_service(session=session, task=task)
    db_task = session.get(Task, task_id)
    expected = task.dict()
    expected["id"] = task_id
    expected["created_at"] = datetime(2021, 10, 23)
    expected["updated_at"] = datetime(2021, 10, 23)
    assert expected == db_task.dict()


def test_read_service(session: Session):
    target_task = Task(name="name", status="todo")
    target_task.before_create()
    session.add(target_task)
    session.commit()
    session.refresh(target_task)
    assert read_task_service(session=session, task_id=1) == target_task


def test_update_task_service_exist_task(session: Session):
    target_task = Task(name="name", status="todo")
    target_task.before_create()
    session.add(target_task)
    session.commit()
    session.refresh(target_task)
    task_id = update_task_service(
        session=session, task_id=1, task=TaskUpdate.validate({"status": "doing"})
    )
    session.refresh(target_task)
    assert task_id == 1
    assert target_task.status == "doing"
    assert target_task.name == "name"


def test_update_task_service_non_exist_task(session: Session):
    task_id = update_task_service(
        session=session, task_id=1, task=TaskUpdate.validate({"status": "doing"})
    )
    assert task_id is None


def test_delete_task_service_target_exist(session: Session):
    target_task = Task(name="name", status="todo")
    target_task.before_create()
    session.add(target_task)
    session.commit()
    task_id = delete_task_service(session=session, task_id=1)
    assert task_id == 1
    assert session.get(Task, 1) is None


def test_delete_task_service_if_target_not_exist(session: Session):
    task_id = delete_task_service(session=session, task_id=1)
    assert task_id is None
