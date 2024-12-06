SQL_CRIAR_TABELA_PROJETO = """
CREATE TABLE IF NOT EXISTS "projeto" (
	"id" INTEGER PRIMARY KEY AUTOINCREMENT,
	"nome_projeto" TEXT NOT NULL,
	"qtd_voluntarios" INTEGER NOT NULL,
	"estado" TEXT NOT NULL,
	"municipio"	TEXT NOT NULL,
	"data_inicio" DATE NOT NULL,
	"data_fim" DATE NOT NULL,
	"meta_doacao" INTEGER NOT NULL,
	"descricao" TEXT NOT NULL,
	"endereco" TEXT NOT NULL
)
"""
SQL_INSERIR_PROJETO = """
    INSERT INTO projeto(
        "nome_projeto", 
        "qtd_voluntarios", 
        "estado", 
        "municipio", 
        "data_inicio", 
        "data_fim", 
        "meta_doacao", 
        "descricao", 
        "endereco"
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

SQL_OBTER_PROJETO_POR_ID = """
    SELECT 
        id, 
        "nome_projeto", 
        "qtd_voluntarios", 
        "estado", 
        "municipio", 
        "data_inicio", 
        "data_fim", 
        "meta_doacao", 
        "descricao", 
        "endereco"
    FROM projeto
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE_PROJETOS = """
    SELECT COUNT(*)
    FROM projeto
"""

SQL_NOME_PROJETO_EXISTE = """
    SELECT COUNT(*)
    FROM projeto
    WHERE "nome_projeto"=?
"""

SQL_ATUALIZAR_PROJETO = """
    UPDATE projeto
    SET 
        "nome_projeto" = ?, 
        "qtd_voluntarios" = ?, 
        "estado" = ?, 
        "municipio" = ?, 
        "data_inicio" = ?, 
        "data_fim" = ?, 
        "meta_doacao" = ?, 
        "descricao" = ?, 
        "endereco" = ?
    WHERE id = ?
"""

SQL_EXCLUIR_PROJETO = """
    DELETE FROM projeto
    WHERE id = ?
"""

