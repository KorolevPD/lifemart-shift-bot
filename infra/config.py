from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field, ValidationError, field_validator


class Settings(BaseSettings):
    """Глобальные настройки бота."""

    # General
    DEBUG: bool = Field(True)

    # Telegram Bot
    BOT_TOKEN: str = Field(..., description="Telegram Bot API token")

    # Database
    DB_NAME: str = Field("db_name", description="Database name")
    DB_USER: str = Field("admin", description="Database user")
    DB_PASSWORD: str = Field("password", description="Database user password")
    DB_HOST: str = Field("localhost", description="Database host")
    DB_PORT: int = Field(5432, description="Database port")
    DB_URL: Optional[str] = Field(
        None, description="Connection URL (optional)")

    @field_validator("BOT_TOKEN")
    def validate_bot_token(cls, v):
        if not v or not v.strip():
            raise ValueError("BOT_TOKEN cannot be empty")
        return v

    @property
    def db_url(self) -> str:
        """Возвращает полный URL для подключения к БД"""
        if self.DB_URL:
            return self.DB_URL
        return (f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@'
                f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}')

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


try:
    settings = Settings()
except ValidationError as e:
    raise SystemExit(f"Configuration error:\n{e}")


if __name__ == "__main__":
    print(settings)
