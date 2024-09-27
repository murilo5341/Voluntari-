from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Usuario:
    id: Optional[str] = None
    nome: Optional[str] = None
    email: Optional[str] = None
    senha: Optional[str] = None
    cpf: Optional[str] = None
    data_nascimento: Optional[date] = None
    telefone: Optional[str] = None
    perfil: Optional[int] = None
    
    
