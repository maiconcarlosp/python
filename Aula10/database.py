# SGBD - Sistema gerenciador de banco de dados
# JDBC

# PostgreSQL
# import psycopg2

# Oracle
# import cx_Oracle

# Sql Server
# import pymssl

import sqlite3
# "user=root,password=root,port=3306,host=localhost"
conn = sqlite3.connect("livraria.sqlite3")

# cursor permite adicionar query
cursor = conn.cursor()

cursor.execute(""" 
	CREATE TABLE cliente(
		cd_cliente integer primary key AUTOINCREMENT,
		nome varchar(50) not null,
		cpf varchar(14) unique not null,
		dataNascimento varchar(10) not null,
		email varchar(50),
		endereco varchar(100) not null
		)
""")

cursor.execute("""
	INSERT INTO cliente (nome, cpf, dataNascimento, email, endereco)
	VALUES('Batman', '123.456.789-0', '01/01/1970', 'batman@hotmail.com.', 'batcaverna')
""")
# executa no banco
conn.commit()

cursor.close()
conn.close()

#resultados = c.fetchone() - retorna somente o primeiro item do banco
#resultados = c.fetchall() - retorna todos os itens encontrados