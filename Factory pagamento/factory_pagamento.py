from models import (
    Pagamento,
    PagamentoBoleto,
    PagamentoCartao,
    PagamentoPix
)
from enum import Enum

class TipoPagamento(Enum):
    Pix = "Pix"
    Boleto = "Boleto"
    Cartao = "Cartao"
    
def create_pagamento(tipo: str, valor: float) -> Pagamento:
    if tipo == "Pix":
        return PagamentoPix(valor)
    if tipo == "Boleto":
        return PagamentoBoleto(valor)
    if tipo == "Cartao":
        return PagamentoCartao(valor) 
    else:
        raise Exception(f"{tipo} não adicionado!")