from models.Vendedor import Vendedor

class GerenciamentoVendedores:

    @classmethod
    def cadastrarNovoVendedor(self,  nome, codigo_vendedor, numero_de_vendas, idade, salario, experiencia, pagamento_mes):
        Vendedor( nome, codigo_vendedor, numero_de_vendas, idade, salario, experiencia, pagamento_mes)

    @classmethod
    def pagarComissao(self, nm_venda, salario):
        comissao = Vendedor.calcularComissao(nm_venda)
        salario_mes = salario + comissao
        Vendedor.salarioComComissao(salario_mes)

    @classmethod
    def calcularFerias(self, numero_de_vendas):
        tempo_de_ferias = numero_de_vendas / 8
        return tempo_de_ferias

