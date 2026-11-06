import tkinter as tk
from tkinter import messagebox

# Variáveis da calculadora
primeiro_numero = 0
operacao = ""

# Função para digitar números
def digitar(numero):
    visor.insert(tk.END, numero)

# Função para escolher a operação
def escolher_operacao(op):
    global primeiro_numero, operacao

    primeiro_numero = float(visor.get())
    operacao = op
    visor.delete(0, tk.END)

# Função para calcular
def calcular():
    global primeiro_numero, operacao

    segundo_numero = float(visor.get())

    if operacao == "+":
        resultado = primeiro_numero + segundo_numero

    elif operacao == "-":
        resultado = primeiro_numero - segundo_numero

    elif operacao == "x":
        resultado = primeiro_numero * segundo_numero

    elif operacao == "/":
        if segundo_numero == 0:
            messagebox.showerror("Erro", "Não é possível dividir por zero!")
            visor.delete(0, tk.END)
            return
        resultado = primeiro_numero / segundo_numero

    visor.delete(0, tk.END)

    if resultado == int(resultado):
        visor.insert(tk.END, str(int(resultado)))
    else:
        visor.insert(tk.END, str(resultado))

    operacao = ""

# Função para limpar
def limpar():
    global primeiro_numero, operacao

    visor.delete(0, tk.END)
    primeiro_numero = 0
    operacao = ""

# Função para apagar o último número
def apagar():
    texto = visor.get()

    visor.delete(0, tk.END)
    visor.insert(0, texto[:-1])

# Função para colocar vírgula decimal
def decimal():
    texto = visor.get()

    if "." not in texto:
        visor.insert(tk.END, ".")


# Criando a janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x350")
janela.resizable(False, False)

# Criando o visor
visor = tk.Entry(janela, font=("Arial", 20), justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

# Botões da primeira linha
tk.Button(janela, text="C", width=6, command=limpar).grid(row=1, column=0, padx=2, pady=2)

tk.Button(janela, text="⌫", width=6, command=apagar).grid(row=1, column=1, padx=2, pady=2)

tk.Button(janela, text="/", width=6, command=lambda: escolher_operacao("/")).grid(row=1, column=2, padx=2, pady=2)

tk.Button(janela, text="x", width=6, command=lambda: escolher_operacao("x")).grid(row=1, column=3, padx=2, pady=2)

# Segunda linha
tk.Button(janela, text="7", width=6, command=lambda: digitar("7")).grid(row=2, column=0, padx=2, pady=2)

tk.Button(janela, text="8", width=6, command=lambda: digitar("8")).grid(row=2, column=1, padx=2, pady=2)

tk.Button(janela, text="9", width=6, command=lambda: digitar("9")).grid(row=2, column=2, padx=2, pady=2)

tk.Button(janela, text="-", width=6, command=lambda: escolher_operacao("-")).grid(row=2, column=3, padx=2, pady=2)

# Terceira linha
tk.Button(janela, text="4", width=6, command=lambda: digitar("4")).grid(row=3, column=0, padx=2, pady=2)

tk.Button(janela, text="5", width=6, command=lambda: digitar("5")).grid(row=3, column=1, padx=2, pady=2)

tk.Button(janela, text="6", width=6, command=lambda: digitar("6")).grid(row=3, column=2, padx=2, pady=2)

tk.Button(janela, text="+", width=6, command=lambda: escolher_operacao("+")).grid(row=3, column=3, padx=2, pady=2)

# Quarta linha
tk.Button(janela, text="1", width=6, command=lambda: digitar("1")).grid(row=4, column=0, padx=2, pady=2)

tk.Button(janela, text="2", width=6, command=lambda: digitar("2")).grid(row=4, column=1, padx=2, pady=2)

tk.Button(janela, text="3", width=6, command=lambda: digitar("3")).grid(row=4, column=2, padx=2, pady=2)

tk.Button(janela, text="=", width=6, command=calcular).grid(row=4, column=3, rowspan=2, padx=2, pady=2)

# Quinta linha
tk.Button(janela, text="0", width=15, command=lambda: digitar("0")).grid(row=5, column=0, columnspan=2, padx=2, pady=2)

tk.Button(janela, text=".", width=6, command=decimal).grid(row=5, column=2, padx=2, pady=2)

# Mantém a janela aberta
janela.mainloop()