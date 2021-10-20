from typing import Optional

from domain.models.task_model import TaskCreate, TaskUpdate, get_session
from entrypoints.helper.base_helper import calc_available_page, calc_offset
from entrypoints.messages.base_message import MutationResponse
from entrypoints.messages.task_message import SearchTasksResponse
from fastapi import APIRouter
from fastapi.params import Depends, Path, Query
from services.task_service import (
    create_task_service,
    delete_task_service,
    search_tasks_service,
    update_task_service,
)
from sqlmodel import Session

router = APIRouter(prefix="/v1/tasks", tags=["tasks"])


@router.get("", response_model=SearchTasksResponse)
async def search_tasks(
    *,
    session: Session = Depends(get_session),
    page: Optional[int] = Query(1, ge=1, description="ページ数(0始まり)"),
    num: Optional[int] = Query(10, ge=0, le=100, description="取得件数"),
):
    results, hit_num = search_tasks_service(
        session=session, offset=calc_offset(page, num), limit=num
    )
    return {
        "page": page,
        "available_page": calc_available_page(num, hit_num),
        "num": len(results),
        "hit_num": hit_num,
        "results": results,
    }


@router.post("", response_model=MutationResponse)
async def create_task(*, session: Depends(get_session), task: TaskCreate):
    task_id = create_task_service(session=session, task=task)
    return {"id": task_id}


@router.put("/{task_id}", response_model=MutationResponse)
async def update_task(*, task_id: int = Path(..., ge=0), task: TaskUpdate):
    update_task_service()
    return {"id": task_id}


@router.delete("/{task_id}", response_model=MutationResponse)
async def delete_task(*, task_id: int = Path(..., ge=0)):
    delete_task_service()
    return {"id": task_id}
