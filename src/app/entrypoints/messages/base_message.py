from pydantic import BaseModel


class SearchResponse(BaseModel):
    # 取得したページ(0始まり)
    page: int
    # 取得可能最大ページ
    available_page: int
    # 返したデータの数
    num: int
    # 検索にヒットしたデータの数
    hit_num: int
