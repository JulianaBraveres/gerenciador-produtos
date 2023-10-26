from flask import Flask, render_template, redirect, request
import func as dbHandler
import models 
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key='__privatekey__'
bootstrap = Bootstrap(app)

@app.route('/', methods=['POST', 'GET'])
def index():
	return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method=='POST':
		username = request.form['username']
		password = request.form['password']
		dbHandler.retrieveUsers(username, password)
		users = dbHandler.retrieveUser()
		if not users:
			return render_template('login.html')
		
		elif users:
			return redirect('/dashboard')
		
	else:
		request.method=='GET'
		return render_template('login.html')


@app.route('/signup', methods= ['POST', 'GET'])
def registro():
		if request.method=='POST':
			if(request.form['username']!='' and request.form['password']!=''):
				username = request.form['username']
				password = request.form['password']
                                users = dbHandler.retrieveUser()
				
				if users:
					return print('Conta já existe')
				
				if not users:
					dbHandler.insertUser(username, password)
				
				return redirect('/')
			
		elif request.method=='GET':
			return render_template('signup.html')
		
@app.route('/dashboard')
def dashboard():
    if request.method=='POST':
        stock = {}  # Dicionário para armazenar o estoque da loja
        return render_template('dashboard.html')

    elif request.method=='GET':
        return render_template('dashboard.html')

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


app.run(debug=True)

'''
    nome = input("Digite o nome do item que deseja editar: ")
    if nome in estoque:
        nova_quantidade = int(input("Digite a nova quantidade disponível: "))
        dashboard().estoque[nome] = nova_quantidade
        print(f"A quantidade de {nome} foi atualizada para {nova_quantidade}.")
    else:
        print(f"{nome} não encontrado no estoque.")
'''
