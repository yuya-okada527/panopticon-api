from domain.models.task_model import Task
from resources.seeds import INITIAL_DATA
from services.task_service import search_tasks_service
from sqlmodel import Session
from sqlmodel.sql.expression import select


def test_search_tasks_service(session: Session):
    # TODO フィクスチャー内でしか、データがうまく入らない。。。
    for task in INITIAL_DATA["tasks"]:
        session.add(task)
        session.commit()
        session.refresh(task)
    results, hit_num = search_tasks_service(session=session, offset=0, limit=2)
    # assert results == INITIAL_DATA["tasks"]
    assert hit_num == 2
