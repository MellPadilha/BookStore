class Vendedor:
    # Atributos da classe:
    # nome
    # codigo_vendedor
    # numero_de_vendas
    # idade
    # salario
    # pagamento_mes
    # experiencia

    def __init__(self, nome, codigo_vendedor, numero_de_vendas, idade, salario, experiencia, pagamento_mes):
        self.nome = nome
        self.codigo_vendedor = codigo_vendedor
        self.numero_de_vendas = numero_de_vendas
        self.idade = idade
        self.salario = salario
        self.experiencia = experiencia
        self.pagamento_mes = pagamento_mes

    def alterarSalario(self):
        if self.experiencia == 'Iniciante':
            self.salario = 2000
        elif self.experiencia == 'Intermediario':
            self.salario = 5000
        elif self.experiencia == 'Senior':
            self.salario = 10000

    def calcularComissao(self):
        comissao = self.numero_de_vendas * 30
        return comissao
    
    def promossaoVendedor(self):
         if self.numero_de_vendas > 300:
            self.experiencia = 'Iniciante'
         elif self.numero_de_vendas > 5000:
            self.experiencia = 'Intermediario'
         elif self.numero_de_vendas > 10000:
            self.experiencia = 'Senior'

         self.alterarSalario()

    def salarioComComissao(self, salario_mes):
        self.salario = salario_mes
        self.pagamento_mes = True
        self.alterarSalario()