from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from repositories.usuario_repo import UsuarioRepo
from routes import administrador_routes, main_routes, voluntario_routes
from routes import moderador_routes
from util.auth import checar_permissao, middleware_autenticacao
from util.exceptions import configurar_excecoes

UsuarioRepo.criar_tabela()
app = FastAPI(dependencies=[Depends(checar_permissao)])
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.middleware(middleware_type="http")(middleware_autenticacao)
configurar_excecoes(app)
app.include_router(main_routes.router)
app.include_router(moderador_routes.router)
app.include_router(administrador_routes.router)
app.include_router(voluntario_routes.router)