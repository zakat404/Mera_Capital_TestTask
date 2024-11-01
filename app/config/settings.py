from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "user_db"
    DB_HOST: str = "db"
    DB_PORT: int = 5432
    DB_NAME: str = "deribit_data"

settings = Settings()
