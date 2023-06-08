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

    def lancarNovaVersao():
        return True

    def aplicarDesconto(self, pencentual):
        self.preco_desconto = self.preco / (pencentual / 100)

    def verificarEstoque(self):
        return self.quantidade