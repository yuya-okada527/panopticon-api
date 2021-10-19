from typing import List, Tuple

from sqlmodel import Session


def search_tasks_service(
    *, session: Session, offset: int, limit: int
) -> Tuple[List, int]:
    """タスクを検索する

    Returns:
        Tuple[List, int]: タスクリスト, ヒット数
    """
    return [], 0


def create_task_service() -> int:
    """タスクを作成する

    Returns:
        int: タスクID
    """
    return 0


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
