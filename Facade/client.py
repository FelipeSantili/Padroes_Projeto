from pacotes import PacoteFacade

if __name__ == "__main__":
    """ Interface "terminal" para reserva de pacotes """
    
    pacote = PacoteFacade()
    
    pacote.reservar(
        origem="Foz do Iguaçu",
        destino="Curitiba",
        data="14/02/2026",
        data_entrada="14/02/2026",
        data_saida="24/02/2026"
    )