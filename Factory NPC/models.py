from abc import ABC

class NPC(ABC):
    def __init__(self, nome: str, tipo: str, itens: list = None):
        self.nome = nome
        self.tipo = tipo
        self.itens = itens
        
    def falar_tipo(self):
        pass
    
class Vendedor(NPC):
    def __init__(self, nome, tipo, itens=None):
        super().__init__(nome, tipo, itens)
        
    def falar_tipo(self) -> str:
        frase = f"Olá viajante, eu sou um {self.tipo}, oque você precisa?"
        if self.itens:
            itens_str = ", ".join(self.itens)
            frase += f" Eu tenho os seguintes itens: {itens_str}."
        return frase

class Ferreiro(NPC):
    def __init__(self, nome, tipo, itens=None):
        super().__init__(nome, tipo, itens)
        
    def falar_tipo(self) -> str:
        frase = f"Olá viajante, eu sou um {self.tipo}, gostaria de uma espada?"
        if self.itens:
            itens_str = ", ".join(self.itens)
            frase += f" Eu tenho os seguintes itens: {itens_str}."
        return frase
    
class Cozinheiro(NPC):
    def __init__(self, nome, tipo, itens=None):
        super().__init__(nome, tipo, itens)
        
    def falar_tipo(self) -> str:
        frase = f"Olá viajante, eu sou um {self.tipo}, quer algum lanche para a viagem??"
        if self.itens:
            itens_str = ", ".join(self.itens)
            frase += f" Eu tenho os seguintes lanches: {itens_str}."
        return frase