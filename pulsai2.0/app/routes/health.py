from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.database import SessionLocal
from app.models import Habit

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def read_home(request: Request):
    db = SessionLocal()
    habits = db.query(Habit).all()
    return templates.TemplateResponse("home.html", {"request": request, "habits": habits})
