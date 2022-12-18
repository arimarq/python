# arquivo para criaçao do banco de dados a ser utilizado pela aplicação
import mysql.connector
from mysql.connector import Error

# DADOS PARA CONEXAO AO SERVIDOR
host = 'localhost'
user = 'root'
pwd = '123456'

# DADOS PARA CRIAR O BANCO DE DADOS
db_name = 'teste2'

# codigo SQL para criar as tabelas (altere o 'nome_tabela' e os nomes dos campos)
tabela1 = '''CREATE TABLE nome_tabela1 (
                campo_id INT PRIMARY KEY AUTO_INCREMENT,
                campo01 VARCHAR(40) NOT NULL,
                campo02 VARCHAR(40) NOT NULL,
                campo03 VARCHAR(3) NOT NULL,
                campo04 INT(5)
            );'''
tabela2 = '''CREATE TABLE nome_tabela2 (
                campo_id INT PRIMARY KEY AUTO_INCREMENT,
                campo01 VARCHAR(40) NOT NULL,
                campo02 VARCHAR(40) NOT NULL,
                campo03 VARCHAR(3) NOT NULL,
                campo04 INT(5)
            );'''

# lista para criacao das tabelas com o for (complete com o nome das variaveis 'tabelas')
lstCriar = [tabela1, tabela2]

# CONECTAR AO SERVIDOR
vcon = None
try:
    vcon = mysql.connector.connect(host=f'{host}', user=f'{user}', password=f'{pwd}')
    print('Conectado ao Servidor MySQL com sucesso')
except Error as err:
    print(f'Erro: {err}')

input('continuar')

# CRIAR O BANCO DE DADOS
vsql = f'CREATE DATABASE {db_name}'
try:
    cur = vcon.cursor()
    cur.execute(vsql)
    print('Banco de dados criado com sucesso')
except Error as err:
    print(f"Erro: '{err}'")

input('continuar')

# CRIAR AS TABELAS
# faz a conexao com o banco de dados criado
try:
    vcon = mysql.connector.connect(host=f'{host}', database=f'{db_name}', user=f'{user}', password=f'{pwd}')
except Error as err:
    print(f'Erro: {err}')
    input('sair')

# cria as tabelas
n = 0
for c in lstCriar:
    try:
        cur = vcon.cursor()
        cur.execute(lstCriar[n])
        print(f'Tabela {n+1} criada com sucesso')
    except Error as err:
        print(f'Erro: {err}')
    n += 1

input('fim')
