from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # Allow tests to skip loading .env by setting TESTING in the environment
    if os.environ.get("TESTING"):
        model_config = SettingsConfigDict(env_file=None)
    else:
        model_config = SettingsConfigDict(env_file=".env")


settings = Settings()