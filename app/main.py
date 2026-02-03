from fastapi import FastAPI
from app.routers import items
from app.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(items.router, prefix="/items", tags=["items"])
#helllo