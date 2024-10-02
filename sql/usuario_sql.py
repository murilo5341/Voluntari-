SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        cpf TEXT NOT NULL ,
        data_nascimento DATE NOT NULL,
        telefone TEXT NOT NULL UNIQUE,
        perfil INT NOT NULL)
"""

SQL_INSERIR_USUARIO = """
    INSERT INTO usuario(nome, email, senha, cpf, data_nascimento, telefone, perfil)
    VALUES (?, ?, ?, ?, ?, ?, ?)
"""


SQL_OBTER_POR_ID = """
    SELECT id, nome, email, senha, cpf, data_nascimento, telefone, perfil
    FROM usuario
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*)
    FROM usuario
"""

SQL_EMAIL_EXISTE = """
    SELECT COUNT(*)
    FROM usuario
    WHERE email=?
"""

SQL_CHECAR_CREDENCIAIS = """
    SELECT nome, email, senha, perfil
    FROM usuario
    WHERE email = ?
"""

SQL_ATUALIZAR_DADOS = """
    UPDATE usuario
    SET nome = ?, email = ?, telefone = ?
    WHERE email = ?
"""
SQL_ATUALIZAR_SENHA = """
    UPDATE usuario
    SET senha = ?
    WHERE email = ?
"""
SQL_EXCLUIR_USUARIO = """
    DELETE FROM usuario
    WHERE email = ?
"""