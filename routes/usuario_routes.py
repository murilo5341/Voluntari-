from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from repositories.usuario_repo import UsuarioRepo
from util.templates import obter_jinja_templates

router = APIRouter(prefix="/usuario")
templates = obter_jinja_templates("templates")

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    usuario = UsuarioRepo.obter_por_id(request.state.usuario.id)
    return templates.TemplateResponse("usuario/pages/index.html", {"request": request, "usuario": usuario})
@router.get("/alterarsenha", response_class=HTMLResponse)
async def get_alterarsenha(request: Request):
    return templates.TemplateResponse("usuario/pages/alterarsenha.html", {"request": request})