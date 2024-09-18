from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/moderador")
templates = obter_jinja_templates("templates/moderador")

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

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

@router.get("/exibirprojetosaprovados", response_class=HTMLResponse)
async def get_exibirprojetosAprovados(request: Request):
    return templates.TemplateResponse("pages/exibirprojetosAprovados.html", {"request": request})

@router.get("/exibirprojetosrejeitados", response_class=HTMLResponse)
async def get_exibirprojetosRejeitados(request: Request):
    return templates.TemplateResponse("pages/exibirprojetosRejeitados.html", {"request": request})

@router.get("/exibirprojetoespecifico", response_class=HTMLResponse)
async def get_exibirprojetoEspecifico(request: Request):
    return templates.TemplateResponse("pages/exibirprojetoEspecifico.html", {"request": request})

@router.get("/alterarsenhamoderador", response_class=HTMLResponse)
async def get_alterarsenhaModerador(request: Request):
    return templates.TemplateResponse("pages/alterarsenhaModerador.html", {"request": request})

@router.get("/mensagemexclusao", response_class=HTMLResponse)
async def get_mensagemExclusao(request: Request):
    return templates.TemplateResponse("pages/mensagemExclusao.html", {"request": request})