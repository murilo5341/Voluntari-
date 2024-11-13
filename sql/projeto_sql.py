SQL_CRIAR_TABELA_PROJETO = """
CREATE TABLE IF NOT EXISTS "projeto" (
	"id" INTEGER PRIMARY KEY AUTOINCREMENT,
	"nome do projeto" TEXT NOT NULL,
	"qtd_voluntarios" INTEGER NOT NULL,
	"Estado" TEXT NOT NULL,
	"Municipio"	TEXT NOT NULL,
	"Data_inicio" DATE NOT NULL,
	"Data_fim" DATE NOT NULL,
	"meta_doacao" INTEGER NOT NULL,
	"descricao" TEXT NOT NULL,
	"endereco" TEXT NOT NULL
)
"""

