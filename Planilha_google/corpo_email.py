import tkinter as tk
from tkinter import scrolledtext


class tela:

    def __init__(self, master):
        # abrir e ler as informações no arquivo resultado01.txt
        with open('corpo_email.txt', 'r') as arquivo:
            texto = arquivo.read()

        self.janela6 = master
        self.janela6.title('Corpo do E-mail')
        # self.janelaPrincipal.iconbitmap('imagens/bandeira.ico')
        # self.principal.configure(background='lightblue')

        self.lbl = tk.Label(self.janela6, text='Entre com o texto para o Corpo do E-mail', font=('Calibri', 12))
        self.lbl.pack(padx=5)
        self.txtarea = scrolledtext.ScrolledText(self.janela6, font=('Calibri', 12), wrap=tk.WORD)
        self.txtarea.insert(tk.INSERT, texto)
        self.txtarea.config(state=tk.DISABLED)  # torna o scrolledtext somente leitura
        self.txtarea.pack(padx=15, pady=15)

        self.fr1 = tk.Frame(self.janela6)
        self.fr1.pack(padx=10, pady=10)
        self.btn1 = tk.Button(self.fr1, text='Editar', width=10, command=self.editar)
        self.btn2 = tk.Button(self.fr1, text='Gravar', width=10, command=self.gravar)
        self.btn3 = tk.Button(self.fr1, text='Cancelar', width=10, command=self.janela6.destroy)
        self.btn1.grid(row=0, column=0)
        self.btn2.grid(row=0, column=1)
        self.btn3.grid(row=0, column=2)

    def editar(self):
        self.txtarea.config(state=tk.NORMAL)  # torna o scrolledtext editavel

    def gravar(self):
        # coleta os dados do entry e armazena no dicionario 'dados'
        conteudo = self.txtarea.get('1.0', tk.END)

        # gravar informações no arquivo cadastro.txt
        with open('corpo_email.txt', 'w') as arquivo:
            arquivo.write(conteudo)

        # fecha a janela3
        self.janela6.destroy()

janelaRaiz = tk.Tk()
tela(janelaRaiz)
janelaRaiz.mainloop()
