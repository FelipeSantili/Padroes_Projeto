from factory_pessoa import create_pessoa, TipoPessoa

if __name__ == "__main__":
    # (SEM FACTORY)
    # Cria a instancia a partir da classe concreta
    # pf = PessoaFisica()
    
    # (COM FACTORY)
    # Obter a instancia chamando o factory
    pf = create_pessoa(TipoPessoa.PF.value, None, 200)
    pj = create_pessoa(TipoPessoa.PJ.value, "Super Dia", 1000)
    
    pf.nome = "Maria"
    print(pf.nome, "-", pf.calculaIR())
    
    print(pj.nome, "-",pj.calculaIR())