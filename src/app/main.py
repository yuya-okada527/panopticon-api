from entrypoints import task_router
from fastapi import FastAPI

app = FastAPI()

##############
# ルータ定義
##############
app.include_router(task_router.router)
