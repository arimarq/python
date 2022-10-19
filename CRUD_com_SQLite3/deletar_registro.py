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


# deletar dados na tabela
def deletar(conexao, sql):
    try:
        cur = conexao.cursor()
        cur.execute(sql)
        conexao.commit()
        print('registro deletado')
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

    # obtem do usuario qual registro deseja apagar
    print('-' * 50)
    reg = int(input('qual registro deseja apagar? (0 = SAIR) [ID] '))
    if reg == 0:
        break

    # codigo SQL para deletar um registro na tabela (ATENCAO para o f-string)
    vsql = f'DELETE FROM tb_contatos WHERE N_idContato={reg}'

    # chama a funcao deletar
    deletar(vcon, vsql)

    perg = ' '
    while perg not in 'SN':
        perg = input('deseja deletar mais registros? [S/N] ').upper().strip()[0]
    if perg == 'N':
        break

# fecha a conexao com o BD
vcon.close()
