import dotenv
from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from repositories.usuario_repo import UsuarioRepo
from routes.main_routes import router as main_router
from routes.administrador_routes import router as administrador_router
from routes.voluntario_routes import router as voluntario_router
from routes.moderador_routes import router as moderador_router
from util.auth import checar_autenticacao, checar_autorizacao
from util.exceptions import configurar_excecoes


dotenv.load_dotenv()
UsuarioRepo.criar_tabela()
app = FastAPI(dependencies=[Depends(checar_autorizacao)])
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.middleware("http")(checar_autenticacao)
configurar_excecoes(app)

app.include_router(main_router)
app.include_router(voluntario_router)
app.include_router(administrador_router)
app.include_router(moderador_router)

