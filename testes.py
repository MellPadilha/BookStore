import unittest
from models.Venda import Venda
from models.Cliente import Cliente
from models.Livro import Livro
from models.Fornecedor import Fornecedor
from services.VendaLivros import VendaLivros
from services.GerenciamentoFornecedor import GerenciamentoFornecedor
from services.GerenciamentoVendedores import GerenciamentoVendedores

class Test(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

class TestVendaLivros(unittest.TestCase):

    def setUp(self):
        self.venda_livros = VendaLivros()

    def test_cadastrarNovaVenda(self):
        codigo_venda = 1
        quantidade = 2
        livro = Livro("Livro A", 10, "Autor A", "Descrição A", 50.0)
        cliente = Cliente("João", "Silva", "jão", "09/03/2002", "Rua A", "123456789")
        forma_pagamento = "Cartão de Crédito"
        status = "Pendente"

        self.venda_livros.cadastrarNovaVenda(codigo_venda, quantidade, livro, cliente, forma_pagamento, status)

        print("Venda registrada com sucesso!")

    def test_realizarDevolucao(self):
        codigo_venda = 1
        quantidade = 2
        livro = Livro("Livro A", 10, "Autor A", "Descrição A", 50.0)
        cliente = Cliente("João", "Silva", "jão", "09/03/2002", "Rua A", "123456789")
        forma_pagamento = "Cartão de Crédito"
        status = "Pendente"
        venda = Venda(codigo_venda, quantidade, livro, cliente, forma_pagamento, status)

        novo_status = "Devolvido"
        self.venda_livros.realizarDevolucao(novo_status)

        print("Livro devolvido com sucesso!")

    def test_vendaComCupom(self):
        percentual_cupom = 20
        livro = Livro("Livro A", 10, "Autor A", "Descrição A", 50.0)

        self.venda_livros.vendaComCupom(percentual_cupom)

        print("Cupom aplicado!")

class TestGerenciamentoVendedores(unittest.TestCase):

    def setUp(self):
        self.gerenciamento = GerenciamentoVendedores()

    def test_cadastrarNovoVendedor(self):
        self.gerenciamento.cadastrarNovoVendedor("João", 452, 0, 25, 5000, "Intermediário", 5000)
        print('Vendedor cadastrado')

    def test_pagarComissao(self):
        self.gerenciamento.cadastrarNovoVendedor("João", 452, 0, 25, 5000, "Iniciante", 2000)
        self.gerenciamento.pagarComissao(50, 5000)
        print('Pagamento com comissão realizado!')

    def test_calcularFerias(self):
        tempo_de_ferias = self.gerenciamento.calcularFerias(100)
        print("Tempo de ferias:", tempo_de_ferias)

class TestGerenciamentoFornecedor(unittest.TestCase):
    def setUp(self):
        self.gerenciamento = GerenciamentoFornecedor()

    def test_cadastrarNovoFornecedor(self):
        nome = "Fornecedor 1"
        tipo_de_fornecedor = "Livros"
        tempo_de_contrato = 12
        endereco = "Rua A, 123"
        pagamento = 5000
        tempo_de_producao = 3

        self.gerenciamento.cadastrarNovoFornecedor(nome, tipo_de_fornecedor, tempo_de_contrato, endereco, pagamento, tempo_de_producao)
        print("Fornecedor cadastrado!")

    def test_atualizarDadosContrato(self):
        fornecedor = Fornecedor("Fornecedor 2", "Escritorio", 6, "Rua B, 456", 6000, 2)
        novo_tempo_contrato = 24
        self.gerenciamento.atualizarDadosContrato(fornecedor, novo_tempo_contrato)
        print("Contrato alterado!")

    def test_verificarTempoDeEntrega(self):
        tempo_de_producao = 5
        tempo_entrega = self.gerenciamento.verificarTempoDeEntrega(tempo_de_producao)

        print("Tempo de entrega:", tempo_entrega)

if __name__ == '__main__':
    unittest.main()