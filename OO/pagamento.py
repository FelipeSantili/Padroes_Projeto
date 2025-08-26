from abc import ABC, abstractmethod
class Pagamento(ABC):
    def __init__(self, valor: float): # Construtor
        # Declarado e inicializado no construtor
        self.valor = valor # Atributo
        
    def status(self) -> str: # Método concreto
        print(f"Valor pago: R$ {self.valor:.2f}")
        
    @abstractmethod # Método abstrato
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
    
    forma_pagamento = input("Escolha a forma de pagamento (1 - Pix, 2 - Boleto, 3 - Cartão): ")

    if forma_pagamento == 1:
        # Tipo - PamentoPix
        pagamento = PagamentoPix(valor)
    elif forma_pagamento == 2:
        # Tipo - PagamentoBoleto
        pagamento = PagamentoBoleto(valor)
    elif forma_pagamento == 3:
        # Tipo - PagamentoCartao
        pagamento = PagamentoCartao(valor)
    else:
        print("Forma de pagamento inválida.")
        exit()

    # pagamento - Objeto | realizar() - Método 
    pagamento.realizar()
    pagamento.status()
    
# Vocabulário:
# - classe abstrata (ABC)
# - construtor (__init__)
# - self
# - atributo
# - métodos
# - @abstractmethod
# - objeto (p)
# - classe concreta
# - herança
# - super() - Chama o controtutor da classe

