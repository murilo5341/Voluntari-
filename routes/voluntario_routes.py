from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from repositories.usuario_repo import UsuarioRepo
from util.templates import obter_jinja_templates

router = APIRouter(prefix="/voluntario")
templates = obter_jinja_templates("templates")

@router.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    usuario = UsuarioRepo.obter_por_id(request.state.usuario.id)
    return templates.TemplateResponse("voluntario/pages/index.html", {"request": request, "usuario": usuario})

@router.get("/voluntarioassinante", response_class=HTMLResponse)
async def get_voluntarioassinante(request: Request):
    return templates.TemplateResponse("voluntario/pages/voluntarioassinante.html", {"request": request})


@router.get("/desativarconta", response_class=HTMLResponse)
async def get_desativarconta(request: Request):
    return templates.TemplateResponse("voluntario/pages/desativarconta.html", {"request": request})

@router.get("/avaliacoes", response_class=HTMLResponse)
async def get_avaliacoes(request: Request):
    return templates.TemplateResponse("voluntario/pages/avaliacoes.html", {"request": request})

@router.get("/ingressarprojeto", response_class=HTMLResponse)
async def get_ingressarProjeto(request: Request):
    return templates.TemplateResponse("voluntario/pages/ingressarProjeto.html", {"request": request})

@router.get("/criarprojeto", response_class=HTMLResponse)
async def get_criarProjeto(request: Request):
    return templates.TemplateResponse("voluntario/pages/criarProjeto.html", {"request": request})

@router.get("/doacao", response_class=HTMLResponse)
async def get_doacao(request: Request):
    return templates.TemplateResponse("voluntario/pages/doacao.html", {"request": request})

@router.get("/excluirprojeto", response_class=HTMLResponse)
async def get_excluirProjeto(request: Request):
    return templates.TemplateResponse("voluntario/pages/excluirProjeto.html", {"request": request})

@router.get("/projetosingressados", response_class=HTMLResponse)
async def get_projetosIngressados(request: Request):
    return templates.TemplateResponse("voluntario/pages/projetosingressados.html", {"request": request})

@router.get("/membrosprojeto", response_class=HTMLResponse)
async def get_membrosProjeto(request: Request):
    return templates.TemplateResponse("voluntario/pages/membrosProjeto.html", {"request": request})

@router.get("/solicitarmoderacao", response_class=HTMLResponse)
async def get_solicitarmoderacao(request: Request):
    return templates.TemplateResponse("voluntario/pages/solicitacaoModeracao.html", {"request": request})

@router.get("/notificacaovoluntario", response_class=HTMLResponse)
async def get_notificacaovoluntario(request: Request):
    return templates.TemplateResponse("voluntario/pages/notificacaoVoluntario.html", {"request": request})

@router.get("/alterarsenha", response_class=HTMLResponse)
async def get_alterarsenha(request: Request):
    return templates.TemplateResponse("voluntario/pages/alterarsenha.html", {"request": request})

@router.get("/projetoscriados", response_class=HTMLResponse)
async def get_projetoscriados(request: Request):
    return templates.TemplateResponse("voluntario/pages/projetoscriados.html", {"request": request})

@router.get("/assinatura", response_class=HTMLResponse)
async def get_assinatura(request: Request):
    return templates.TemplateResponse("voluntario/pages/assinatura.html", {"request": request})

@router.get("/projetoscriados", response_class=HTMLResponse)
async def get_projetoscriados(request: Request):
    return templates.TemplateResponse("voluntario/pages/projetoscriados.html", {"request": request})

@router.get("/compartilharprojeto", response_class=HTMLResponse)
async def get_compartilhar(request: Request):
    return templates.TemplateResponse("voluntario/pages/compartilhar.html", {"request": request})

@router.get("/projetosfinalizados", response_class=HTMLResponse)
async def get_projetosfinalizados(request: Request):
    return templates.TemplateResponse("voluntario/pages/projetosfinalizados.html", {"request": request})

@router.get("/doacoesfeitas", response_class=HTMLResponse)
async def get_doacoesfeitas(request: Request):
    return templates.TemplateResponse("voluntario/pages/doacoesfeitas.html", {"request": request})

@router.get("/assinarPlanoAnual", response_class=HTMLResponse)
async def get_assinarPlanoAnual(request: Request):
    return templates.TemplateResponse("voluntario/pages/assinarPlanoAnual.html", {"request": request})

@router.get("/PagamentoCreditoAnual", response_class=HTMLResponse)
async def get_pagamentoCreditoAnual(request: Request):
    return templates.TemplateResponse("voluntario/pages/pagamentoCreditoAnual.html", {"request": request})

@router.get("/PagamentoCreditoMensal", response_class=HTMLResponse)
async def get_pagamentoCreditoMensal(request: Request):
    return templates.TemplateResponse("voluntario/pages/pagamentoCreditoMensal.html", {"request": request})

@router.get("/PagamentoPixAnual", response_class=HTMLResponse)
async def get_pagamentoPixAnual(request: Request):
    return templates.TemplateResponse("voluntario/pages/pagamentoPixAnual.html", {"request": request})

@router.get("/PagamentoPixMensal", response_class=HTMLResponse)
async def get_pagamentoPixMensal(request: Request):
    return templates.TemplateResponse("voluntario/pages/pagamentoPixMensal.html", {"request": request})

@router.get("/assinarPlanoMensal", response_class=HTMLResponse)
async def get_assinarPlanoMensal(request: Request):
    return templates.TemplateResponse("voluntario/pages/assinarPlanoMensal.html", {"request": request})

@router.get("/confPagamentoAnual", response_class=HTMLResponse)
async def get_confPagamentoAnual(request: Request):
    return templates.TemplateResponse("voluntario/pages/confPagamentoAnual.html", {"request": request})

@router.get("/confPagamentoMensal", response_class=HTMLResponse)
async def get_confPagamentoMensal(request: Request):
    return templates.TemplateResponse("voluntario/pages/confPagamentoMensal.html", {"request": request})

@router.get("/pagamentoAprovado", response_class=HTMLResponse)
async def get_pagamentoAprovado(request: Request):
    return templates.TemplateResponse("voluntario/pages/pagamentoAprovado.html", {"request": request})

@router.get("/pagamentoPixAprovado", response_class=HTMLResponse)
async def get_pagamentoPixAprovado(request: Request):
    return templates.TemplateResponse("voluntario/pages/pagamentoPixAprovado.html", {"request": request})

@router.get("/doarProjeto", response_class=HTMLResponse)
async def get_doarProjeto(request: Request):
    return templates.TemplateResponse("voluntario/pages/doarProjeto.html", {"request": request})

@router.get("/cartaodoarProjeto", response_class=HTMLResponse)
async def get_cartaodoarProjeto(request: Request):
    return templates.TemplateResponse("voluntario/pages/cartaodoarProjeto.html", {"request": request})

@router.get("/confdoacaoCartao", response_class=HTMLResponse)
async def get_confdoacaoCartao(request: Request):
    return templates.TemplateResponse("voluntario/pages/confdoacaoCartao.html", {"request": request})

@router.get("/pixdoarProjeto", response_class=HTMLResponse)
async def get_pixdoarProjeto(request: Request):
    return templates.TemplateResponse("voluntario/pages/pixdoarProjeto.html", {"request": request})


@router.get("/doacaoRealizada", response_class=HTMLResponse)
async def get_doacaoRealizada(request: Request):
    return templates.TemplateResponse("voluntario/pages/doacaoRealizada.html", {"request": request})