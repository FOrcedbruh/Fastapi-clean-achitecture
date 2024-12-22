from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

PORT: str = os.environ.get("PORT")
HOST: str = os.environ.get("HOST")
RELOAD: str = os.environ.get("RELOAD")

DB_URL: str = os.environ.get("DB_URL")

class RunCfg(BaseModel):
    port: int = int(PORT)
    host: str = HOST
    reload: bool = bool(RELOAD)

class DBcfg(BaseModel):
    url: str = DB_URL
    echo: bool = True


class Settings(BaseSettings):
    runcfg: RunCfg = RunCfg()
    db: DBcfg = DBcfg()


settings = Settings()