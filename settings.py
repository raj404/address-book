from pydantic import BaseSettings
import os

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

settings = Settings()