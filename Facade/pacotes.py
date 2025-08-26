from aereo import ReservaVoo
from hotels import ReservaHotel
from transporte import ReservaTransporte
from alimentacao import ReservaAlimentacao
from guia_turistico import ReservaGuia

class PacoteFacade:
    def __init__(self):
        self.aereo = ReservaVoo()
        self.hotel = ReservaHotel()
        self.transporte = ReservaTransporte()
        self.alimentacao = ReservaAlimentacao()
        self.guia = ReservaGuia()

    def reservar(self, origem, destino, data, data_entrada, data_saida, alimentacao: bool = None, local = None, guia: bool = None):
        self.aereo.reservar_voo(origem, destino, data)
        self.hotel.reservar_hotel(destino, data_entrada, data_saida)
        self.transporte.reservar_transporte(destino, data)
        if(alimentacao):
            self.alimentacao.reservar_alimentacao(data, local)
        if(guia):
            self.guia.reservar_guia(origem, destino, data)
    
class PacoteAlimentacao:
    def __init__(self):
        self.aereo = ReservaVoo()
        self.hotel = ReservaHotel()
        self.transporte = ReservaTransporte()
        self.alimentacao = ReservaAlimentacao()
        self.guia = ReservaGuia()

    def reservar(self, origem, destino, data, data_entrada, data_saida, alimentacao: bool = None, local = None, guia: bool = None):
        self.aereo.reservar_voo(origem, destino, data)
        self.hotel.reservar_hotel(destino, data_entrada, data_saida)
        self.transporte.reservar_transporte(destino, data)
        self.alimentacao.reservar_alimentacao(data, local)
