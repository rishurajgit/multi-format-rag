from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Gemini Configuration
    GEMINI_API_KEY: str
    LLM_MODEL: str
    EMBEDDING_MODEL: str

    # RAG Configuration
    CHUNK_SIZE: int
    CHUNK_OVERLAP: int

    # Storage
    CHROMA_DB_PATH: str
    UPLOAD_DIR: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()