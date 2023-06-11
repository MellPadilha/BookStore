class Venda:
    # Atributos da classe:
    # codigo_venda
    # quantidade
    # livro
    # cliente
    # forma_pagamento
    # status

    def __init__(self, codigo_venda, quantidade, livro, cliente, forma_pagamento, status):
        self.codigo_venda = codigo_venda
        self.quantidade = quantidade
        self.livro = livro
        self.cliente = cliente
        self.forma_pagamento = forma_pagamento
        self.status = status

    @classmethod
    def alterarQuantidade(self, quantidade_atual):
        self.quantidade = quantidade_atual

    @classmethod
    def mudarFormaPagamento(self, forma_pagamento_real):
        self.forma_pagamento = forma_pagamento_real

    @classmethod
    def alterarLivro(self, livroNovo):
       self.livro = livroNovo
    
    @classmethod
    def mudarStatusLivro(self, status):
        self.status = status