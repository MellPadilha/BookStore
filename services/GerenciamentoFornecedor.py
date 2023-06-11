from models.Fornecedor import Fornecedor

class GerenciamentoFornecedor:

    @classmethod
    def cadastrarNovoFornecedor(self, nome, tipo_de_fornecedor, tempo_de_contrato, endereco, pagamento, tempo_de_producao):
        Fornecedor(nome, tipo_de_fornecedor, tempo_de_contrato, endereco, pagamento, tempo_de_producao)

    @classmethod
    def atualizarDadosContrato(self, fornecedor, novo_tempo_contrato):
        fornecedor.atualizarTempoContrato(novo_tempo_contrato)

    @classmethod
    def verificarTempoDeEntrega(self, tempo_de_producao):
        tempo_entrega = tempo_de_producao * 2
        return tempo_entrega

