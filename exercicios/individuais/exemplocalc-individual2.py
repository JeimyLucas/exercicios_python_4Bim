import tkinter as tk

janela = tk.TK()
janela.title("Teclado da calculadora")

# adicionando botões APENAS nas colunas
botao1 = tk.Button(janela, text="1", width=6)
botao1.grid(row=0, column=0)

botao2 = tk.Button(janela, text="2", width=6)
botao2.grid(row=0, column=1)

botao3 = tk.Button(janela, text="3", width=6)
botao3.grid(row=0, column=2)

janela.mainloop()