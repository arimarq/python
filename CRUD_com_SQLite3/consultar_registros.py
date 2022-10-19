import sqlite3
from sqlite3 import Error
from conectar_BD import conexaoBanco

# chama a funcao conexaoBando do arquivo conectar_BD e cria a variavel vcon
vcon = conexaoBanco()


# consulta os dados na tabela
def consulta(conexao, sql):
    cur = conexao.cursor()
    cur.execute(sql)
    resultado = cur.fetchall()
    return resultado


# codigo SQL para consultar os dados na tabela
vsql = 'SELECT * FROM tb_contatos'

'''
para consultas com filtro utilize a funçao WHERE na linha sql.
EX: 'SELECT * FROM tb_contatos WHERE T_nomeContato="silva"'
vai retornar todos os registro que tem silva no nome (tem que ser totalmente igual)
ATENCAO para as aspas simples e aspas duplas

para consultas com filtro e parte do campo, utilize a funcao LIKE do sql.
EX: 'SELECT * FROM tb_contatos WHERE T_nomeContato LIKE "%silva%"'
nesse caso vai retornar todos os registros que tenham silva em qualquer parte do nome
ATENCAO para as aspas simples e aspas duplas
'''

# chama a funcao consulta e carrega a variavel res com os resultados
res = consulta(vcon, vsql)

# exibe os dados na tela
for r in res:
    print(r)

# fecha a conexao com o BD
vcon.close()

# pausa a tela para leitura
print('-' * 50)
perg = input('Pressione <ENTER> para continuar! ')
