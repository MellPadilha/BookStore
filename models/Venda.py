class Venda:
    # Atributos da classe:
    # codigo_venda
    # quantidade
    # livro
    # pessoa
    # forma_pagamento
    # status

    def __init__(self, codigo_venda, quantidade, livro, pessoa, forma_pagamento, status):
        self.codigo_venda = codigo_venda
        self.quantidade = quantidade
        self.livro = livro
        self.pessoa = pessoa
        self.forma_pagamento = forma_pagamento
        self.status = status

    def alterarQuantidade(self, quantidade_atual):
        self.quantidade = quantidade_atual

    def mudarFormaPagamento(self, forma_pagamento_real):
        self.forma_pagamento = forma_pagamento_real

    def alterarLivro(self, livroNovo):
       self.livro = livroNovo

    def mudarStatusLivro(self, status):
        self.status = status