import sqlite3 as sql

def insertUser(username,password):
    con = sql.connect("estoque.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def retrieveUsers(username, password):
	con = sql.connect("estoque.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM users")
	users = cur.fetchall()
	con.close()
	return users

def insertProduct(name, quantity):
	con = sql.connect("estoque.db")
	cur = con.cursor()
	cur.execute("INSERT INTO products (name,quantity) VALUES (?,?)", (name, quantity))
	con.commit()
	con.close()

def retrieveProduct(name):
	con = sql.connect("estoque.db")
	cur = con.cursor()
	cur.execute("SELECT name FROM products")
	products = cur.fetchall()
	con.close()
	return products

def editProduct(quantity):
	con = sql.connect("estoque.db")
	cur = con.cursor()
	cur.execute("UPDATE INTO products (quantity) VALUES (?)", (quantity))
	products = cur.fetchall()
	con.close()
	return products

def removeProduct(name):
	con = sql.connect("estoque.db")
	cur = con.cursor()
	cur.execute("DELETE FROM products WHERE name IN (SELECT name FROM products) == (name) VALUES (?)", (name))
	con.commit()
	con.close()
