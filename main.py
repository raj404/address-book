from fastapi import FastAPI
from database import engine
import models
from routers import address

models.Base.metadata.create_all(bind=engine)

application = FastAPI()


application.include_router(address.app)
