class Fornecedor:
    # Atributos da classe:
    # nome
    # tipo_de_fornecedor -> Livros, Escritorio(materiais de escritorio) e tecnologia(teclados, fones e afins)
    # tempo_de_contrato
    # endereco
    # pagamento
    # tempo_de_producao

    def __init__(self, nome, tipo_de_fornecedor, tempo_de_contrato, endereco, pagamento, tempo_de_producao):
        self.nome = nome
        self.tipo_de_fornecedor = tipo_de_fornecedor
        self.tempo_de_contrato = tempo_de_contrato
        self.endereco = endereco
        self.pagamento = pagamento
        self.tempo_de_producao = tempo_de_producao

    def atualizarTempoContrato(self, novo_tempo):
        self.tempo_de_contrato = novo_tempo

    def atualizarEndereco(self, novo_endereco):
        self.endereco = novo_endereco

    def calcularValorPagamento(self):
        if self.tipo_de_fornecedor == 'Livros':
            return self.pagamento * 1.1
        elif self.tipo_de_fornecedor == 'Escritorio':
            return self.pagamento * 1.2
        elif self.tipo_de_fornecedor == 'Tecnologia':
            return self.pagamento * 1.3
        else:
            return self.pagamento
