# MENU DE OPÇOES PARA O CRUD

# importar modulos
from time import sleep

# carrega a lista com as opcoes
lista = ['Sair', 'Criar Tabelas', 'Inserir', 'Consultar', 'Atualizar', 'Deletar']

while True:
    print("\n" * 20)  # limpa o terminal

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
        arquivo = 'criar_tabelas.py'
    elif op == 2:
        resp = 'Inserir Registro'
        arquivo = 'inserir_registro.py'
    elif op == 3:
        resp = 'Consultar Registros'
        arquivo = 'consultar_registros.py'
    elif op == 4:
        resp = 'Atualizar Registro'
        arquivo = 'atualizar_registro.py'
    elif op == 5:
        resp = 'Deletar Registro'
        arquivo = 'deletar_registro.py'
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
    # verifica a resposta
    if perg == 'S':
        exec(open(arquivo).read()) # executa o arquivo da op
