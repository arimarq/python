def pesquisa():
    if nome in lista:
        print(f'o {nome} está na lista')
    else:
        print(f'o {nome} NÃO está na lista')


with open('convidados.txt', 'r') as arquivo:
    lista = arquivo.read()

while nome not in '999':
    nome = input('qual nome deseja pesquisar? [sair = 999] ').strip().upper()
    if nome == '999':
        break
    pesquisa()
