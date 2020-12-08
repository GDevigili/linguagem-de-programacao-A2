

class ExcecaoVazio(Exception):
    """Excecao para quando o banco voltar valor vazio

    Attributes:
        retorno -- retorno do banco
        message -- explicacao do erro
    """

    def __init__(self, retorno, message="Retorno Vazio"):
        self.retorno = retorno
        self.message = message
        super().__init__(self.message)