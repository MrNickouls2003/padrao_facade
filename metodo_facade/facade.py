from subsistema_banco import BancoDeDados
from subsistema_validador import Validador
from subsistema_email import EnviadorDeEmail

class GerenciadorFacade:
    def __init__(self):
        self.banco = BancoDeDados()
        self.validador = Validador()
        self.email = EnviadorDeEmail()

    def processar_dados(self, dados):
        
        if not self.validador.validar(dados):
            print("Erro: Dados inválidos!")
            return
        self.banco.salvar_dados(dados)
        
        self.email.enviar_email("nicolasaugusto2003@gmail.com", "Seus dados foram processados com sucesso!")
