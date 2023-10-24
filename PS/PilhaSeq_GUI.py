import tkinter as tk
from tkinter import messagebox
from PilhaSeq import PilhaSeq

# Função para atualizar a interface gráfica com os elementos da pilha
def atualizar_interface():
    canvas.delete("all") # Limpa o canvas
    tamanho = pilha.tamanho()
    largura_quadrado = 100
    altura_quadrado = 60
    margem_inferior = 20

    y = 50

    # Loop para desenhar os quadrados dos elementos
    for i in range(tamanho):
        x = 300
        valor = pilha.dados[tamanho - i - 1]
        canvas.create_rectangle(x, y, x + largura_quadrado, y + altura_quadrado, fill="lightblue")
        canvas.create_text(x + largura_quadrado / 2, y + altura_quadrado / 2, text=str(valor), font=("Arial", 16))
        y += altura_quadrado + 10

    y += margem_inferior

    # Criação de uma barra de rolagem vertical
    altura_total = y
    canvas.config(scrollregion=(0, 0, 1100, altura_total))

    vertical_scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vertical_scrollbar.set)
    vertical_scrollbar.grid(row=1, column=5, sticky="ns")

# Função para empilhar um valor na pilha
def empilhar_valor():
    valor = entrada_elemento.get()
    if valor.isdigit():
        valor = int(valor)
        if pilha.push(valor):
            atualizar_interface()
        else:
            messagebox.showwarning("Pilha Cheia", "A pilha está cheia e não é possível empilhar mais elementos.")
    else:
        messagebox.showwarning("Valor Inválido", "Digite um valor inteiro válido.")

# Função para desempilhar um valor da pilha
def desempilhar_valor():
    if not pilha.vazia():
        valor = pilha.pop()
        atualizar_interface()    
    else:
        messagebox.showwarning("Pilha Vazia", "A pilha está vazia e não é possível desempilhar elementos.")

# Função para exibir o elemento no topo da pilha
def mostrar_topo():
    if not pilha.vazia():
        topo = pilha.top()
        messagebox.showinfo("Elemento no Topo", f"O elemento no topo da pilha é: {topo}")
    else:
        messagebox.showwarning("Pilha Vazia", "A pilha está vazia, não há elemento no topo.")

# Inicialização da pilha
pilha = PilhaSeq(15)

# Criação da janela principal
root = tk.Tk()
root.title("Pilha Sequencial")

# Ajuste do tamanho da janela principal
root.geometry("1100x800")

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

botao_empilhar = tk.Button(root, text="Empilhar Elemento", command=empilhar_valor, bg=cor_azul, fg="white")
botao_empilhar.grid(row=0, column=2, padx=10, pady=10)

botao_desempilhar = tk.Button(root, text="Desempilhar Elemento", command=desempilhar_valor, bg=cor_azul, fg="white")
botao_desempilhar.grid(row=0, column=3, padx=10, pady=10)

botao_mostrar_topo = tk.Button(root, text="Mostrar Elemento no Topo", command=mostrar_topo, bg=cor_azul, fg="white")
botao_mostrar_topo.grid(row=0, column=4, padx=10, pady=10)

canvas = tk.Canvas(root, width=700, height=700, bg="white")
canvas.grid(row=1, column=0, columnspan=5, padx=10, pady=20)

atualizar_interface()

# Inicialização da interface gráfica
root.mainloop()
