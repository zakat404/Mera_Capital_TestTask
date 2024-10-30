from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "user_db"
    DB_HOST: str = "db"
    DB_PORT: int = 5432
    DB_NAME: str = "deribit_data"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f"DB_USER: {self.DB_USER}")
        print(f"DB_PASSWORD: {self.DB_PASSWORD}")
        print(f"DB_HOST: {self.DB_HOST}")
        print(f"DB_PORT: {self.DB_PORT}")
        print(f"DB_NAME: {self.DB_NAME}")

settings = Settings()
