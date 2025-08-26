from models import (
    Pessoa ,
    PessoaFisica, 
    PessoaJuridica
)
from enum import Enum

class TipoPessoa(Enum):
    PF = "PF"
    PJ = "PJ"

def create_pessoa(tipo: str, nome: str = None, renda: float = None) -> Pessoa:
    if tipo == "PF":
        return PessoaJuridica(nome, renda)
    if tipo == "PJ":
        return PessoaFisica(nome, renda)
    else:
        # Erro
        raise Exception(f"{tipo} não existe!")
    
    