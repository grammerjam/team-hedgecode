from pydantic_settings import BaseSettings, SettingsConfigDict
from motor.motor_asyncio import AsyncIOMotorClient

class CommonSettings(BaseSettings):
    APP_NAME: str = "NTFX_APP"
    VERSION: str = "1.0.0"
    DEBUG_MODE: bool = False


class ServerSettings(BaseSettings):
    HOST: str = "localhost"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URI: str
    DB_NAME: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    async def initiate_database(self):
        client = AsyncIOMotorClient(self.DB_URI)
        return client


settings = Settings()



