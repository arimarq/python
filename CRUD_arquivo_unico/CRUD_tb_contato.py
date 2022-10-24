# CRUD_tb_contato.py

'''
OBSERVACOES:
1) - executa CRUD na tabela TB_CONTATOS do banco de dados agenda.
2) - as funcoes com nome inserir, consultar, alterar e deletar, são os codigos para execucao.
3) - as funcoes com nome inserirRegistro, consultarRegistro, alterarRegistro e deletarRegistro,
    são os codigos para manipulacao do banco de dados
'''

# importacao dos modulos necessarios
import sqlite3
from sqlite3 import Error
from conectar_BD import conexaoBanco
from time import sleep


# >>>>>> FUNCAO PARA CRIAR AS TABELAS DO BANCO DE DADOS <<<<<<
def criarTab():
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


# >>>>>> FUNCOES DE MANIPULACAO DO BANCO DE DADOS <<<<<<


# insere o registro no BD (create)
def inserirRegistro(conexao, sql):
    try:
        cur = conexao.cursor()
        cur.execute(sql)
        conexao.commit()
        print('-' * 50)
        print('registro inserido')
    except Error as ex:
        print(ex)


# consulta o registro no BD (read)
def consultarRegistro(conexao, sql):
    cur = conexao.cursor()
    cur.execute(sql)
    resultado = cur.fetchall()
    return resultado


# atualizar o registro no BD (update)
def atualizarRegistro(conexao, sql):
    try:
        cur = conexao.cursor()
        cur.execute(sql)
        conexao.commit()
        print('registro alterado')
    except Error as ex:
        print(ex)


# deleta o registro no BD (delete)
def deletarRegistro(conexao, sql):
    try:
        cur = conexao.cursor()
        cur.execute(sql)
        conexao.commit()
        print('registro deletado')
    except Error as ex:
        print(ex)

# >>>>>> FUNCOES DE EXECUCAO <<<<<<


# inserir (create)
def inserir():
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

        # abre a conexao com o BD // chama a funcao inserirRegistro // fecha a conexao com o BD
        vcon = conexaoBanco()
        inserirRegistro(vcon, vsql)
        vcon.close()

        perg = ' '
        while perg not in 'SN':
            perg = input('deseja inserir mais registros? [S/N] ').upper().strip()[0]
        if perg == 'N':
            break


# consultar (read)
def consultar():
    # codigo SQL para consultar todos os dados na tabela
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

    # abre a conexao com o BD // chama a funcao consultaRegistro e carrega a variavel res // fecha a conexao com o BD
    vcon = conexaoBanco()
    res = consultarRegistro(vcon, vsql)
    vcon.close()

    # exibe os dados na tela
    for r in res:
        print(r)

    # pausa a tela para leitura
    print('-' * 50)
    input('Pressione <ENTER> para continuar! ')


# atualizar (update)
def atualizar():
    while True:
        # codigo SQL para consultar os dados na tabela
        vsql = 'SELECT * FROM tb_contatos'

        # abre a conexao com o BD // chama a funcao consultaRegistro e carrega a variavel res // fecha a conexao com o BD
        vcon = conexaoBanco()
        res = consultarRegistro(vcon, vsql)
        vcon.close()

        # exibe os dados na tela
        for r in res:
            print(r)

        # obtem do usuario qual registro deseja alterar
        print('-' * 50)
        reg = int(input('qual registro deseja alterar? (0 = VOLTAR) [ID] '))
        if reg == 0:
            break

        nome = input('digite o novo nome: ')
        fone = input('digite o novo telefone: ')
        mail = input('digite o novo email: ')

        # codigo SQL para alterar um registro na tabela (ATENCAO para as aspas simples, aspas duplas e f-string)
        vsql = f'UPDATE tb_contatos SET T_nomeContato="{nome}", T_telefoneContato="{fone}", T_emailContato="{mail}" WHERE N_idContato={reg}'

        # abre a conexao com o BD // chama a funcao atualizarRegistro // fecha a conexao com o BD
        vcon = conexaoBanco()
        atualizarRegistro(vcon, vsql)
        vcon.close()

        perg = ' '
        while perg not in 'SN':
            perg = input('deseja alterar mais registros? [S/N] ').upper().strip()[0]
        if perg == 'N':
            break


# deletar (delete)
def deletar():
    while True:
        # codigo SQL para consultar os dados na tabela
        vsql = 'SELECT * FROM tb_contatos'

        # abre a conexao com o BD // chama a funcao consultaRegistro e carrega a variavel res // fecha a conexao com o BD
        vcon = conexaoBanco()
        res = consultarRegistro(vcon, vsql)
        vcon.close()

        # exibe os dados na tela
        for r in res:
            print(r)

        # obtem do usuario qual registro deseja apagar
        print('-' * 50)
        reg = int(input('qual registro deseja apagar? (0 = VOLTAR) [ID] '))
        if reg == 0:
            break

        # codigo SQL para deletar um registro na tabela (ATENCAO para o f-string)
        vsql = f'DELETE FROM tb_contatos WHERE N_idContato={reg}'

        # abre a conexao com o BD // chama a funcao deletarRegistro // fecha a conexao com o BD
        vcon = conexaoBanco()
        deletarRegistro(vcon, vsql)
        vcon.close()

        perg = ' '
        while perg not in 'SN':
            perg = input('deseja deletar mais registros? [S/N] ').upper().strip()[0]
        if perg == 'N':
            break


# >>>>>> CRIACAO DO MENU <<<<<<
# carrega a tupla com as opcoes
lista = ('Sair', 'Criar Tabelas', 'Inserir', 'Consultar', 'Atualizar', 'Deletar')

while True:
    # Cria as variaveie para confirmacao
    perg = ' ' # carrega perg vazia para entrar na confirmacao
    esperar = 0 # carrega 0 seg para o sleep

    # exibe o menu na tela
    print('=' * 20)
    print(f'{"MENU PRINCIPAL":^20}')
    print('=' * 20)
    for i, item in enumerate(lista):
        print(f'{i} = {item}')
    print('=' * 20)
    op = int(input('Opção: '))

    # carrega as variaveis de acordo com a opcao
    if op == 0:
        break
    elif op == 1:
        resp = 'Criar Tabelas'
        acao = 'criarTab()'
    elif op == 2:
        resp = 'Inserir Registro'
        acao = 'inserir()'
    elif op == 3:
        resp = 'Consultar Registros'
        acao = 'consultar()'
    elif op == 4:
        resp = 'Atualizar Registro'
        acao = 'atualizar()'
    elif op == 5:
        resp = 'Deletar Registro'
        acao = 'deletar()'
    else:
        resp = 'uma opção inválida\nEscolha entre 0 e 5'
        perg = 'N' # carrega N na perg para passar direto pela confirmacao
        esperar = 4 # carrega 4 seg para o sleep

    # exibe a opcao escolhida na tela e pede confirmacao
    print(f'Você escolheu {resp}.')
    sleep(esperar)
    while perg not in 'SN':
        perg = input('Confirma? [S/N] ').strip().upper()[0]

    print('-' * 50)
    # verifica a resposta e executa a funcao escolhida
    if perg == 'S':
        exec(acao) # para executar uma variavel precisa do exec()
