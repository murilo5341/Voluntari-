SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        data_nascimento DATE NOT NULL,
        telefone TEXT NOT NULL,
        perfil INT NOT NULL)
"""

SQL_INSERIR = """
    INSERT INTO usuario(id, nome, email, senha, data_nascimento, telefone, perfil)
    VALUES (?, ?, ?)
"""

SQL_EXCLUIR = """
    DELETE FROM usuario    
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, email, senha, data_nascimento, telefone, perfil
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
    SELECT nome, email, perfil, senha
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