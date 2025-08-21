from abc import ABC

class Pagamento(ABC):
    def __init__(self, valor: float):
        self.valor = valor

    def status(self) -> None:
        print(f"Valor pago: R$ {self.valor:.2f}")

    def realizar(self):
        pass

class PagamentoPix(Pagamento):
    def realizar(self):
        self.valor = self.valor * 0.90
        print("Pagamento via Pix realizado com sucesso!")
        print(f"Valor do pagamento foi R$ {self.valor:.2f}")

class PagamentoBoleto(Pagamento):
    def realizar(self):
        self.valor = self.valor * 0.95
        print("Pagamento via Boleto realizado com sucesso!")
        print(f"Valor do pagamento foi R$ {self.valor:.2f}")

class PagamentoCartao(Pagamento):   
    def realizar(self):
        self.valor = self.valor * 0.90
        print("Pagamento via Cartão realizado com sucesso!")
        print(f"Valor do pagamento foi R$ {self.valor:.2f}")