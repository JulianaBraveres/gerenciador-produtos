from flask import Flask, render_template, redirect, request
import func as dbHandler

app = Flask(__name__)
app.secret_key='__privatekey__'

@app.route('/', methods=['POST', 'GET'])
def login():
	if request.method=='POST':
		username = request.form['username']
		password = request.form['password']
		dbHandler.retrieveUsers(username, password)
		users = dbHandler.retrieveUsers()
		if not dbHandler.users:
			return render_template('login.html')
		
		else:
			return redirect('/dashboard', name=username)
		
	else:
		request.method=='GET'
		return render_template('login.html')


@app.route('/registro', methods= ['POST', 'GET'])
def registro():
		if request.method=='POST':
			if(request.form['username']!='' and request.form['password']!=''):
				username = request.form['username']
				password = request.form['password']
				
				if dbHandler.users:
					return print('Conta já existe')
				
				if not dbHandler.users:
					dbHandler.insertUser(username, password)
				
				return redirect('/login')
			
		elif request.method=='GET':
			return render_template('registro.html')
		
@app.route('/dashboard')
def dashboard():
	toque = {}  # Dicionário para armazenar o estoque da loja

def adicionar_item():
    nome = input("Digite o nome do item: ")
    quantidade = int(input("Digite a quantidade disponível: "))
    estoque[nome] = quantidade
    print(f"{nome} foi adicionado ao estoque com uma quantidade de {quantidade}.")

def editar_item():
    nome = input("Digite o nome do item que deseja editar: ")
    if nome in estoque:
        nova_quantidade = int(input("Digite a nova quantidade disponível: "))
        estoque[nome] = nova_quantidade
        print(f"A quantidade de {nome} foi atualizada para {nova_quantidade}.")
    else:
        print(f"{nome} não encontrado no estoque.")

def mostrar_estoque():
    print("\nItens no estoque:")
    for item, quantidade in estoque.items():
        print(f"{item}: {quantidade}")

while True:
    print("\n### Menu ###")
    print("1. Adicionar item ao estoque")
    print("2. Editar quantidade de um item no estoque")
    print("3. Mostrar itens no estoque")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        adicionar_item()
    elif escolha == "2":
        editar_item()
    elif escolha == "3":
        mostrar_estoque()
    elif escolha == "4":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")



app.run()
