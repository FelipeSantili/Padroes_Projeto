class PageViews:
    # Garante que só existe um instancia
    """ Singleton que mantém o contador de acesso """
    _instance = None

    def __init__(self):
        """ Método construtor """
        if not hasattr(self, "counter"):
            self.counter = 0
        
    @staticmethod
    def get_instance():
        """ Ponto de acesso global """
        return PageViews()
        
    def add_visiter(self):
        """ incrementa contador de visitantes """
        self.counter += 1
        print(self.counter)

    def __new__(cls): # csl == PageViews
        """ Sobrescreve o método __new__ """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# A própria classe fica responsavel pela sua instancia

if __name__ == "__main__":
    page = PageViews() # page = PageViews.__init__()
    page.add_visiter()
    page.add_visiter()
    
    page2 = PageViews()
    page2.add_visiter()
    
    page3 = PageViews()
    page3.add_visiter()
    
    page4 = PageViews()
    page4.add_visiter()
    
    page5 = PageViews()
    page5.add_visiter()
    
    print(id(page)) # Endereço de memória
    print(id(page2)) 