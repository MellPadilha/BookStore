class Livro:
    # Atributos da classe:
    # nome
    # quantidade
    # autor
    # descricao
    # preco
    # preco_desconto

    def __init__(self, nome, quantidade, autor, descricao, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.quantidade = quantidade
        self.autor = autor
        self.descricao = descricao
        self.preco = preco

    @classmethod
    def lancarNovaVersao():
        return True

    @classmethod
    def aplicarDesconto(self, percentual):
        self.preco_desconto = percentual / 100

    @classmethod
    def verificarEstoque(self):
        return self.quantidade