import bcrypt
from fastapi import APIRouter, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse

from models.usuario_model import *
from repositories.usuario_repo import UsuarioRepo
from util.auth import NOME_COOKIE_AUTH, criar_token, obter_hash_senha
from util.mensagens import adicionar_mensagem_erro, adicionar_mensagem_sucesso
from util.templates import obter_jinja_templates

router = APIRouter()
templates = obter_jinja_templates("templates")


@router.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("main/pages/index.html", {"request": request})


# @router.get("/", response_class=HTMLResponse)
# async def get_root(request: Request):
#     return templates.TemplateResponse("main/pages/index.html", {"request": request})
@router.get("/entrar")
async def get_root(request: Request):
    usuario = request.state.usuario if hasattr(request.state, "usuario") else None
    if not usuario or not usuario.perfil:
        return templates.TemplateResponse("main/pages/entrar.html", {"request": request})    
    if usuario.perfil == 1:
        return RedirectResponse("/voluntario", status_code=status.HTTP_303_SEE_OTHER)
    if usuario.perfil == 2:
        return RedirectResponse("/administrador", status_code=status.HTTP_303_SEE_OTHER)
    if usuario.perfil == 3:
        return RedirectResponse("/moderador", status_code=status.HTTP_303_SEE_OTHER)
# @router.get("/post_entrar", response_class=HTMLResponse)
# async def get_entrar(request: Request):
#     return templates.TemplateResponse("main/pages/entrar.html", {"request": request})

@router.post("/post_entrar")
async def post_entrar(
    email: str = Form(...), 
    senha: str = Form(...)):
    usuario = UsuarioRepo.checar_credenciais(email, senha)
    if usuario is None:
        response = RedirectResponse("/entrar", status_code=status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(response, "credenciais inválidas.")
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
    adicionar_mensagem_sucesso(response, "login realizado com sucesso")
    return response

@router.post("/alterar_senha")
async def post_senha(request: Request):
    dados = dict(await request.form())
    usuarioAutenticadoDto = (
        request.state.usuario if hasattr(request.state, "usuario") else None
    )
    senha_atual = dados["Senha Atual"]
    nova_senha = dados["Nova Senha"]
    confirmacao_nova_senha = dados["confirmacao_nova_senha"]
    senha_hash = UsuarioRepo.obter_senha_por_email(usuarioAutenticadoDto.email)
    if not senha_hash or not bcrypt.checkpw(senha_atual.encode(), senha_hash.encode()):
        response = RedirectResponse("/usuario/senha", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(
            response, "Senha atual inválida! Cheque o valor digitado e tente novamente."
        )
        return response
    if nova_senha != confirmacao_nova_senha:
        response = RedirectResponse("/usuario/senha", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(
            response,
            "Nova senha e confirmação não conferem! Cheque os valores digitados e tente novamente.",
        )
        return response
    if nova_senha == senha_atual:
        response = RedirectResponse("/usuario/senha", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(
            response,
            "Nova senha deve ser diferente da senha atual! Cheque os valores digitados e tente novamente.",
        )
        return response
    senha_hash = bcrypt.hashpw(nova_senha.encode(), bcrypt.gensalt())
    if UsuarioRepo.atualizar_senha(usuarioAutenticadoDto.id, senha_hash.decode()):
        response = RedirectResponse("/usuario", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_sucesso(response, "Senha atualizada com sucesso!")
        return response
    else:
        response = RedirectResponse("/usuario/senha", status.HTTP_303_SEE_OTHER)
        adicionar_mensagem_erro(
            response,
            "Ocorreu um problema ao atualizar sua senha. Tente novamente mais tarde.",
        )
        return response

@router.get("/cadastro", response_class=HTMLResponse)
async def get_cadastro(request: Request):
    return templates.TemplateResponse("main/pages/cadastro.html", {"request": request})

@router.post("/post_cadastro")
async def post_cadastro(
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    cpf: str = Form(...),
    data_nascimento: str = Form(...),
    telefone: str = Form(...),
    confsenha: str = Form(...)):
    if senha != confsenha:
        return RedirectResponse("/cadastro", status_code=status.HTTP_303_SEE_OTHER)
    senha_hash = obter_hash_senha(senha)
    usuario = Usuario(None, nome, email,senha_hash, cpf,data_nascimento,telefone,perfil=1 )
    UsuarioRepo.inserir(usuario)
    usuario = UsuarioRepo.checar_credenciais(email, senha)
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


@router.get("/termos", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("main/pages/termos.html", {"request": request})

@router.get("/ajuda", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("main/pages/ajuda.html", {"request": request})

@router.get("/projetos", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("main/pages/projetos.html", {"request": request})

@router.get("/colaboradores", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("main/pages/colaboradores.html", {"request": request})

@router.get("/modalidadespatrocinio", response_class=HTMLResponse)
async def get_modalidadesPatrocinio(request: Request):
    return templates.TemplateResponse("main/pages/modalidadesPatrocinio.html", {"request": request})

@router.get("/esquecisenha", response_class=HTMLResponse)
async def get_EsqueciSenha(request: Request):
    return templates.TemplateResponse("main/pages/esquecisenha.html", {"request": request})

@router.get("/projetosingressados", response_class=HTMLResponse)
async def get_projetosIngressados(request: Request):
    return templates.TemplateResponse("main/pages/projetosingressados.html", {"request": request})

@router.get("/patrocinador", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("main/pages/patrocinador.html", {"request": request})

@router.get("/verificaremail", response_class=HTMLResponse)
async def get_EsqueciSenha(request: Request):
    return templates.TemplateResponse("main/pages/verificaremail.html", {"request": request})

@router.get("/sobre", response_class=HTMLResponse)
async def get_EsqueciSenha(request: Request):
    return templates.TemplateResponse("main/pages/sobre.html", {"request": request})

@router.get("/visualizarprojeto", response_class=HTMLResponse)
async def get_voluntarioassinante(request: Request):
    return templates.TemplateResponse("main/pages/visualizarProjeto.html", {"request": request})


@router.get("/sair")
async def get_sair():
    response = RedirectResponse("/", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value="",
        max_age=1,
        httponly=True,
        samesite="lax")
    return response    