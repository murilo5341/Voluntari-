from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from repositories.usuario_repo import UsuarioRepo
from routes import main_routes
from util.auth import checar_permissao, middleware_autenticacao
from util.exceptions import configurar_excecoes
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

UsuarioRepo.criar_tabela()
app = FastAPI(dependencies=[Depends(checar_permissao)])
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.middleware(middleware_type="http")(middleware_autenticacao)
configurar_excecoes(app)
app.include_router(main_routes.router)

app = FastAPI()
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def get_root(request: Request):
    view_model = {
        "request": request
    }
    return templates.TemplateResponse("/index.html", view_model)
