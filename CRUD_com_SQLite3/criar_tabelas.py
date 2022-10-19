import sqlite3
from sqlite3 import Error
from conectar_BD import conexaoBanco

# chama a funcao conexaoBanco do arquivo conectar BD e cria a variavel vcon
vcon = conexaoBanco()

# codigo SQL para criar a tabela
vsql = '''CREATE TABLE tb_contatos(
          N_idContato INTEGER PRIMARY KEY AUTOINCREMENT,
          T_nomeContato VARCHAR(30),
          T_telefoneContato VARCHAR(14),
          T_emailContato VARCHAR(30)
          );
       '''
# vsql1 = '''CREATE TABLE tb_vendas(
#           N_idVendas INTEGER PRIMARY KEY AUTOINCREMENT,
#           T_nomeVendas VARCHAR(30)
#           );
#        '''
#
# vsql2 = '''CREATE TABLE tb_clientes(
#           N_idClientes INTEGER PRIMARY KEY AUTOINCREMENT,
#           T_nomeClientes VARCHAR(30)
#           );
#        '''

# lista para criacao das tabelas (complete com o nome dos 'vsql' acima)
lstCriar = [vsql]

# criacao da tabela
n = 0
for c in lstCriar:
    def criarTabela(conexao, sql):
        try:
            cur = conexao.cursor()
            cur.execute(sql)
            print(f'tabela {n} criada com sucesso')
        except Error as ex:
            print(ex)

    criarTabela(vcon, lstCriar[n])
    n += 1
# fecha a conexao com o BD
vcon.close()
