class Usuario():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def getId(self):
        return str(self.id)

    def setId(self, id):
        self.id = id

    def getusername(self):
        return self.username

    def setusername(self, username):
        self.username = username

    def getpassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

usuario = Usuario(0, 'username', 'password', False)