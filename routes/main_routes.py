from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter()
templates = obter_jinja_templates("templates/main")


@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

@router.get("/entrar", response_class=HTMLResponse)
async def get_entrar(request: Request):
    return templates.TemplateResponse("pages/entrar.html", {"request": request})

@router.get("/cadastro", response_class=HTMLResponse)
async def get_cadastro(request: Request):
    return templates.TemplateResponse("pages/cadastro.html", {"request": request})

@router.get("/termos", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/termos.html", {"request": request})

@router.get("/ajuda", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/ajuda.html", {"request": request})

@router.get("/perfil", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/perfil.html", {"request": request})

@router.get("/assinaturadousuarioassinante", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/assinaturadousuarioassinante.html", {"request": request})

@router.get("/desativarconta", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/desativarconta.html", {"request": request})

@router.get("/projetos", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/projetos.html", {"request": request})

@router.get("/colaboradores", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/colaboradores.html", {"request": request})

@router.get("/patrocinador", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/patrocinador.html", {"request": request})

@router.get("/denunciaprojeto", response_class=HTMLResponse)
async def get_denunciaProjeto(request: Request):
    return templates.TemplateResponse("pages/denunciaProjeto.html", {"request": request})

@router.get("/excluirprojeto", response_class=HTMLResponse)
async def get_excluirProjeto(request: Request):
    return templates.TemplateResponse("pages/excluirProjeto.html", {"request": request})

@router.get("/avaliacoes", response_class=HTMLResponse)
async def get_avaliacoes(request: Request):
    return templates.TemplateResponse("pages/avaliacoes.html", {"request": request})

@router.get("/visualizarprojeto", response_class=HTMLResponse)
async def get_visualizarProjeto(request: Request):
    return templates.TemplateResponse("pages/visualizarProjeto.html", {"request": request})

@router.get("/ingressarprojeto", response_class=HTMLResponse)
async def get_ingressarProjeto(request: Request):
    return templates.TemplateResponse("pages/ingressarProjeto.html", {"request": request})

@router.get("/bloquearprojeto", response_class=HTMLResponse)
async def get_bloquearProjeto(request: Request):
    return templates.TemplateResponse("pages/bloquearProjeto.html", {"request": request})

@router.get("/assinatura", response_class=HTMLResponse)
async def get_assinatura(request: Request):
    return templates.TemplateResponse("pages/assinatura.html", {"request": request})

@router.get("/criarprojeto", response_class=HTMLResponse)
async def get_criarProjeto(request: Request):
    return templates.TemplateResponse("pages/criarProjeto.html", {"request": request})

@router.get("/doacao", response_class=HTMLResponse)
async def get_doacao(request: Request):
    return templates.TemplateResponse("pages/doacao.html", {"request": request})

@router.get("/modalidadespatrocinio", response_class=HTMLResponse)
async def get_modalidadesPatrocinio(request: Request):
    return templates.TemplateResponse("pages/modalidadesPatrocinio.html", {"request": request})

@router.get("/esquecisenha", response_class=HTMLResponse)
async def get_EsqueciSenha(request: Request):
    return templates.TemplateResponse("pages/esquecisenha.html", {"request": request})

@router.get("/verificaremail", response_class=HTMLResponse)
async def get_EsqueciSenha(request: Request):
    return templates.TemplateResponse("pages/verificaremail.html", {"request": request})






