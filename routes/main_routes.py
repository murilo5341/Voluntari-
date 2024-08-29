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

@router.get("/sobre", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/sobre.html", {"request": request})

@router.get("/denuncia-projeto", response_class=HTMLResponse)
async def get_denunciaProjeto(request: Request):
    return templates.TemplateResponse("pages/denunciaProjeto.html", {"request": request})

@router.get("/excluir-projeto", response_class=HTMLResponse)
async def get_excluirProjeto(request: Request):
    return templates.TemplateResponse("pages/excluirProjeto.html", {"request": request})




