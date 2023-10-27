class Produto():
    def __init__(self, nome, quantidade, preco, descricao):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.descricao = descricao

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getQuantidade(self):
        return self.quantidade

    def setQuantidade(self, quantidade):
        self.quantidade = quantidade

    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        self.preco = preco
    
    def getDescricao(self):
        return self.descricao

    def setDescricao(self, descricao):
        self.descricao = descricao

produto = Produto(0, 'nome', 'quantidade', 'preco', 'descricao')