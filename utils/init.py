from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    base_url: str = ''
    skip_mocking: bool = True


settings = Settings()
