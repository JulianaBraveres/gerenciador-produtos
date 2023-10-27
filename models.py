class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def editar_item(name, quantity):
        if(request.form[''] and stock.get(name)):
            dbHandler.editProduct(quantity)
            dashboard.stock[name] = quantity
            return print("Quantidade atualizada com sucesso")

        else: 
            print('Produto não encontrado no estoque. Nome não existe')


    def remover_estoque(name):
        if(request.form['name'] != '' and stock.get(name)):
            dbHandler.removeProduct(name)
            del stock[name, quantity]
            return print("Produto removido com sucesso")

        else:
            return print("Produto não existe. Nome inválido")

    def adicionar_item(name, quantity):
        if(request.form['name'] != ''):
            name = request.form['name']

            if dbHandler.products and stock.get(name):
                return print("Produto inválido. Nome já existe!")

            if not dbHandler.products:
                dbHandler.insertProduct(name, quantity)
                dashboard.stock[name] = quantity
                print(f"{name} foi adicionado ao estoque com uma quantidade de {quantity}.")
                return render_template(dashboard.html)



