from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json
import pathlib

app = FastAPI()
BASE_DIR = pathlib.Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# 정적 파일 제공
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    with open(BASE_DIR.parent / "projects.json", "r", encoding="utf-8") as f:
        projects = json.load(f)
    return templates.TemplateResponse("home.html", {"request": request, "projects": projects})

@app.get("/projects", response_class=HTMLResponse)
async def projects_page(request: Request):
    with open(BASE_DIR.parent / "projects.json", "r", encoding="utf-8") as f:
        projects = json.load(f)
    return templates.TemplateResponse("projects.html", {"request": request, "projects": projects})

