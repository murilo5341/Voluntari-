from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/moderador")
templates = obter_jinja_templates("templates/moderador")

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

@router.get("/exibirmoderador", response_class=HTMLResponse)
async def get_exibirModerador(request: Request):
    return templates.TemplateResponse("pages/exibirModerador.html", {"request": request})

@router.get("/perfilmoderador", response_class=HTMLResponse)
async def get_perfilModerador(request: Request):
    return templates.TemplateResponse("pages/perfilModerador.html", {"request": request})

@router.get("/moderadorcomassinatura", response_class=HTMLResponse)
async def get_moderadorcomAssinatura(request: Request):
    return templates.TemplateResponse("pages/moderadorcomAssinatura.html", {"request": request})

@router.get("/resumodeatividades", response_class=HTMLResponse)
async def get_resumodeAtividades(request: Request):
    return templates.TemplateResponse("pages/resumodeAtividades.html", {"request": request})

@router.get("/desativarcontamoderador", response_class=HTMLResponse)
async def get_desativarcontaModerador(request: Request):
    return templates.TemplateResponse("pages/desativarcontaModerador.html", {"request": request})

@router.get("/exibirprojetosrecentes", response_class=HTMLResponse)
async def get_exibirprojetosRecentes(request: Request):
    return templates.TemplateResponse("pages/exibirprojetosRecentes.html", {"request": request})