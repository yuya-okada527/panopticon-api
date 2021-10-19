from core.config import CORE_SETTINGS, EnvEnum
from domain.models.task_model import create_db_and_tables
from entrypoints import task_router
from fastapi import FastAPI

app = FastAPI(
    title="Panopticon API", description="セルフモニタリングツールPanopticonのためのAPI", version="v1"
)

##################
# ルータ定義
##################
app.include_router(task_router.router)
