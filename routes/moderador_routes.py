from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from repositories.usuario_repo import UsuarioRepo
from util.templates import obter_jinja_templates

router = APIRouter(prefix="/moderador")
templates = obter_jinja_templates("templates")

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    usuario = UsuarioRepo.obter_por_id(request.state.usuario.id)
    # return templates.TemplateResponse("/moderador/pages/index.html", {"request": request, "usuario": usuario})
    return RedirectResponse("/usuario", 303)

@router.get("/resumodeatividades", response_class=HTMLResponse)
async def get_resumodeAtividades(request: Request):
    return templates.TemplateResponse("/moderador/pages/resumodeAtividades.html", {"request": request})

@router.get("/exibirprojetosrecentes", response_class=HTMLResponse)
async def get_exibirprojetosRecentes(request: Request):
    return templates.TemplateResponse("/moderador/pages/exibirprojetosRecentes.html", {"request": request})

@router.get("/exibirprojetosaprovados", response_class=HTMLResponse)
async def get_exibirprojetosAprovados(request: Request):
    return templates.TemplateResponse("/moderador/pages/exibirprojetosAprovados.html", {"request": request})

@router.get("/exibirprojetosrejeitados", response_class=HTMLResponse)
async def get_exibirprojetosRejeitados(request: Request):
    return templates.TemplateResponse("/moderador/pages/exibirprojetosRejeitados.html", {"request": request})

@router.get("/mensagemexclusao", response_class=HTMLResponse)
async def get_mensagemExclusao(request: Request):
    return templates.TemplateResponse("/moderador/pages/mensagemExclusao.html", {"request": request})