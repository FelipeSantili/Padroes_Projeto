from aereo import ReservaVoo
from hotels import ReservaHotel
from transporte import ReservaTransporte

class PacoteFacade:
    def __init__(self):
        self.aereo = ReservaVoo()
        self.hotel = ReservaHotel()
        self.transporte = ReservaTransporte()

    def reservar(self, origem, destino, data, data_entrada, data_saida):
        self.aereo.reservar_voo(origem, destino, data)
        self.hotel.reservar_hotel(destino, data_entrada, data_saida)
        self.transporte.reservar_transporte(destino, data)