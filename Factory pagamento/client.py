from factory_pagamento import (
    create_pagamento, 
    TipoPagamento
)

if __name__ == "__main__":
    pix = create_pagamento(TipoPagamento.Pix.value, 200)
    boleto = create_pagamento(TipoPagamento.Boleto.value, 200)
    cartao = create_pagamento(TipoPagamento.Cartao.value, 200)
    
    pix.realizar()
    boleto.realizar()
    cartao.realizar()