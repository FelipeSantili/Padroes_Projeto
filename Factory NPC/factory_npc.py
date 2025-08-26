from models import (
    NPC,
    Vendedor,
    Ferreiro,
    Cozinheiro,
)

from enum import Enum

class TipoNPC(Enum):
    Vendedor = "Vendedor"
    Ferreiro = "Ferreiro"
    Cozinheiro = "Cozinheiro"
    
def create_npc(tipo: str, nome: str, itens: list = None) -> NPC:
    if tipo == TipoNPC.Vendedor.value:
        return Vendedor(nome, tipo, itens)
    if tipo == TipoNPC.Ferreiro.value:
        return Ferreiro(nome, tipo, itens)
    if tipo == TipoNPC.Cozinheiro.value:
        return Cozinheiro(nome, tipo, itens)
    else:
        raise Exception(f"{tipo} não existe!")