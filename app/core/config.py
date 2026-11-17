from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    database_url: str = "sqlite:///./careertrack.db"

    app_name: str = "CareerTrack"
    debug: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()