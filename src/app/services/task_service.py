from typing import List, Optional, Tuple

from domain.models.task_model import Task, TaskCreate, TaskUpdate
from sqlmodel import Session, desc, select

DEFAULT_ORDER_KEYS = ["status"]


def search_tasks_service(
    *,
    session: Session,
    offset: int,
    limit: int,
    order_keys: List[str] = DEFAULT_ORDER_KEYS,
) -> Tuple[List[Task], int]:
    """タスクを検索する

    Returns:
        Tuple[List, int]: タスクリスト, ヒット数
    """
    statements = select(Task).offset(offset).limit(limit)
    for order_key in order_keys:
        # TODO 昇順・降順の制御
        statements = statements.order_by(desc(Task.order_key(order_key)))
    results = session.exec(statements).all()
    # TODO countのクエリを作る
    return results, len(results)


def read_task_service(*, session: Session, task_id: int) -> Optional[Task]:
    """タスクを取得する

    Returns:
        Optional[Task]: タスク
    """
    return session.get(Task, task_id)


def create_task_service(*, session: Session, task: TaskCreate) -> int:
    """タスクを作成する

    Returns:
        int: タスクID
    """
    new_task: Task = Task.from_orm(task)
    new_task.before_create()
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task.id


def update_task_service(
    *, session: Session, task_id: int, task: TaskUpdate
) -> Optional[int]:
    """タスクを更新する

    Returns:
        int: タスクID
    """
    target = session.get(Task, task_id)
    if not target:
        return None
    for key, value in task.dict(exclude_unset=True).items():
        setattr(target, key, value)
    target.before_update()
    session.add(target)
    session.commit()
    return task_id


def delete_task_service(*, session: Session, task_id: int) -> Optional[int]:
    """タスクを削除する

    Returns:
        int: タスクID
    """
    target = session.get(Task, task_id)
    if not target:
        return None
    session.delete(target)
    session.commit()
    return task_id
