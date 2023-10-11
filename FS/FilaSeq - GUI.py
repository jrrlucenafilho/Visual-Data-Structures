import tkinter as tk
from tkinter import messagebox
from FilaSeq import FilaSeq

# Função para atualizar a interface gráfica com os elementos da fila
def atualizar_interface():
    canvas.delete("all")  # Limpa o canvas
    tamanho = fila.tamanho()
    largura_quadrado = 100
    altura_quadrado = 60

    # Loop para desenhar os quadrados na ordem inversa
    for i in range(tamanho):
        x = 50 + i * (largura_quadrado + 10)  # Coordenada x do quadrado
        valor = fila.dados[(fila.inicio + tamanho - i - 1) % fila.TAM_MAX]
        canvas.create_rectangle(x, 50, x + largura_quadrado, 90 + altura_quadrado, fill="lightblue")
        canvas.create_text(x + largura_quadrado / 2, 70 + altura_quadrado / 2, text=str(valor), font=("Arial", 16))

# Função para inserir um valor na fila
def inserir_valor():
    valor = entrada_elemento.get()
    if valor.isdigit():
        valor = int(valor)
        if fila.insere(valor):
            atualizar_interface()
        else:
            messagebox.showwarning("Fila Cheia", "A fila está cheia e não é possível inserir mais elementos.")
    else:
        messagebox.showwarning("Valor Inválido", "Digite um valor inteiro válido.")

# Função para remover um valor da fila
def remover_valor():
    if not fila.vazia():
        valor = fila.remove()
        atualizar_interface()
    else:
        messagebox.showwarning("Fila Vazia", "A fila está vazia e não é possível remover elementos.")

# Função para exibir o primeiro elemento da fila
def exibir_primeiro():
    valor = fila.primeiro()
    if valor != -1:
        messagebox.showinfo("Primeiro Elemento", f"O primeiro elemento da fila é: {valor}")
    else:
        messagebox.showwarning("Fila Vazia", "A fila está vazia!")

# Inicialização da fila
fila = FilaSeq(10)

# Criação da janela principal
root = tk.Tk()
root.title("Fila Sequencial")

# Ajuste do tamanho da janela principal
root.geometry("1280x600")

# Configuração da fonte global para Arial 14
fonte_global = ("Arial", 14)
root.option_add("*Font", fonte_global)

# Definição de cores azul e cinza
cor_azul = "#3498db"
cor_cinza = "#bdc3c7"

# Definição do fundo da janela principal como cinza
root.configure(bg=cor_cinza)

# Criação de elementos na GUI
label_elemento = tk.Label(root, text="Elemento:")
label_elemento.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entrada_elemento = tk.Entry(root)
entrada_elemento.grid(row=0, column=1, padx=10, pady=10, sticky="w")

botao_adicionar = tk.Button(root, text="Adicionar Elemento", command=inserir_valor, bg=cor_azul, fg="white")
botao_adicionar.grid(row=0, column=2, padx=10, pady=10)

botao_remover = tk.Button(root, text="Remover Elemento", command=remover_valor, bg=cor_azul, fg="white")
botao_remover.grid(row=0, column=3, padx=10, pady=10)

botao_exibir_primeiro = tk.Button(root, text="Exibir Primeiro", command=exibir_primeiro, bg=cor_azul, fg="white")
botao_exibir_primeiro.grid(row=0, column=4, padx=10, pady=10)

canvas = tk.Canvas(root, width=1260, height=500, bg="white", scrollregion=(0, 0, 1260, 500))
canvas.grid(row=1, column=0, columnspan=5, padx=10, pady=20)

atualizar_interface()

# Inicialização da interface gráfica
root.mainloop()
