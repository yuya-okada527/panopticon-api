from typing import Optional

from pydantic import BaseModel


class SearchResponse(BaseModel):
    "検索APIの共通レスポンス"
    # 取得したページ(0始まり)
    page: int
    # 取得可能最大ページ
    available_page: int
    # 返したデータの数
    num: int
    # 検索にヒットしたデータの数
    hit_num: int


class MutationResponse(BaseModel):
    "更新APIの共通レスポンス"
    # 更新対象ID
    id: Optional[int]
