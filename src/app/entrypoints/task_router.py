from typing import Optional

from domain.models.task_model import TaskCreate
from entrypoints.messages.base_message import MutationResponse
from entrypoints.messages.task_message import SearchTasksResponse
from fastapi import APIRouter
from fastapi.params import Query

router = APIRouter(prefix="/v1/tasks", tags=["tasks"])


@router.get("", response_model=SearchTasksResponse)
async def search_tasks(
    *,
    page: Optional[int] = Query(0, ge=0),
    num: Optional[int] = Query(10, ge=0, le=100),
):
    return {"page": 0, "available_page": 0, "num": 0, "hit_num": 0, "results": []}


@router.post("", response_model=MutationResponse)
async def create_task(*, task: TaskCreate):
    return {"id": 0}
