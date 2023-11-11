import func as dbHandler
from flask import Flask, render_template, redirect, request


class Product:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


    def remover_estoque():
        if(request.form['name'] != ''):
            name = request.form['name']
            for product in dbHandler.retrieveProduct():
                if product[0]==name:
                    dbHandler.removeProduct(name)
                    return print("Produto removido com sucesso")

        else:
            return print("Produto não existe. Nome inválido")

    def adicionar_item():
        if(request.form['name'] != '' and request.form['quantity'] != ''):
            name = request.form['name']
            quantity = request.form['quantity']
            
            for product in dbHandler.retrieveProduct():
                if product[0]==name and product[1]==quantity:
                    return print("Produto inválido. Nome já existe!")
            dbHandler.insertProduct(name, quantity)
            print(f"{name} foi adicionado ao estoque com uma quantidade de {quantity}.")
            return redirect('/dashboard')
                    
            
    product = ('name', 'quantity')