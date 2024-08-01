from fastapi import FastAPI
from api.database import Base, engine
from api.routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
