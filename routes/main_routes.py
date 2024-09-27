from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse

from models.usuario_model import Usuario
from repositories.usuario_repo import UsuarioRepo
from util.auth import NOME_COOKIE_AUTH, criar_token, obter_hash_senha
from util.templates import obter_jinja_templates

router = APIRouter()
templates = obter_jinja_templates("templates/main")
@router.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})


# @router.get("/", response_class=HTMLResponse)
# async def get_root(request: Request):
#     return templates.TemplateResponse("pages/index.html", {"request": request})
@router.get("/entrar")
async def get_root(request: Request):
    usuario = request.state.usuario if hasattr(request.state, "usuario") else None
    if not usuario or not usuario.perfil:
        return templates.TemplateResponse("pages/entrar.html", {"request": request})    
    if usuario.perfil == 1:
        return RedirectResponse("/voluntario", status_code=status.HTTP_303_SEE_OTHER)
    if usuario.perfil == 2:
        return RedirectResponse("/administrador", status_code=status.HTTP_303_SEE_OTHER)
    if usuario.perfil == 3:
        return RedirectResponse("/moderador", status_code=status.HTTP_303_SEE_OTHER)
# @router.get("/post_entrar", response_class=HTMLResponse)
# async def get_entrar(request: Request):
#     return templates.TemplateResponse("pages/entrar.html", {"request": request})

@router.post("/post_entrar")
async def post_entrar(
    email: str = Form(...), 
    senha: str = Form(...)):
    usuario = UsuarioRepo.checar_credenciais(email, senha)
    if usuario is None:
        response = RedirectResponse("/entrar", status_code=status.HTTP_303_SEE_OTHER)
        return response
    token = criar_token(usuario[0], usuario[1], usuario[2], usuario[3])
    nome_perfil = None
    match (usuario[2]):
        case 1: nome_perfil = "voluntario"
        case 2: nome_perfil = "administrador"
        case 3: nome_perfil = "moderador"
        case _: nome_perfil = ""

    response = RedirectResponse(f"/{nome_perfil}", status_code=status.HTTP_303_SEE_OTHER)    
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=token,
        max_age=3600*24*365*10,
        httponly=True,
        samesite="lax"
    )
    return response

@router.get("/cadastro", response_class=HTMLResponse)
async def get_cadastro(request: Request):
    return templates.TemplateResponse("pages/cadastro.html", {"request": request})

@router.post("/post_cadastro")
async def post_cadastro(
    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    senha: str = Form(...),
    confsenha: str = Form(...),
    perfil: int = Form(...)):
    if senha != confsenha:
        return RedirectResponse("/cadastro", status_code=status.HTTP_303_SEE_OTHER)
    senha_hash = obter_hash_senha(senha)
    usuario = Usuario(None, nome, email, telefone, senha_hash, None, perfil)
    UsuarioRepo.inserir(usuario)
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/termos", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/termos.html", {"request": request})

@router.get("/ajuda", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/ajuda.html", {"request": request})

@router.get("/projetos", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/projetos.html", {"request": request})

@router.get("/colaboradores", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/colaboradores.html", {"request": request})

@router.get("/modalidadespatrocinio", response_class=HTMLResponse)
async def get_modalidadesPatrocinio(request: Request):
    return templates.TemplateResponse("pages/modalidadesPatrocinio.html", {"request": request})

@router.get("/esquecisenha", response_class=HTMLResponse)
async def get_EsqueciSenha(request: Request):
    return templates.TemplateResponse("pages/esquecisenha.html", {"request": request})

@router.get("/projetosingressados", response_class=HTMLResponse)
async def get_projetosIngressados(request: Request):
    return templates.TemplateResponse("pages/projetosingressados.html", {"request": request})

@router.get("/patrocinador", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/patrocinador.html", {"request": request})

@router.get("/verificaremail", response_class=HTMLResponse)
async def get_EsqueciSenha(request: Request):
    return templates.TemplateResponse("pages/verificaremail.html", {"request": request})

@router.get("/sobre", response_class=HTMLResponse)
async def get_EsqueciSenha(request: Request):
    return templates.TemplateResponse("pages/sobre.html", {"request": request})

@router.get("/assinarplano", response_class=HTMLResponse)
async def get_assinarPlanoAnual(request: Request):
    return templates.TemplateResponse("pages/assinarPlanoAnual.html", {"request": request})





