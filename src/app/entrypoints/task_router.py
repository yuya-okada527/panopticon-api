from typing import Optional

from domain.models.task_model import TaskCreate, TaskUpdate
from entrypoints.messages.base_message import MutationResponse
from entrypoints.messages.task_message import SearchTasksResponse
from fastapi import APIRouter
from fastapi.params import Path, Query
from services.task_service import search_tasks_service

router = APIRouter(prefix="/v1/tasks", tags=["tasks"])


@router.get("", response_model=SearchTasksResponse)
async def search_tasks(
    *,
    page: Optional[int] = Query(0, ge=0),
    num: Optional[int] = Query(10, ge=0, le=100),
):
    results, hit_num = search_tasks_service()
    return {
        "page": 0,
        "available_page": 0,
        "num": 0,
        "hit_num": hit_num,
        "results": results,
    }


@router.post("", response_model=MutationResponse)
async def create_task(*, task: TaskCreate):
    return {"id": 0}


@router.put("/{task_id}", response_model=MutationResponse)
async def update_task(*, task_id: int = Path(..., ge=0), task: TaskUpdate):
    return {"id": 0}


@router.delete("/{task_id}", response_model=MutationResponse)
async def delete_task(*, task_id: int = Path(..., ge=0)):
    return {"id": 0}
