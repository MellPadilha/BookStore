from models import Vendedor

class GerenciamentoVendedores:

    def cadastrarNovoVendedor(self, nome, codigo_vendedor, idade, salario, experiencia):
        Vendedor(nome, codigo_vendedor, idade, salario, experiencia)

    def pagarComissão(self, codigo_vendedor, salario):
        comissao = Vendedor.calcularComissao(codigo_vendedor)
        salario_mes = salario + comissao
        Vendedor.salarioComComissao(salario_mes)

    def calcularFerias(self, numero_de_vendas):
        tempo_de_ferias = numero_de_vendas / 8
        return tempo_de_ferias

