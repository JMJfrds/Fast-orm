from pydantic_settings import BaseSettings
from functools import lru_cache



class Settings(BaseSettings):
    app_name: str = "myapp"
    app_debug: bool = False
    app_version: str = "0.0.1"

    db_user: str = 'Fastapi_owner'
    db_password: str = 'npg_rdlUW3Y4Ahow'
    db_host: str = 'ep-falling-thunder-a16fz454-pooler.ap-southeast-1.aws.neon.tech'
    db_port: int = 5432
    db_name: str = 'Fastapi'

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "allow"
    }


@lru_cache()
def get_settings():
    return Settings()