from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

class Settings(BaseSettings):
    data_file: Path = Path("./data.json")
    llm_model_name: str = "gemini-2.5-flash"
    llm_model_provider: str = "google_genai"
    llm_api_key: str = ""
    max_history_size: int = 10

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
