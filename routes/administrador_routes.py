from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from repositories.usuario_repo import UsuarioRepo
from util.templates import obter_jinja_templates

router = APIRouter(prefix="/administrador")
templates = obter_jinja_templates("templates")

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    usuario = UsuarioRepo.obter_por_id(request.state.usuario.id)
    return templates.TemplateResponse("administrador/pages/index.html", {"request": request, "usuario": usuario})

@router.get("/bloquearprojeto", response_class=HTMLResponse)
async def get_bloquearProjeto(request: Request):
    return templates.TemplateResponse("administrador/pages/bloquearProjeto.html", {"request": request})

@router.get("/denunciaprojeto", response_class=HTMLResponse)
async def get_denunciaProjeto(request: Request):
    return templates.TemplateResponse("administrador/pages/denunciaProjeto.html", {"request": request})

@router.get("/cadastrarpatrocinador", response_class=HTMLResponse)
async def get_cadastrarPatrocinador(request: Request):
    return templates.TemplateResponse("administrador/pages/cadastrarPatrocinador.html", {"request": request})

@router.get("/exibirmoderador", response_class=HTMLResponse)
async def get_exibirModerador(request: Request):
    return templates.TemplateResponse("administrador/pages/exibirModerador.html", {"request": request})

@router.get("/alterarsenha", response_class=HTMLResponse)
async def get_alterarsenha(request: Request):
    return templates.TemplateResponse("administrador/pages/alterarsenhaadministrador.html", {"request": request})

@router.get("/notificacao", response_class=HTMLResponse)
async def get_alterarsenha(request: Request):
    return templates.TemplateResponse("administrador/pages/notificacaoadministrador.html", {"request": request})

@router.get("/denunciausuario", response_class=HTMLResponse)
async def get_denunciaProjeto(request: Request):
    return templates.TemplateResponse("administrador/pages/denunciausuario.html", {"request": request})

@router.get("/denunciausuarioaprovada", response_class=HTMLResponse)
async def get_denunciaProjeto(request: Request):
    return templates.TemplateResponse("administrador/pages/denunciausuarioaprovada.html", {"request": request})

@router.get("/usuariobanido", response_class=HTMLResponse)
async def get_denunciaProjeto(request: Request):
    return templates.TemplateResponse("administrador/pages/usuariobanido.html", {"request": request})

@router.get("/visualizardenuncia", response_class=HTMLResponse)
async def get_denunciaProjeto(request: Request):
    return templates.TemplateResponse("administrador/pages/visualizardenuncia.html", {"request": request})

@router.get("/patrocinadores", response_class=HTMLResponse)
async def get_patrocinadores(request: Request):
    return templates.TemplateResponse("administrador/pages/patrocinadores.html", {"request": request})
@router.get("/administradores", response_class=HTMLResponse)
async def get_administradores(request: Request):
    return templates.TemplateResponse("administrador/pages/administradores.html", {"request": request})