import pytest
from domain.models.task_model import Task
from services.task_service import search_tasks_service
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
