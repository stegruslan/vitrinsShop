from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import FileResponse, PlainTextResponse
from pathlib import Path
import os
import logging

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
ROOT_DIR = Path(".")

app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR, html=True),
    name="static",
)
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@app.get("/sitemap.xml", include_in_schema=False)
async def get_sitemap():
    return FileResponse(
        ROOT_DIR / "sitemap.xml",
        media_type="application/xml"
    )

@app.get("/robots.txt", include_in_schema=False)
async def get_robots():
    return FileResponse(
        ROOT_DIR / "robots.txt",
        media_type="text/plain"
    )


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})