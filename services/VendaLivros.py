from models import Vendedor, Livro, Venda, Cliente

class VendaLivros:

    def cadastrarNovaVenda(self, codigo_venda, quantidade, livro, pessoa, forma_pagamento, status):
        Venda(codigo_venda, quantidade, livro, pessoa, forma_pagamento, status)

    def realizerDevolucao(self, status):
        Venda.mudarStatusLivro(status)

    def vendaComCupom(self, codigo_cupom):
        Livro.aplicarDesconto(codigo_cupom)

