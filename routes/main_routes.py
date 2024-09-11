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

@router.get("/cadastrarpatrocinador", response_class=HTMLResponse)
async def get_cadastrarPatrocinador(request: Request):
    return templates.TemplateResponse("pages/cadastrarPatrocinador.html", {"request": request})

@router.get("/exibirmoderador", response_class=HTMLResponse)
async def get_exibirModerador(request: Request):
    return templates.TemplateResponse("pages/exibirModerador.html", {"request": request})
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





