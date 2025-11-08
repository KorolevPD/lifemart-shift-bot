from pydantic_settings import BaseSettings
from pydantic import Field, ValidationError, field_validator


class Settings(BaseSettings):
    """Глобальные настройки бота."""

    BOT_TOKEN: str = Field(..., description="Telegram Bot API token")

    ADMIN_ID: int | None = Field(
        None, description="Telegram ID of Admin user")

    @field_validator("BOT_TOKEN")
    def validate_bot_token(cls, v):
        if not v or not v.strip():
            raise ValueError("BOT_TOKEN cannot be empty")
        return v

    @field_validator("ADMIN_ID")
    def validate_admin_id(cls, v):
        if v <= 0:
            raise ValueError("ADMIN_ID must be a positive number")
        return v

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
