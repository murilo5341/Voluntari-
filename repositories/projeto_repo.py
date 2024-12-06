from typing import Optional
from models.projeto_model import Projeto
from sql.projeto_sql import *
from util.database import obter_conexao


class ProjetoRepo:
    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as db:
            cursor = db.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @classmethod
    def inserir(cls, projeto: Projeto) -> bool:
            with obter_conexao() as db:
                cursor = db.cursor()
                resultado = cursor.execute(
                    SQL_INSERIR,
                    (
                        projeto.nome_projeto,
                        projeto.qtd_voluntarios,
                        projeto.estado,
                        projeto.municipio,
                        projeto.data_inicio,                        
                        projeto.data_fim,
                        projeto.meta_doacao,
                        projeto.descricao,
                        projeto.endereco,

                    )
                )
                return resultado.rowcount > 0

    @classmethod
    def alterar(cls, projeto: Projeto) -> bool:
            with obter_conexao() as db:
                cursor = db.cursor()
                resultado = cursor.execute(
                    SQL_ATUALIZAR,
                    (
                        projeto.nome_projeto,
                        projeto.data_inicio,
                        projeto.data_fim,
                        projeto.descricao,
                        projeto.id,
                    ),
                )
                return resultado.rowcount > 0


    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Projeto]:
        with obter_conexao() as db:
            cursor = db.cursor()
            dados = cursor.execute(
                SQL_OBTER_POR_ID, (id,)).fetchone()
            if dados:
                return Projeto(*dados)
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
    def excluir_projeto(cls, id: int) -> bool:
        with obter_conexao() as db:
            cursor = db.cursor()
            resultado = cursor.execute(
                SQL_EXCLUIR, (id,))
            return resultado.rowcount > 0    