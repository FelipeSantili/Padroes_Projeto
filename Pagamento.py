from abc import ABC, abstractmethod
class Pagamento(ABC):
    def __init__(self, valor: float):
        self.valor = valor
        
    def status(self) -> str:
        print(f"Valor pago: R$ {self.valor:.2f}")
        
    @abstractmethod
    def realizar(self):
        pass
        
class PagamentoPix(Pagamento):
    def realizar(self):
        self.valor = self.valor + 10
        print("Pagamento via Pix realizado com sucesso!")     

class PagamentoBoleto(Pagamento):
    def realizar(self):
        self.valor = self.valor * 1.12
        print("Pagamento via Boleto realizado com sucesso!")
        
class PagamentoCartao(Pagamento):
    def realizar(self):
        self.valor = self.valor * 1.15
        print("Pagamento via Cartão realizado com sucesso!")


if __name__ == "__main__":
    valor = 100
    
    forma_pagamento = int(input("Escolha a forma de pagamento (1 - Pix, 2 - Boleto, 3 - Cartão): "))

    if forma_pagamento == 1:
        pagamento = PagamentoPix(valor)
    elif forma_pagamento == 2:
        pagamento = PagamentoBoleto(valor)
    elif forma_pagamento == 3:
        pagamento = PagamentoCartao(valor)
    else:
        print("Forma de pagamento inválida.")
        exit()

    pagamento.realizar()
    pagamento.status()
