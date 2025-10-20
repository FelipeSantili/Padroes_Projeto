from abc import ABC, abstractmethod

class Observer(ABC): 
    """ Quem esta interessado em ser notificado """
    @abstractmethod
    def update(self, item=None, preco=None): ...

class Subject(ABC):
    """ Aquele que notifica """
    @abstractmethod
    def subscribe(self, observer: Observer): ...
    @abstractmethod
    def cancel(self, observer: Observer): ...
    @abstractmethod
    def notify(self, item=None, preco=None): ...

class Estoque(Subject): 
    def __init__(self): 
        self.subscribers = [] # lista de inscritos
        self.items = []

    def subscribe(self, observer: Observer): 
        self.subscribers.append(observer)

    def cancel(self, observer: Observer):
        if observer in self.subscribers:
            self.subscribers.remove(observer)
    
    def notify(self, item=None, preco=None):
        """ Disparo da notificação """
        print(f"> Notificando inscritos pelo item {item} (R$ {preco})")
        for sub in list(self.subscribers):
            sub.update(item, preco)

    def new_item(self, item: str, preco: float):
        """ Ocorrência do evento de chegada de um item """
        print(f"\nProduto '{item}' chegou no estoque por R$ {preco}")
        self.items.append((item, preco))
        self.notify(item, preco)

class Cliente(Observer):
    def __init__(self, nome, preco_max=None, continuar=False):
        self.nome = nome
        self.subject = None
        self.item = None
        self.preco_max = preco_max
        self.continuar = continuar

    def add_item(self, item, subject: Subject):
        """ Inscrição para ser notificado sobre um produto """
        self.item = item
        self.subject = subject
        self.subject.subscribe(self)

    def update(self, item, preco):
        """ O que o cliente faz ao ser notificado """
        if self.item == item:
            if self.preco_max is None or preco <= self.preco_max:
                print(f"{self.nome} notificado: {item} disponível por R$ {preco}")
                if not self.continuar:
                    self.subject.cancel(self)

class Fornecedor(Observer):
    def __init__(self, nome):
        self.nome = nome

    def update(self, item, preco):
        print(f"Fornecedor {self.nome} notificado: {item} foi recebido no estoque (R$ {preco})")

if __name__ == "__main__":
    estoque = Estoque()

    # Fornecedor sempre notificado
    fornecedor = Fornecedor("TechParts")
    estoque.subscribe(fornecedor)

    # Cliente que só quer ser notificado até ser avisado 1 vez
    maria = Cliente("Maria", preco_max = 1200, continuar = False)
    maria.add_item("Phone A2", estoque)

    # Cliente que quer continuar recebendo
    joao = Cliente("João", continuar = True)
    joao.add_item("Phone A2", estoque)

    # Simulação de novos produtos
    estoque.new_item("Phone A2", 1500)
    estoque.new_item("Phone A2", 1100)
