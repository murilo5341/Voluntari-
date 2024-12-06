from typing import Optional
from models.usuario_model import Usuario
from sql.usuario_sql import *
from util.auth import conferir_senha
from util.database import obter_conexao


class UsuarioRepo:
    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @classmethod
    def inserir(cls, usuario: Usuario) -> bool:
            with obter_conexao() as db:
                cursor = db.cursor()
                resultado = cursor.execute(
                    SQL_INSERIR_USUARIO,
                    (
                        usuario.nome,
                        usuario.email,
                        usuario.senha,
                        usuario.cpf,
                        usuario.data_nascimento,                        
                        usuario.telefone,
                        usuario.perfil,
                    )
                )
                return resultado.rowcount > 0

    @classmethod
    def alterar(cls, usuario: Usuario) -> bool:
            with obter_conexao() as db:
                cursor = db.cursor()
                resultado = cursor.execute(
                    SQL_ATUALIZAR_DADOS,
                    (
                        usuario.nome,
                        usuario.email,
                        usuario.data_nascimento,
                        usuario.telefone,
                        usuario.id,
                    ),
                )
                return resultado.rowcount > 0

    @staticmethod
    def obter_senha_por_email(email: str) -> Optional[str]:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_OBTER_SENHA_POR_EMAIL, (email,))
            dados = cursor.fetchone()
            if dados is None:
                return None
            return dados[0]

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Usuario]:
        with obter_conexao() as db:
            cursor = db.cursor()
            dados = cursor.execute(
                SQL_OBTER_POR_ID, (id,)).fetchone()
            if dados:
                return Usuario(*dados)
            return None

    # @classmethod
    # def obter_quantidade(cls) -> int:
    #     try:
    #         with obter_conexao() as conexao:
    #             cursor = conexao.cursor()
    #             tupla = cursor.execute(
    #                 SQL_OBTER_QUANTIDADE).fetchone()



    # @classmethod
    # def email_existe(cls, email: str) -> bool:
    #     try:
    #         with obter_conexao() as conexao:
    #             cursor = conexao.cursor()
    #             tupla = cursor.execute(SQL_EMAIL_EXISTE, (email,)).fetchone()
    #             return tupla[0] > 0
    #     except sqlite3.Error as ex:
    #         print(ex)
    #         return False
        
          
    @classmethod
    def checar_credenciais(cls, email: str, senha: str) -> Optional[tuple]:
        with obter_conexao() as db:
            cursor = db.cursor()
            dados = cursor.execute(
                SQL_CHECAR_CREDENCIAIS, (email,)).fetchone()
            if dados:
                if conferir_senha(senha, dados[3]):
                    return (dados[0], dados[1], dados[2], dados[4])
            return None
    
    @staticmethod
    def atualizar_senha(id: int, senha: str) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_ATUALIZAR_SENHA, (senha, id))
            return cursor.rowcount > 0
        
    @classmethod
    def excluir_usuario(cls, id: int) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            resultado = cursor.execute(
                SQL_EXCLUIR_USUARIO, (id,))
            return resultado.rowcount > 0    