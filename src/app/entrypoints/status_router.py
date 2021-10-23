from fastapi import APIRouter

router = APIRouter(prefix="/v1/statuses", tags=["status"])


@router.get("")
async def search_statuses():
    return {}
