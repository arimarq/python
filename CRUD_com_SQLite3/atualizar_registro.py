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


# atualiza dados na tabela
def atualizar(conexao, sql):
    try:
        cur = conexao.cursor()
        cur.execute(sql)
        conexao.commit()
        print('registro alterado')
    except Error as ex:
        print(ex)


while True:
    # codigo SQL para consultar os dados na tabela
    vsql = 'SELECT * FROM tb_contatos'

    # chama a funcao consulta e carrega a variavel res com os resultados
    res = consulta(vcon, vsql)

    # exibe os dados na tela
    for r in res:
        print(r)

    # obtem do usuario qual registro deseja alterar
    print('-' * 50)
    reg = int(input('qual registro deseja alterar? (0 = SAIR) [ID] '))
    if reg == 0:
        break

    nome = input('digite o novo nome: ')
    fone = input('digite o novo telefone: ')
    mail = input('digite o novo email: ')

    # codigo SQL para alterar um registro na tabela (ATENCAO para as aspas simples, aspas duplas e f-string)
    vsql = f'UPDATE tb_contatos SET T_nomeContato="{nome}", T_telefoneContato="{fone}", T_emailContato="{mail}" WHERE N_idContato={reg}'

    # chama a funcao deletar
    atualizar(vcon, vsql)

    perg = ' '
    while perg not in 'SN':
        perg = input('deseja alterar mais registros? [S/N] ').upper().strip()[0]
    if perg == 'N':
        break

# fecha a conexao com o BD
vcon.close()
