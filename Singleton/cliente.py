from site_config import SiteConfig

if __name__ == "__main__":
    
    config1 = SiteConfig.get_config()
    config1.add_visitante()
    print(f"Configuração 1: {config1.titulo}")