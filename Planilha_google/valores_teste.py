import tkinter as tk
from tkinter import messagebox

class tela:

    def criarfr2(self):
        # abrir e ler as informações no arquivo valores_teste txt
        with open('valores_teste.txt', 'r') as arquivo:
            valores = arquivo.readlines()

        # carrega as variaveis com os dados
        q01_op01 = (valores[1][:-1])
        q01_op02 = (valores[3][:-1])
        q01_op03 = (valores[5][:-1])
        q02_op01 = (valores[7][:-1])
        q02_op02 = (valores[9][:-1])
        q02_op03 = (valores[11][:-1])
        q03_op01 = (valores[13][:-1])
        q03_op02 = (valores[15][:-1])
        q03_op03 = (valores[17][:-1])
        q04_op01 = (valores[19][:-1])
        q04_op02 = (valores[21][:-1])
        q04_op03 = (valores[23][:-1])
        res01 = (valores[25][:-1])
        res02fim = (valores[27][:-1])
        res02ini = (valores[29][:-1])
        res03 = (valores[31][:-1])

        self.fr2 = tk.Frame(self.janela7, width=720, height=550)
        self.fr2.pack(padx=5, pady=5)

        self.tit_altera = tk.Label(self.fr2, text='VALORES PARA USO NO TESTE', font=('Calibri', 12, 'bold'))
        self.tit_altera.place(x=360, y=20, anchor=tk.CENTER)

        tk.Label(self.fr2, text='Pergunta 01 - Op 01:').place(x=135, y=50, anchor=tk.E)
        tk.Label(self.fr2, text='              Op 02:').place(x=135, y=75, anchor=tk.E)
        tk.Label(self.fr2, text='              Op 03:').place(x=135, y=100, anchor=tk.E)
        self.entry_q1op1 = tk.Entry(self.fr2, width=4)  # criar os campos
        self.entry_q1op2 = tk.Entry(self.fr2, width=4)
        self.entry_q1op3 = tk.Entry(self.fr2, width=4)
        self.entry_q1op1.insert(0, q01_op01)  # exibir os valores nos campos
        self.entry_q1op2.insert(0, q01_op02)
        self.entry_q1op3.insert(0, q01_op03)
        self.entry_q1op1.place(x=140, y=50, anchor=tk.W)  # colocar os campos com valores na tela
        self.entry_q1op2.place(x=140, y=75, anchor=tk.W)
        self.entry_q1op3.place(x=140, y=100, anchor=tk.W)

        tk.Label(self.fr2, text='Pergunta 02 - Op 01:').place(x=310, y=50, anchor=tk.E)
        tk.Label(self.fr2, text='              Op 02:').place(x=310, y=75, anchor=tk.E)
        tk.Label(self.fr2, text='              Op 03:').place(x=310, y=100, anchor=tk.E)
        self.entry_q2op1 = tk.Entry(self.fr2, width=4)  # criar os campos
        self.entry_q2op2 = tk.Entry(self.fr2, width=4)
        self.entry_q2op3 = tk.Entry(self.fr2, width=4)
        self.entry_q2op1.insert(0, q02_op01)  # exibir os valores nos campos
        self.entry_q2op2.insert(0, q02_op02)
        self.entry_q2op3.insert(0, q02_op03)
        self.entry_q2op1.place(x=315, y=50, anchor=tk.W)  # colocar os campos com valores na tela
        self.entry_q2op2.place(x=315, y=75, anchor=tk.W)
        self.entry_q2op3.place(x=315, y=100, anchor=tk.W)

        tk.Label(self.fr2, text='Pergunta 03 - Op 01:').place(x=500, y=50, anchor=tk.E)
        tk.Label(self.fr2, text='              Op 02:').place(x=500, y=75, anchor=tk.E)
        tk.Label(self.fr2, text='              Op 03:').place(x=500, y=100, anchor=tk.E)
        self.entry_q3op1 = tk.Entry(self.fr2, width=4)  # criar os campos
        self.entry_q3op2 = tk.Entry(self.fr2, width=4)
        self.entry_q3op3 = tk.Entry(self.fr2, width=4)
        self.entry_q3op1.insert(0, q03_op01)  # exibir os valores nos campos
        self.entry_q3op2.insert(0, q03_op02)
        self.entry_q3op3.insert(0, q03_op03)
        self.entry_q3op1.place(x=500, y=50, anchor=tk.W)  # colocar os campos com valores na tela
        self.entry_q3op2.place(x=500, y=75, anchor=tk.W)
        self.entry_q3op3.place(x=500, y=100, anchor=tk.W)

        tk.Label(self.fr2, text='Pergunta 04 - Op 01:').place(x=680, y=50, anchor=tk.E)
        tk.Label(self.fr2, text='              Op 02:').place(x=680, y=75, anchor=tk.E)
        tk.Label(self.fr2, text='              Op 03:').place(x=680, y=100, anchor=tk.E)
        self.entry_q4op1 = tk.Entry(self.fr2, width=4)  # criar os campos
        self.entry_q4op2 = tk.Entry(self.fr2, width=4)
        self.entry_q4op3 = tk.Entry(self.fr2, width=4)
        self.entry_q4op1.insert(0, q04_op01)  # exibir os valores nos campos
        self.entry_q4op2.insert(0, q04_op02)
        self.entry_q4op3.insert(0, q04_op03)
        self.entry_q4op1.place(x=685, y=50, anchor=tk.W)  # colocar os campos com valores na tela
        self.entry_q4op2.place(x=685, y=75, anchor=tk.W)
        self.entry_q4op3.place(x=685, y=100, anchor=tk.W)

        tk.Label(self.fr2, text='Acima de :').place(x=355, y=140, anchor=tk.E)
        tk.Label(self.fr2, text='Entre:').place(x=355, y=165, anchor=tk.E)
        tk.Label(self.fr2, text='e').place(x=405, y=165, anchor=tk.E)
        tk.Label(self.fr2, text='Abaixo de:').place(x=355, y=195, anchor=tk.E)
        tk.Label(self.fr2, text='=> Resultado 01').place(x=440, y=140, anchor=tk.W)
        tk.Label(self.fr2, text='=> Resultado 02').place(x=440, y=165, anchor=tk.W)
        tk.Label(self.fr2, text='=> Resultado 03').place(x=440, y=195, anchor=tk.W)
        self.entry_res01 = tk.Entry(self.fr2, width=4)  # criar os campos
        self.entry_res02fim = tk.Entry(self.fr2, width=4)
        self.entry_res02ini = tk.Entry(self.fr2, width=4)
        self.entry_res03 = tk.Entry(self.fr2, width=4)
        self.entry_res01.insert(0, res01)  # carrega os valores nos campos
        self.entry_res02fim.insert(0, res02fim)
        self.entry_res02ini.insert(0, res02ini)
        self.entry_res03.insert(0, res03)
        self.entry_res01.place(x=365, y=140, anchor=tk.W)  # colocar os campos com valores na tela
        self.entry_res02fim.place(x=365, y=165, anchor=tk.W)
        self.entry_res02ini.place(x=410, y=165, anchor=tk.W)
        self.entry_res03.place(x=365, y=195, anchor=tk.W)

        self.btn1_altera = tk.Button(self.fr2, text='Salvar', width=10, command=self.salvar)
        self.btn2_altera = tk.Button(self.fr2, text='Sair', width=10, command=self.janela7.destroy)
        self.btn1_altera.place(x=355, y=230, anchor=tk.E)
        self.btn2_altera.place(x=365, y=230, anchor=tk.W)


    def __init__(self, master):
        self.janela7 = master
        self.janela7.geometry('730x460')
        self.janela7.title('Valores para o teste')
        # self.janelaPrincipal.iconbitmap('imagens/bandeira.ico')
        # self.principal.configure(background='lightblue')

        self.criarfr2()

    def salvar(self):
        # coleta os dados do entry e armazena no dicionario 'dados'
        dados = dict()
        dados['questao01_op01'] = self.entry_q1op1.get()
        dados['questao01_op02'] = self.entry_q1op2.get()
        dados['questao01_op03'] = self.entry_q1op3.get()
        dados['questao02_op01'] = self.entry_q2op1.get()
        dados['questao02_op02'] = self.entry_q2op2.get()
        dados['questao02_op03'] = self.entry_q2op3.get()
        dados['questao03_op01'] = self.entry_q3op1.get()
        dados['questao03_op02'] = self.entry_q3op2.get()
        dados['questao03_op03'] = self.entry_q3op3.get()
        dados['questao04_op01'] = self.entry_q4op1.get()
        dados['questao04_op02'] = self.entry_q4op2.get()
        dados['questao04_op03'] = self.entry_q4op3.get()
        dados['resultado01'] = self.entry_res01.get()
        dados['resultado02fim'] = self.entry_res02fim.get()
        dados['resultado02ini'] = self.entry_res02ini.get()
        dados['resultado03'] = self.entry_res03.get()

        # gravar informações no arquivo cadastro.txt
        with open('valores_teste.txt', 'w') as arquivo:
            for k, item in dados.items():
                arquivo.write(f'>>>>{k}\n{item}\n')

        # self.msg = messagebox.showinfo('Informacao', 'Valores salvos com sucesso!')
        self.fr2.destroy()
        self.frameTemp = tk.Frame(self.janela7, width=720, height=100)
        self.frameTemp.pack()
        tk.Label(self.frameTemp, text='Dados salvos com sucesso!').place(x=360, y=20, anchor=tk.CENTER)
        tk.Button(self.frameTemp, text='Sair', width=10, command=self.janela7.destroy).place(x=355, y=70, anchor=tk.E)
        tk.Button(self.frameTemp, text='Continuar', width=10, command=self.continua).place(x=365, y=70, anchor=tk.W)

    def continua(self):
        self.frameTemp.destroy()
        self.criarfr2()

janelaRaiz = tk.Tk()
tela(janelaRaiz)
janelaRaiz.mainloop()
