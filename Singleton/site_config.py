class SiteConfig:
    
    _instance = None
    _initialized = False

    def __init__(self):

        if self._initialized:
            return 
        
        self.counter = 0
        self.titulo = None
        self.idioma = None
        self.email = None
        self._initialized = True

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @staticmethod
    def get_config():
        singleton = SiteConfig()
        singleton.titulo = "teste"
        singleton.idioma = "pt-BR"
        singleton.email = "google@gmail.com"

        return singleton
    
    def add_visitante(self):
        self.counter+=1
        print(self.counter)