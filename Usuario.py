class Usuario():
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

    def getId(self):
        return str(self.id)

    def setId(self, id):
        self.id = id

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getSenha(self):
        return self.senha

    def setPassword(self, senha):
        self.senha = senha

usuario = Usuario(0, 'nome', 'email', 'senha', False)