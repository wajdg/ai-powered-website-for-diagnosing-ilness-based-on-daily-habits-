from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import health
from app.models import Base
from app.database import engine

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(health.router)
