import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import smtplib
import email.message
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# declarando as variaveis
valores = result = resultadoTela = ''
data = hora = nome = end = email_cli = fone = op1 = op2 = op3 = op4 = anot = ''

# abrir e ler as informações nos arquivos txt
with open('cadastro.txt', 'r') as arquivo:
    texto = arquivo.readlines()

with open('corpo_email.txt', 'r') as arquivo2:
    texto2 = arquivo2.read()

# carrega as variaveis com os dados para conexao na planilha e envio do email
ID_planilha = (texto[1][:-1])
meu_email = (texto[3][:-1])
password_mail = (texto[5][:-1])
assunto_mail = (texto[7][:-1])
folha = (texto[9][:-1])
coluna = (texto[11][:-1])
corpo_email = texto2

# dados da planilha)
n = 2
linha = f'{folha}!A{n}:{coluna}{n}'

# FAZ A CONEXAO E AUTENTICAÇÃO COM O GOOGLE SHEETS
# se modificar este escopo, apague o arquivo 'token.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None

if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# se não houver credenciais validas o usuario vai fazer login manualmente
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            # coloque o nome do seu arquivo .json que foi baixado no google cloud
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # salva as credenciais para futuros logins
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

# inicializa o serviço de planilhas no modo global
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


class tela:
    def recriarFrame2(self):
        self.fr2.destroy()
        self.fr2 = tk.Frame(self.fr0, height=400, width=400, borderwidth=2, relief='ridge')
        self.fr2.pack(side=tk.LEFT)
        self.fr2.pack_propagate(0)

    def __init__(self, master):
        self.principal = master
        self.principal.geometry('700x500')
        self.principal.title('Teste Vocacional')
        # self.janelaPrincipal.iconbitmap('imagens/bandeira.ico')
        self.principal.configure(background='lightblue')

        # cria e exibe os frames
        self.fr0 = tk.Frame(self.principal, background='lightyellow', borderwidth=4, relief='ridge')
        self.fr1 = tk.Frame(self.fr0, height=400, width=200, background='lightgreen', borderwidth=2, relief='ridge')
        self.fr2 = tk.Frame(self.fr0, height=400, width=400, borderwidth=2, relief='ridge')
        self.fr0.pack(padx=30, pady=30)
        self.fr1.pack(side=tk.LEFT)
        self.fr2.pack(side=tk.LEFT)
        self.fr1.pack_propagate(0)
        self.fr2.pack_propagate(0)

        # elementos do frame 1
        self.lbl_titulo = tk.Label(self.fr1, text='MENU PRINCIPAL', background='lightgreen')
        self.btn1 = tk.Button(self.fr1, text='Ver novas respostas', width=20, command=self.novas)
        self.btn2 = tk.Button(self.fr1, text='Resultado do teste', width=20, command=self.resultado)
        self.btn3 = tk.Button(self.fr1, text='Enviar e-mail', width=20, command=self.enviar_email)
        self.btn4 = tk.Button(self.fr1, text='Limpar respostas', width=20, command=self.limpar_resp)
        self.traco = tk.Label(self.fr1, text=f'\u2550' * 12, background='lightgreen')
        self.btn5 = tk.Button(self.fr1, text='Dados do Usuário', width=20, command=self.executa_dados)
        self.btn6 = tk.Button(self.fr1, text='Resultado 01', width=20, command=self.executa_result01)
        self.btn7 = tk.Button(self.fr1, text='Resultado 02', width=20, command=self.executa_result02)
        self.btn8 = tk.Button(self.fr1, text='Resultado 03', width=20, command=self.executa_result03)
        self.btn9 = tk.Button(self.fr1, text='Corpo do E-mail', width=20, command=self.executa_corpoEmail)
        self.btn10 = tk.Button(self.fr1, text='Valores do teste', width=20, command=self.executa_valores)
        self.lbl_titulo.pack(padx=10, pady=10)
        self.btn1.pack()
        self.btn2.pack()
        self.btn3.pack()
        self.btn4.pack()
        self.traco.pack()
        self.btn5.pack()
        self.btn6.pack()
        self.btn7.pack()
        self.btn8.pack()
        self.btn9.pack()
        self.btn10.pack()

        # elementos do frame 2
        self.lbl = tk.Label(self.fr2, text='JANELA DE EXIBIÇÃO', font='Verdana')
        self.lbl.pack(padx=5, pady=5)

    def novas(self):
        # importando variaveis globais
        global valores, result, data, hora, nome, end, email_cli, fone, op1, op2, op3, op4, anot

        # verifica a ultima linha preenchida da planilha
        while True:
            global n
            resultcell = sheet.values().get(spreadsheetId=ID_planilha,
                                            range=f'{folha}!{coluna}{n}:{coluna}{n}').execute()  # le o valor da coluna J na linha 'n'
            valuecell = resultcell.get('values', [])
            if not valuecell:  # chega se valuecell esta vazio, se vazio é verdadeiro
                linha = f'{folha}!A{n}:{coluna}{n}'
                result = sheet.values().get(spreadsheetId=ID_planilha, range=linha).execute()
                valores = result.get('values', [])  # guarda os valores da ultima linha preenchida na variavel 'valores' como uma lista composta

                # carrega as variaveis com os dados da lista 'valores'
                if not valores:
                    data = 'Não há respostas novas'
                    break
                else:
                    data = valores[0][0][:10]
                    hora = valores[0][0][11:]
                    nome = valores[0][1].upper()
                    end = valores[0][2]
                    email_cli = valores[0][3]
                    fone = valores[0][4]
                    op1 = valores[0][5]
                    op2 = valores[0][6]
                    op3 = valores[0][7]
                    op4 = valores[0][8]
                    anot = 'Não enviada'
                    break
            else:
                n += 1

        # cria o texto para exibir na janela
        texto = (f'Preenchimento: {data} {hora} \n'
                 f'Nome: {nome} \n'
                 f'Endereço: {end} \n'
                 f'E-mail: {email_cli} \n'
                 f'Telefone: {fone} \n'
                 f'{"-" * 60} \n'
                 f'Respostas do teste: \n'
                 f'{"-" * 60} \n'
                 f'Questão Nr 01 = {op1} \n'
                 f'Questão Nr 02 = {op2} \n'
                 f'Questão Nr 03 = {op3} \n'
                 f'Questão Nr 04 = {op4} \n'
                 f'{"-" * 60} \n'
                 f'Resposta do teste: {anot}')

        # exibe valores na janela
        self.recriarFrame2()
        self.lbl = tk.Label(self.fr2, text='DADOS COLETADOS NA PLANILHA', font=('Verdana', 12))
        self.lbl.pack(padx=5, pady=5)
        self.txtarea = scrolledtext.ScrolledText(self.fr2, font=('Calibri', 12), wrap=tk.WORD)
        self.txtarea.insert(tk.INSERT, texto)
        self.txtarea.config(state=tk.DISABLED)  # torna o scrolledtext somente leitura
        self.txtarea.pack(expand=True, fill=tk.X)

    def resultado(self):
        global resultadoTela

        # abre o arquivo valores_teste txt e le os valores para os if abaixo
        with open('valores_teste.txt', 'r') as arquivo:
            valores = arquivo.readlines()

        # carrega as variaveis com os dados
        q01_op01 = int(valores[1][:-1])
        q01_op02 = int(valores[3][:-1])
        q01_op03 = int(valores[5][:-1])
        q02_op01 = int(valores[7][:-1])
        q02_op02 = int(valores[9][:-1])
        q02_op03 = int(valores[11][:-1])
        q03_op01 = int(valores[13][:-1])
        q03_op02 = int(valores[15][:-1])
        q03_op03 = int(valores[17][:-1])
        q04_op01 = int(valores[19][:-1])
        q04_op02 = int(valores[21][:-1])
        q04_op03 = int(valores[23][:-1])
        res01 = int(valores[25][:-1])
        res03 = int(valores[31][:-1])

        # analisa as respostas e carrega o valor na variavel 'respXX'
        # questao 01
        if op1[:2] == '01':
            resp01 = q01_op01
        elif op1[:2] == '02':
            resp01 = q01_op02
        elif op1[:2] == '03':
            resp01 = q01_op03
        else:
            resp01 = 0

        # questao 02
        if op2[:2] == '01':
            resp02 = q02_op01
        elif op2[:2] == '02':
            resp02 = q02_op02
        elif op2[:2] == '03':
            resp02 = q02_op03
        else:
            resp02 = 0

        # questao 03
        if op3[:2] == '01':
            resp03 = q03_op01
        elif op3[:2] == '02':
            resp03 = q03_op02
        elif op3[:2] == '03':
            resp03 = q03_op03
        else:
            resp03 = 0

        # questao 04
        if op4[:2] == '01':
            resp04 = q04_op01
        elif op4[:2] == '02':
            resp04 = q04_op02
        elif op4[:2] == '03':
            resp04 = q04_op03
        else:
            resp04 = 0

        soma = resp01 + resp02 + resp03 + resp04

        # resultado do teste // abre e le as informações no arquivo resultadoXX txt
        if soma > res01:
            with open('resultado01.txt', 'r') as arquivo:
                resultado = arquivo.read()
        elif soma > res03:
            with open('resultado02.txt', 'r') as arquivo:
                resultado = arquivo.read()
        else:
            with open('resultado03.txt', 'r') as arquivo:
                resultado = arquivo.read()

        # cria texto2 para exibir na janela
        resultadoTela = (f'Você obteve {resp01} pontos na questão 01\n'
                         f'Você obteve {resp02} pontos na questão 02\n'
                         f'Você obteve {resp03} pontos na questão 03\n'
                         f'Você obteve {resp04} pontos na questão 04\n'
                         f'\n'
                         f'Sua pontuação total no teste foi de {soma} pontos.\n'
                         f'\n'
                         f'O resultado do seu teste foi:\n'
                         f'{resultado}')

        # exibe o resultado na janela
        self.recriarFrame2()
        self.lbl = tk.Label(self.fr2, text='RESULTADOS', font=('Verdana', 12))
        self.lbl.pack(padx=5, pady=5)
        self.txtarea = scrolledtext.ScrolledText(self.fr2, font=('Calibri', 12), wrap=tk.WORD)
        self.txtarea.insert(tk.INSERT, resultadoTela)
        self.txtarea.config(state=tk.DISABLED)  # torna o scrolledtext somente leitura
        self.txtarea.pack(expand=True, fill=tk.X)

    def enviar_email(self):
        global resultadoTela, email_cli, meu_email, assunto_mail, password_mail, corpo_email
        msg_email = corpo_email + '\n' + resultadoTela
        if not valores:
            self.msg = messagebox.showinfo('Informação', 'Você não checou se há novas respostas!')
        else:
            self.msg = messagebox.askquestion('Confirma', 'Deseja enviar o email agora?')
            if self.msg == 'yes':
                # este bloco abaixo envia um email com corpo do email no formato HTML
                msg = email.message.Message()
                msg['Subject'] = assunto_mail
                msg['From'] = meu_email
                msg['To'] = email_cli
                password = password_mail
                msg.set_payload(msg_email)

                s = smtplib.SMTP('smtp.gmail.com: 587')
                s.starttls()

                s.login(msg['From'], password)
                s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
                s.sendmail(msg['From'], meu_email, msg.as_string().encode('utf-8'))  # enviar email cópia para meu email
                self.msg = messagebox.showinfo('Informação', 'Email com o resultado enviado!')

                # altera a celula anotacoes da linha em uso
                valores_add = [['XXXXX']]
                result = sheet.values().update(spreadsheetId=ID_planilha,
                                               range=f'{folha}!J{n}', valueInputOption='USER_ENTERED',
                                               body={'values': valores_add}).execute()

    def limpar_resp(self):
        self.msg = messagebox.showinfo('Informação', 'Faça a exclusão manual das linhas na planilha de '
                                                     'respostas no Google Drive! IMPORTANTE: não apague '
                                                     'os dados, exclua as linhas.')

    def executa_dados(self):
        exec(open('dados_usuario.py').read())

    def executa_result01(self):
        exec(open('resultado01.py').read())

    def executa_result02(self):
        exec(open('resultado02.py').read())

    def executa_result03(self):
        exec(open('resultado03.py').read())

    def executa_corpoEmail(self):
        exec(open('corpo_email.py').read())

    def executa_valores(self):
        exec(open('valores_teste.py').read())

janelaRaiz = tk.Tk()
tela(janelaRaiz)
janelaRaiz.mainloop()
