from typing import List, Tuple

from domain.models.task_model import Task, TaskCreate
from sqlmodel import Session, select


def search_tasks_service(
    *, session: Session, offset: int, limit: int
) -> Tuple[List[Task], int]:
    """タスクを検索する

    Returns:
        Tuple[List, int]: タスクリスト, ヒット数
    """
    results = session.exec(select(Task).offset(offset).limit(limit)).all()
    # TODO countのクエリを作る
    return results, len(results)


def create_task_service(*, session: Session, task: TaskCreate) -> int:
    """タスクを作成する

    Returns:
        int: タスクID
    """
    new_task = Task.from_orm(task)
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task.id


def update_task_service() -> int:
    """タスクを更新する

    Returns:
        int: タスクID
    """
    return 0


def delete_task_service() -> int:
    """タスクを削除する

    Returns:
        int: タスクID
    """
    return 0
