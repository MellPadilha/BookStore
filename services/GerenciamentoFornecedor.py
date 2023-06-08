from models import Fornecedor

class GerenciamentoFornecedor:

    def cadastrarNovoFornecedor(self, nome, tipo_de_fornecedor, tempo_de_contrato, endereco, tempo_de_entrega):
        Fornecedor(nome, tipo_de_fornecedor, tempo_de_contrato, endereco, tempo_de_entrega)

    def atualizarDadosContrato(self, fornecedor, novo_tempo_contrato):
        fornecedor.atualizarTempoContrato(novo_tempo_contrato)

    def verificarTempoDeEntrega(self, tempo_de_producao):
        tempo_entrega = tempo_de_producao * 2
        return tempo_entrega

