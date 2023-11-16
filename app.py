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
        username = request.form['username'] #username recebe o nome vindo do form username
        password = request.form['password']
        users = dbHandler.retrieveUsers()
        
        if not users:  #se users existir, renderiza o dashboard
            return render_template('login.html')
		
        if users: #se users n existir 
            for user in users:
                if user[0]==username and user[1]==password:
                  return redirect('/dashboard')    		
    
    return render_template('login.html')


@app.route('/signup', methods= ['POST', 'GET'])
def signup():
    if request.method=='POST':
        if(request.form['username']!='' and request.form['password']!=''): #se as áreas do form não forem vazias, username receber o input do form com nome username
            username = request.form['username']
            password = request.form['password']
            users = dbHandler.retrieveUsers()		
            
            if users:
                for user in users:
                      if user[0]==username and user[1]==password:
                            return redirect('/signup')
            dbHandler.insertUser(username, password)
            return redirect('/login') #render_template('/teste.html', users = users)
			
    #elif request.method=='GET':
    return render_template('signup.html')

		
@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    stock = []
    stock = dbHandler.retrieveProduct()
    return render_template('dashboard.html', stock = stock)


@app.route('/add', methods = ['POST', 'GET'])
def add():
    if request.method=='POST':
        models.Product.adicionar_item()
        return redirect('/dashboard')
    
    elif request.method=='GET':
        return render_template('add.html')



@app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method=='POST':
        models.Product.remover_estoque()
        return redirect('/dashboard')
    elif request.method=='GET':
        return render_template('delete.html')


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
