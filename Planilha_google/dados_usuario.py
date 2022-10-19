import tkinter as tk

ID_planilha = meu_email = password = assunto_mail = folha = coluna = ' '

class tela:
    def criaframe1(self):
        global ID_planilha, meu_email, password, assunto_mail, folha, coluna

        # abrir e ler as informações no arquivo cadastro.txt
        with open('cadastro.txt', 'r') as arquivo:
            texto = arquivo.readlines()

        # carrega as variaveis com os dados
        ID_planilha = (texto[1][:-1])
        meu_email = (texto[3][:-1])
        password = (texto[5][:-1])
        assunto_mail = (texto[7][:-1])
        folha = (texto[9][:-1])
        coluna = (texto[11][:-1])

        # criar a frame e seus widgets
        self.fr1 = tk.Frame(self.janela2, height=195, width=430)
        self.fr1.place(x=0, y=0)

        self.titulo = tk.Label(self.fr1, text='DADOS SALVOS NO CADASTRO', font=('Calibri', 12, 'bold'))
        self.titulo.place(x=275, y=20, anchor=tk.CENTER)
        tk.Label(self.fr1, text='Id da Planilha:').place(x=130, y=50, anchor=tk.E)
        tk.Label(self.fr1, text='E-mail google:').place(x=130, y=70, anchor=tk.E)
        tk.Label(self.fr1, text='Senha do e-mail (API):').place(x=130, y=90, anchor=tk.E)
        tk.Label(self.fr1, text='Assunto do e-mail:').place(x=130, y=110, anchor=tk.E)
        tk.Label(self.fr1, text='Nome da folha dados:').place(x=130, y=130, anchor=tk.E)
        tk.Label(self.fr1, text='Ultima coluna:').place(x=130, y=150, anchor=tk.E)
        tk.Label(self.fr1, text=ID_planilha).place(x=135, y=50, anchor=tk.W)
        tk.Label(self.fr1, text=meu_email).place(x=135, y=70, anchor=tk.W)
        tk.Label(self.fr1, text=password).place(x=135, y=90, anchor=tk.W)
        tk.Label(self.fr1, text=assunto_mail).place(x=135, y=110, anchor=tk.W)
        tk.Label(self.fr1, text=folha).place(x=135, y=130, anchor=tk.W)
        tk.Label(self.fr1, text=coluna).place(x=135, y=150, anchor=tk.W)

        self.btn1 = tk.Button(self.fr1, text='Alterar', width=10, command=self.alterar)
        self.btn2 = tk.Button(self.fr1, text='Sair', width=10, command=self.janela2.destroy)
        self.btn1.place(x=270, y=180, anchor=tk.E)
        self.btn2.place(x=280, y=180, anchor=tk.W)

    def __init__(self, master):
        self.janela2 = master
        self.janela2.geometry('550x465')
        self.janela2.title('Cadastro dos Dados')
        # self.janelaPrincipal.iconbitmap('imagens/bandeira.ico')
        # self.principal.configure(background='lightblue')

        self.criaframe1()  # chama a função para criar a frame1

    def alterar(self):
        global ID_planilha, meu_email, password, assunto_mail, folha, coluna

        self.fr2 = tk.Frame(self.janela2, height=250, width=530, borderwidth=1, relief='solid')
        self.fr2.place(x=10, y=200)

        tk.Label(self.fr2, text='DIGITE OS NOVOS DADOS', font=('Calibri', 12, 'bold')).place(x=265, y=20, anchor=tk.CENTER)
        tk.Label(self.fr2, text='Id da Planilha:').place(x=140, y=50, anchor=tk.E)
        tk.Label(self.fr2, text='E-mail google:').place(x=140, y=80, anchor=tk.E)
        tk.Label(self.fr2, text='Senha do e-mail (API):').place(x=140, y=110, anchor=tk.E)
        tk.Label(self.fr2, text='Assunto do e-mail:').place(x=140, y=140, anchor=tk.E)
        tk.Label(self.fr2, text='Nome da folha dados:').place(x=140, y=170, anchor=tk.E)
        tk.Label(self.fr2, text='Ultima coluna:').place(x=140, y=200, anchor=tk.E)
        self.entry_id = tk.Entry(self.fr2, width=50) # criar os campos
        self.entry_mail = tk.Entry(self.fr2, width=40)
        self.entry_pass = tk.Entry(self.fr2, width=30)
        self.entry_assunto = tk.Entry(self.fr2, width=60)
        self.entry_folha = tk.Entry(self.fr2, width=15)
        self.entry_coluna = tk.Entry(self.fr2, width=3)
        self.entry_id.insert(0, ID_planilha)  # carrega os valores nos campos
        self.entry_mail.insert(0, meu_email)
        self.entry_pass.insert(0, password)
        self.entry_assunto.insert(0, assunto_mail)
        self.entry_folha.insert(0, folha)
        self.entry_coluna.insert(0, coluna)
        self.entry_id.place(x=145, y=50, anchor=tk.W) # exibe os campos com valores na tela
        self.entry_mail.place(x=145, y=80, anchor=tk.W)
        self.entry_pass.place(x=145, y=110, anchor=tk.W)
        self.entry_assunto.place(x=145, y=140, anchor=tk.W)
        self.entry_folha.place(x=145, y=170, anchor=tk.W)
        self.entry_coluna.place(x=145, y=200, anchor=tk.W)

        self.btn1_altera = tk.Button(self.fr2, text='Gravar', width=10, command=self.gravar)
        self.btn2_altera = tk.Button(self.fr2, text='Cancelar', width=10, command=self.fr2.destroy)
        self.btn1_altera.place(x=260, y=230, anchor=tk.E)
        self.btn2_altera.place(x=270, y=230, anchor=tk.W)

    def gravar(self):
        # coleta os dados do entry e armazena no dicionario 'dados'
        dados = dict()
        dados['id_planilha'] = self.entry_id.get()
        dados['meu_email'] = self.entry_mail.get()
        dados['passwd'] = self.entry_pass.get()
        dados['assunto'] = self.entry_assunto.get()
        dados['nome_folha_dados'] = self.entry_folha.get()
        dados['ultima_coluna'] = self.entry_coluna.get()

        # gravar informações no arquivo cadastro.txt
        with open('cadastro.txt', 'w') as arquivo:
            for k, item in dados.items():
                arquivo.write(f'>>>>{k}\n{item}\n')

        # atualiza o frame 1
        self.fr1.destroy()
        self.criaframe1()

        # apaga a frame 2
        self.fr2.destroy()


janelaRaiz = tk.Tk()
tela(janelaRaiz)
janelaRaiz.mainloop()
