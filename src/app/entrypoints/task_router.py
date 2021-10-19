from typing import Optional

from domain.models.task_model import TaskCreate, TaskUpdate
from entrypoints.helper.base_helper import calc_available_page
from entrypoints.messages.base_message import MutationResponse
from entrypoints.messages.task_message import SearchTasksResponse
from fastapi import APIRouter
from fastapi.params import Path, Query
from services.task_service import (
    create_task_service,
    delete_task_service,
    search_tasks_service,
    update_task_service,
)

router = APIRouter(prefix="/v1/tasks", tags=["tasks"])


@router.get("", response_model=SearchTasksResponse)
async def search_tasks(
    *,
    page: Optional[int] = Query(1, ge=1, description="ページ数(0始まり)"),
    num: Optional[int] = Query(10, ge=0, le=100, description="取得件数"),
):
    results, hit_num = search_tasks_service()
    return {
        "page": page,
        "available_page": calc_available_page(num, hit_num),
        "num": len(results),
        "hit_num": hit_num,
        "results": results,
    }


@router.post("", response_model=MutationResponse)
async def create_task(*, task: TaskCreate):
    task_id = create_task_service()
    return {"id": task_id}


@router.put("/{task_id}", response_model=MutationResponse)
async def update_task(*, task_id: int = Path(..., ge=0), task: TaskUpdate):
    update_task_service()
    return {"id": task_id}


@router.delete("/{task_id}", response_model=MutationResponse)
async def delete_task(*, task_id: int = Path(..., ge=0)):
    delete_task_service()
    return {"id": task_id}
