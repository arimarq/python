import sqlite3
from sqlite3 import Error
from conectar_BD import conexaoBanco

# chama a funcao conexaoBando do arquivo conectar_BD e cria a variavel vcon
vcon = conexaoBanco()


# inserir dados na tabela
def inserir(conexao, sql):
    try:
        cur = conexao.cursor()
        cur.execute(sql)
        conexao.commit()
        print('-' * 50)
        print('registro inserido')
    except Error as ex:
        print(ex)


while True:
    # obtendo os dados do usuario
    nome = input('digite o nome: ')
    telefone = input('digite o telefone: ')
    email = input('digite o email: ')

    # codigo SQL para inserir dados na tabela (ATENCAO para o f antes das aspas para utilizao do f-string)
    vsql = f'''INSERT INTO tb_contatos 
                    (T_nomeContato, T_telefoneContato, T_emailContato) 
                    VALUES ("{nome}", "{telefone}", "{email}")
            '''

    # chama a funcao inserir
    inserir(vcon, vsql)

    perg = ' '
    while perg not in 'SN':
        perg = input('deseja inserir mais registros? [S/N] ').upper().strip()[0]
    if perg == 'N':
        break

# fecha a conexao com o BD
vcon.close()
