class Produto():
    def __init__(self, id, name, quantity):
        self.name = name
        self.quantity = quantity

    def getname(self):
        return self.name
    
    def setname(self, name):
        self.name = name

    def getQuantidade(self):
        return self.quantity

    def setQuantidade(self, quantity):
        self.quantity = quantity

product = Produto(0, 'name', 'quantity')