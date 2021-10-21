from typing import List

from domain.models.task_model import Task
from entrypoints.messages.base_message import SearchResponse


class SearchTasksResponse(SearchResponse):
    results: List[Task]
