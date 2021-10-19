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


##################
# 起動イベント定義
##################
@app.on_event("startup")
def on_startup():
    if CORE_SETTINGS.env == EnvEnum.LOCAL:
        create_db_and_tables()
