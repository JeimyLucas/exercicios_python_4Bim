import tkinter as tk

def somar():
    n1 = float(entry1.get())
    n2 = float(entry2.get())

    result = n1 + n2

    lbl_result.config(text=f"Resultado: {result}")


janela = tk.TK()
janela.title("Calculadora")
janela.geometry("350x250")


lbl_num1 = tk.Label(janela, text="Primeiro número: ")
lbl_num1.pack() #posiciona o componente na janela

entry1 = tk.Entry(janela)
entry1.pack()


lbl_num2 = lbl_num2 = tk.Label(janela, text="Segundo número: ")
lbl_num2.pack()

entry2 = tk.Entry(janela)
entry2.pack()

# criando o botão e associando com a função
botao_somar = tk.Button(
    janela,
    text="Somar",
    command=somar # se o parenteses não for colocado, a função será chamada apenas no clique
)
botao_somar.pack(pady=15) #pady adiciona espaço vertical ao redor do botão, como se fosse o padding do css


lbl_result = lbl_result = tk.Label(janela, text="Resultado: ")
lbl_result.pack()

janela.mainloop() #mantem a janela aberta e aguardando as ações do usuário
