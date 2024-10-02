from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Котенковая'
    description: str = ''
    database_url: str
    max_name_len: int = 100
    api_version: int = 1

    class Config:
        env_file = '.env'


settings = Settings()