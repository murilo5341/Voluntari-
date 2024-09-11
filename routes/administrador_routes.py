from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/administrador")
templates = obter_jinja_templates("templates/administrador")


@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

@router.get("/bloquearprojeto", response_class=HTMLResponse)
async def get_bloquearProjeto(request: Request):
    return templates.TemplateResponse("pages/bloquearProjeto.html", {"request": request})

@router.get("/denunciaprojeto", response_class=HTMLResponse)
async def get_denunciaProjeto(request: Request):
    return templates.TemplateResponse("pages/denunciaProjeto.html", {"request": request})
