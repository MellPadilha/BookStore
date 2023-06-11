from models.Venda import Venda
from models.Livro import Livro

class VendaLivros:

    @classmethod
    def cadastrarNovaVenda(self, codigo_venda, quantidade, livro, cliente, forma_pagamento, status):
        Venda(codigo_venda, quantidade, livro, cliente, forma_pagamento, status)

    @classmethod
    def realizarDevolucao(self, status):
        Venda.mudarStatusLivro(status)

    @classmethod
    def vendaComCupom(self, percentual):
        Livro.aplicarDesconto(percentual)

