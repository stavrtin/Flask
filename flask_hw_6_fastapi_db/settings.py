from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()

Settings(DATABASE_URL="sqlite:///prod_ord_user.db.db")
