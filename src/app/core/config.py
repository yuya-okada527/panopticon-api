from enum import Enum

from pydantic import BaseSettings


class EnvEnum(Enum):
    LOCAL = "local"
    PROD = "prod"


class CoreSettings(BaseSettings):
    env: EnvEnum = EnvEnum.LOCAL
    fe_domain: str = "http://localhost:8080"


class DBSettings(BaseSettings):
    db_url = "sqlite:///db/database.db"
    echo = True

    class Config:
        env_file = "env/db.env"


############
# 設定初期化
############
CORE_SETTINGS = CoreSettings()
DB_SETTINGS = DBSettings()
