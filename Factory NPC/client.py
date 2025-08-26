from factory_npc import (
    create_npc,
    TipoNPC
)

if __name__ == "__main__":
    
    vendedor = create_npc(TipoNPC.Vendedor.value, "Jerry Cat", 
        ["Botas", "Túnica", "Armadura", "Poção de vida", "Bolsa maior"]
        )
    
    ferreiro = create_npc(TipoNPC.Ferreiro.value, "Clark Kent",
        ["Machado", "Espada", "Cajado", "Escudo", "Arco-Flecha"])
    
    cozinheiro = create_npc(TipoNPC.Cozinheiro.value, "Érick Jacquin")
    
    print(vendedor.falar_tipo())
    print(ferreiro.falar_tipo())
    print(cozinheiro.falar_tipo())