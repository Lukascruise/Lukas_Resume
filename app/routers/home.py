from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.main import templates   # 👈 main.py 에서 가져오기

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})