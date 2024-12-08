from facade import GerenciadorFacade

if __name__ == "__main__":
    gerenciador = GerenciadorFacade()
    dados = "Informações importantes"
    gerenciador.processar_dados(dados)
