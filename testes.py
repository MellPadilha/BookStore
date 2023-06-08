import unittest
from models import Venda, Livro, Cliente, Vendedor, Fornecedor
from services import GerenciamentoVendedores, VendaLivros, GerenciamentoFornecedor

# class UnitTest(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')

class TestVendaLivros(unittest.TestCase):

    def setUp(self):
        self.venda_livros = VendaLivros()

    def test_cadastrarNovaVenda(self):
        codigo_venda = 1
        quantidade = 2
        livro = Livro("Livro A", 10, "Autor A", "Descrição A", 50.0)
        cliente = Cliente("João", "Silva", "joao@example.com", "Rua A", "123456789")
        forma_pagamento = "Cartão de Crédito"
        status = "Pendente"

        # Chamar o método de cadastro de nova venda
        self.venda_livros.cadastrarNovaVenda(codigo_venda, quantidade, livro, cliente, forma_pagamento, status)

        # Verificar se a venda foi cadastrada corretamente
        # Exemplo: Verificar se o atributo código da venda foi definido corretamente
        venda = Venda.getVendaByCodigo(codigo_venda)
        self.assertEqual(venda.codigo_venda, codigo_venda)
        self.assertEqual(venda.quantidade, quantidade)
        self.assertEqual(venda.livro, livro)
        self.assertEqual(venda.cliente, cliente)
        self.assertEqual(venda.forma_pagamento, forma_pagamento)
        self.assertEqual(venda.status, status)

    def test_realizarDevolucao(self):
        # Configurar um cenário com uma venda já existente
        codigo_venda = 1
        quantidade = 2
        livro = Livro("Livro A", 10, "Autor A", "Descrição A", 50.0)
        cliente = Cliente("João", "Silva", "joao@example.com", "Rua A", "123456789")
        forma_pagamento = "Cartão de Crédito"
        status = "Pendente"
        venda = Venda(codigo_venda, quantidade, livro, cliente, forma_pagamento, status)

        # Chamar o método de realizar devolução
        novo_status = "Devolvido"
        self.venda_livros.realizarDevolucao(novo_status)

        # Verificar se o status da venda foi atualizado corretamente
        self.assertEqual(venda.status, novo_status)

    def test_vendaComCupom(self):
        # Configurar um cenário com um livro e um código de cupom
        codigo_cupom = "ABC123"
        livro = Livro("Livro A", 10, "Autor A", "Descrição A", 50.0)

        # Chamar o método de venda com cupom
        self.venda_livros.vendaComCupom(codigo_cupom)

        # Verificar se o desconto foi aplicado corretamente no livro
        self.assertEqual(livro.preco_desconto, livro.preco * 0.9)  # Exemplo: desconto de 10%

class TestGerenciamentoVendedores(unittest.TestCase):

    def setUp(self):
        self.gerenciamento = GerenciamentoVendedores()

    def test_cadastrarNovoVendedor(self):
        self.gerenciamento.cadastrarNovoVendedor("João", 1, 30, 5000, "Intermediário")
        # Verificar se o vendedor foi cadastrado corretamente

    def test_pagarComissao(self):
        # Cadastrar um vendedor com código 1
        self.gerenciamento.cadastrarNovoVendedor("João", 1, 30, 5000, "Intermediário")
        # Pagar comissão para o vendedor com código 1
        self.gerenciamento.pagarComissao(1, 5000)
        # Verificar se o salário do vendedor foi atualizado corretamente

    def test_calcularFerias(self):
        # Calcular férias com base em um número de vendas
        tempo_de_ferias = self.gerenciamento.calcularFerias(100)
        print("Tempo de ferias:", tempo_de_ferias)
        # Verificar se o tempo de férias foi calculado corretamente

class TestGerenciamentoFornecedor(unittest.TestCase):
    def setUp(self):
        self.gerenciamento = GerenciamentoFornecedor()

    def test_cadastrarNovoFornecedor(self):
        # Dados do fornecedor
        nome = "Fornecedor 1"
        tipo_de_fornecedor = "Livros"
        tempo_de_contrato = 12
        endereco = "Rua A, 123"
        tempo_de_entrega = 3

        # Chamar o método de cadastro
        self.gerenciamento.cadastrarNovoFornecedor(nome, tipo_de_fornecedor, tempo_de_contrato, endereco, tempo_de_entrega)

        # Verificar se o fornecedor foi cadastrado corretamente
        fornecedores = Fornecedor.get_all()
        self.assertEqual(len(fornecedores), 1)
        fornecedor = fornecedores[0]
        self.assertEqual(fornecedor.nome, nome)
        self.assertEqual(fornecedor.tipo_de_fornecedor, tipo_de_fornecedor)
        self.assertEqual(fornecedor.tempo_de_contrato, tempo_de_contrato)
        self.assertEqual(fornecedor.endereco, endereco)
        self.assertEqual(fornecedor.tempo_de_entrega, tempo_de_entrega)

    def test_atualizarDadosContrato(self):
        # Criar um fornecedor de teste
        fornecedor = Fornecedor("Fornecedor 2", "Escritorio", 6, "Rua B, 456", 2)

        # Chamar o método de atualização de contrato
        novo_tempo_contrato = 24
        self.gerenciamento.atualizarDadosContrato(fornecedor, novo_tempo_contrato)

        # Verificar se o contrato foi atualizado corretamente
        self.assertEqual(fornecedor.tempo_de_contrato, novo_tempo_contrato)

    def test_verificarTempoDeEntrega(self):
        # Dados de produção
        tempo_de_producao = 5

        # Chamar o método de verificação de tempo de entrega
        tempo_entrega = self.gerenciamento.verificarTempoDeEntrega(tempo_de_producao)

        # Verificar se o tempo de entrega foi calculado corretamente
        self.assertEqual(tempo_entrega, tempo_de_producao * 2)

if __name__ == '__main__':
    unittest.main()