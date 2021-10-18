from typing import List, Optional

TASK_API_PATH = "/v1/tasks"


def make_url(path: str, queries: Optional[List[str]] = None):
    assert isinstance(queries, list) or queries is None

    # クエリがあれば、クエリつきでURL作成
    if queries:
        return path + "?" + "&".join(queries)

    # クエリがない場合、パスのみ
    return path
