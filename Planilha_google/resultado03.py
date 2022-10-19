import tkinter as tk
from tkinter import scrolledtext


class tela:

    def __init__(self, master):
        # abrir e ler as informações no arquivo resultado03.txt
        with open('resultado03.txt', 'r') as arquivo:
            texto = arquivo.read()

        self.janela5 = master
        self.janela5.title('Resultado 03')
        # self.janelaPrincipal.iconbitmap('imagens/bandeira.ico')
        # self.principal.configure(background='lightblue')

        self.lbl = tk.Label(self.janela5, text='Entre com o texto para a resposta 03', font=('Calibri', 12))
        self.lbl.pack(padx=5, pady=5)
        self.txtarea = scrolledtext.ScrolledText(self.janela5, font=('Calibri', 12), wrap=tk.WORD)
        self.txtarea.insert(tk.INSERT, texto)
        self.txtarea.config(state=tk.DISABLED)  # torna o scrolledtext somente leitura
        self.txtarea.pack(padx=15, pady=15)

        self.fr1 = tk.Frame(self.janela5)
        self.fr1.pack(padx=10, pady=10)
        self.btn1 = tk.Button(self.fr1, text='Editar', width=10, command=self.editar)
        self.btn2 = tk.Button(self.fr1, text='Gravar', width=10, command=self.gravar)
        self.btn3 = tk.Button(self.fr1, text='Cancelar', width=10, command=self.janela5.destroy)
        self.btn1.grid(row=0, column=0)
        self.btn2.grid(row=0, column=1)
        self.btn3.grid(row=0, column=2)

    def editar(self):
        self.txtarea.config(state=tk.NORMAL)  # torna o scrolledtext editavel

    def gravar(self):
        # coleta os dados do entry e armazena no dicionario 'dados'
        conteudo = self.txtarea.get('1.0', tk.END)

        # gravar informações no arquivo cadastro.txt
        with open('resultado03.txt', 'w') as arquivo:
            arquivo.write(conteudo)

        # fecha a janela4
        self.janela5.destroy()

janelaRaiz = tk.Tk()
tela(janelaRaiz)
janelaRaiz.mainloop()
