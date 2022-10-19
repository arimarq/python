import sqlite3
from sqlite3 import Error


# criar conexao (se o BD não existir vai ser criado)
def conexaoBanco():
    # para BD em outra pasta utilize caminho completo (ATENCAO para o r antes das aspas para evitar o escape da \)
    # caminho = r'C:\Users\arima\Meu Drive\pessoais\python\estudo\proj_aprender\CRUD_python_SQLite3\agenda.db'
    caminho = 'agenda.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con
