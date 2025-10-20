from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, lumens: int): ...


class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer: Observer): ...
    @abstractmethod
    @abstractmethod
    def notify(self): ...


class SensorNotifier(Subject):
    def __init__(self):
        self.subscribers = []
        self.lumens = 0

    def subscribe(self, observer: Observer):
        self.subscribers.append(observer)

    def notify(self):
        print("\n> Notificando observadores sobre mudança de luminosidade...")
        for sub in self.subscribers:
            sub.update(self.lumens)

    def set_luminosidade(self, lumens: int):
        self.lumens = lumens
        print(f"\n>>> Luminosidade atual: {lumens} lumens")
        self.notify()


class ObservadorInterno(Observer):
    def __init__(self, nome):
        self.nome = nome

    def update(self, lumens: int):
        if lumens < 100:
            estado = "acendendo todas as lâmpadas internas"
        elif 100 <= lumens <= 300:
            estado = "acendendo metade das lâmpadas internas"
        else:
            estado = "desligando todas as lâmpadas internas"
        print(f"[{self.nome}] {estado} (lumens={lumens})")


class ObservadorExterno(Observer):
    def __init__(self, nome):
        self.nome = nome

    def update(self, lumens: int):
        if lumens <= 50:
            estado = "acendendo todas as lâmpadas externas"
        elif 50 < lumens <= 200:
            estado = "acendendo apenas lâmpadas de LED externas"
        else:
            estado = "desligando todas as lâmpadas externas"
        print(f"[{self.nome}] {estado} (lumens={lumens})")


if __name__ == "__main__":
    sensor = SensorNotifier()

    interno = ObservadorInterno("Área Interna")
    externo = ObservadorExterno("Área Externa")

    sensor.subscribe(interno)
    sensor.subscribe(externo)

    sensor.set_luminosidade(50)
    sensor.set_luminosidade(100)
    sensor.set_luminosidade(300)
    sensor.set_luminosidade(310)
