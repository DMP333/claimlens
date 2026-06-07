from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # API Keys
    GOOGLE_FACTCHECK_API_KEY: str = ""
    SEMANTIC_SCHOLAR_API_KEY: str = ""
    OPEN_PAGE_RANK_KEY: str = ""

    # Database (PostgreSQL)
    DATABASE_URL: str = ""

    # App settings
    DEBUG: bool = True

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()