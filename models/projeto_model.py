from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Projeto:
    id: Optional[str] = None
    nome_projeto: Optional[str] = None
    qtd_voluntarios: Optional[str] = None
    estado: Optional[str] = None
    municipio: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    meta_doacao: Optional[float] = None
    descricao: Optional[int] = None
    endereco: Optional[int] = None
    
    
