class Cliente:
    # Atributos da classe:
    # nome
    # sobrenome
    # apelido
    # nascimento
    # endereco
    # telefone

    def __init__(self, nome, sobrenome, apelido, nascimento, endereco, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.apelido = apelido
        self.nascimento = nascimento
        self.endereco = endereco
        self.telefone = telefone

    def alterarEndereco(self, endereco_novo):
        self.endereco = endereco_novo

    def atualizarTelefone(self, telefone_novo):
        self.telefone = telefone_novo

    def alterarApelido(self, apelidoNovo):
        self.apelido = apelidoNovo