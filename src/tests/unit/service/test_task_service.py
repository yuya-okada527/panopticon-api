import pytest
from domain.models.task_model import Task, TaskCreate
from services.task_service import create_task_service, search_tasks_service
from sqlmodel import Session


@pytest.mark.parametrize("args", [[0, 2, 5, 2], [1, 3, 4, 3], [3, 3, 5, 2]])
def test_search_tasks_service_offset_limit(session: Session, args):
    offset, limit, count, expected = args
    for i in range(count):
        task = Task(name=f"name{i}", status="todo")
        session.add(task)
    session.commit()
    _, hit_num = search_tasks_service(session=session, offset=offset, limit=limit)
    assert hit_num == expected


def test_create_task_service(session: Session):
    task = TaskCreate(name="name", status="todo")
    task_id = create_task_service(session=session, task=task)
    db_task = session.get(Task, task_id)
    expected = task.dict()
    expected["id"] = task_id
    assert expected == db_task.dict()
