from logging import debug
from pydantic.tools import T
import uvicorn
from fastapi.logger import logger


async def app(scope, receive, send):
    ...


if __name__ == "__main__":
    uvicorn.run("main:application", host="0.0.0.0", port=8000, log_level="info")
