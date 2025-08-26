from abc import ABC
class Pessoa(ABC):
    def __init__(self, nome: str, renda: float):
        self.nome = nome
        self.renda = renda

    def calculaIR(self) -> float:
        pass

class PessoaFisica(Pessoa):

    def __init__(self, nome: str = None, renda: float = None, cpf: str = None):
        super().__init__(nome, renda)
        self.cpf = cpf

    def calculaIR(self) -> float:
        return self.renda * 0.25

class PessoaJuridica(Pessoa):
    def __init__(self, nome: str = None, renda: float = None, cnpj: str = None, ie: int = None):
        super().__init__(nome, renda)
        self.cnpj = cnpj

    def calculaIR(self) -> float:
        return self.renda * 0.18
