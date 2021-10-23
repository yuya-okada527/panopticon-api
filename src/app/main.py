from core.middleware import CORS
from entrypoints import task_router
from fastapi import FastAPI

app = FastAPI(
    title="Panopticon API", description="セルフモニタリングツールPanopticonのためのAPI", version="v1"
)

# ルータ定義
app.include_router(task_router.router)

# ミドルウェア定義
app.add_middleware(**CORS)
