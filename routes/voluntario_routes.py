from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/voluntario")
templates = obter_jinja_templates("templates/voluntario")


@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

@router.get("/assinaturadousuarioassinante", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/assinaturadousuarioassinante.html", {"request": request})

@router.get("/desativarconta", response_class=HTMLResponse)
async def get_termos(request: Request):
    return templates.TemplateResponse("pages/desativarconta.html", {"request": request})

@router.get("/avaliacoes", response_class=HTMLResponse)
async def get_avaliacoes(request: Request):
    return templates.TemplateResponse("pages/avaliacoes.html", {"request": request})

@router.get("/ingressarprojeto", response_class=HTMLResponse)
async def get_ingressarProjeto(request: Request):
    return templates.TemplateResponse("pages/ingressarProjeto.html", {"request": request})

@router.get("/assinatura", response_class=HTMLResponse)
async def get_assinatura(request: Request):
    return templates.TemplateResponse("pages/assinatura.html", {"request": request})

@router.get("/criarprojeto", response_class=HTMLResponse)
async def get_criarProjeto(request: Request):
    return templates.TemplateResponse("pages/criarProjeto.html", {"request": request})

@router.get("/doacao", response_class=HTMLResponse)
async def get_doacao(request: Request):
    return templates.TemplateResponse("pages/doacao.html", {"request": request})

@router.get("/excluirprojeto", response_class=HTMLResponse)
async def get_excluirProjeto(request: Request):
    return templates.TemplateResponse("pages/excluirProjeto.html", {"request": request})
