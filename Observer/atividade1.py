from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, item=None, preco=None): ...

class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer: Observer): ...
    @abstractmethod
    def cancel(self, observer: Observer): ...
    @abstractmethod
    def notify(self, item=None, preco=None): ...

class Estoque(Subject):
    def __init__(self):
        self.subscribers = []
        self.items = []
        self.precos = {}

    def subscribe(self, observer: Observer):
        self.subscribers.append(observer)

    def cancel(self, observer: Observer):
        if observer in self.subscribers:
            self.subscribers.remove(observer)

    def notify(self, item=None, preco=None):
        print("> notificando inscritos")
        for sub in list(self.subscribers):
            sub.update(item=item, preco=preco)

    def new_item(self, item: str, preco: float):
        print(f"> {item} chegou no estoque por R${preco}")
        self.items.append(item)
        self.precos[item] = preco
        self.notify(item=item, preco=preco)

class Fornecedor(Observer):
    def __init__(self, nome):
        self.nome = nome

    def update(self, item=None, preco=None):
        print(f"Fornecedor {self.nome} notificado: {item} recebido no estoque (R${preco})")

class Cliente(Observer):
    def __init__(self, nome, continuar=False, preco_max=None):
        self.nome = nome
        self.subject = None
        self.item = None
        self.continuar = continuar
        self.preco_max = preco_max

    def add_item(self, item, subject: Subject):
        self.item = item
        self.subject = subject
        self.subject.subscribe(self)

    def update(self, item=None, preco=None):
        if self.item == item:
            if self.preco_max is not None and preco > self.preco_max:
                print(f"Usuário {self.nome} ignorou {item} (R${preco} > {self.preco_max})")
                return

            print(f"Usuário {self.nome} notificado: {item} disponível por R${preco}")
            if not self.continuar:
                self.subject.cancel(self)

if __name__ == "__main__":
    estoque = Estoque()

    maria = Cliente("Maria", continuar=False, preco_max=1200)
    maria.add_item("Phone A2", estoque)

    joao = Cliente("João", continuar=True)
    joao.add_item("Phone A2", estoque)

    fornecedor = Fornecedor("Casa China")
    estoque.subscribe(fornecedor)

    estoque.new_item("Phone A2", 1300)
    estoque.new_item("Phone A2", 1100)
    estoque.new_item("Phone A8", 900)
