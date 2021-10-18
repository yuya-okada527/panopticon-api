from typing import List

from entrypoints.messages.base_message import SearchResponse


class SearchTasksResponse(SearchResponse):
    results: List
