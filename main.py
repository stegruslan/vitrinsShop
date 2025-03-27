from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from pathlib import Path
import os
import logging
# ??

logging.basicConfig(level=logging.INFO)
DEBUG = os.getenv("DEBUG", "False") == "True"


app = FastAPI(
    title="VitrinaShop",
    version="1.0.0",
    debug=DEBUG,
)


app.add_middleware(GZipMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://vitrinshop.ru"],
    allow_methods=["GET"],
)

STATIC_DIR = Path("static")
TEMPLATES_DIR = Path("templates")

app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR, html=True),
    name="static",
)
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Роуты
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})