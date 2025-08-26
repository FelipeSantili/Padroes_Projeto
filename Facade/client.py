from pacotes import PacoteFacade, PacoteAlimentacao

if __name__ == "__main__":
    """ Interface "terminal" para reserva de pacotes """
    
    pacote = PacoteFacade()
    pacoteAlimentacao = PacoteFacade()
    
    input("Escolha 1 ou 2")
    
    pacote.reservar(
        origem="Foz do Iguaçu",
        destino="Curitiba",
        data="14/02/2026",
        data_entrada="14/02/2026",
        data_saida="24/02/2026",
        alimentacao=True,
        local="Restaurante Velho Madaloso",
        guia=True
    )
    
    pacoteAlimentacao.reservar(
        origem="Foz do Iguaçu",
        destino="Curitiba",
        data="14/02/2026",
        data_entrada="14/02/2026",
        data_saida="24/02/2026",
        alimentacao=True,
        local="Restaurante Velho Madaloso",
    )