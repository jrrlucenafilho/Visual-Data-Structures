import tkinter as tk
from LSQ import LSQ
from tkinter import messagebox

# Função para exibir a lista na GUI


def exibir_lista():
    resultado.delete("all")  # Limpa todos os desenhos anteriores
    x, y = 30, 100  # Posição inicial para desenhar os quadrados
    quadrados = []
    largura_quadrado = 80  # Largura dos quadrados

    for i in range(1, 16):

        if minhaLista.elemento(i) == False:
            dado = ""
        else: 
            
            dado = minhaLista.elemento(i)


        quadrado = resultado.create_rectangle(
            x, y, x + largura_quadrado, y + 80, outline="black", width=2, fill="lightblue")
        resultado.create_text(x + largura_quadrado / 2, y +
                              40, text=str(dado), font=("Arial", 16), fill="black")
        quadrados.append(quadrado)
        x += largura_quadrado
           # Adiciona a margem

    # Atualiza o contador de elementos
    contador_label.config(text=f"Total de elementos: {minhaLista.lista_tam()}")

    # Contador de elementos
    contador = minhaLista.lista_tam()



def inserir_elemento():

    print ("entrei no inserir")
    posicao = posicao_entry.get()
    valor = valor_entry.get()

    print(posicao)
    print(valor)

    if not posicao or not valor:
        messagebox.showerror("Erro", "Preencha o campo de entrada.")
        return

    try:
        posicao = int(posicao)
        valor = int(valor)
    except ValueError:
        messagebox.showerror(
            "Erro", "Posição e valor devem ser números inteiros.")
        return

    if posicao < 1 or posicao > minhaLista.lista_tam() + 1:
        messagebox.showerror("Erro", "Posição de inserção inválida.")
        return

    resultado.delete("all")
    
    if minhaLista.lista_cheia():
        messagebox.showerror("Erro", "A lista está cheia!")
    

    minhaLista.insere_dados(valor, posicao)

    

    exibir_lista()


def remover_elemento():
    posicao = remover_entry.get()

    if not posicao:
        messagebox.showerror("Erro", "Preencha o campo de remoção.")
        return

    try:
        posicao = int(posicao)
    except ValueError:
        messagebox.showerror(
            "Erro", "Posição de remoção deve ser um número inteiro.")
        return

    if posicao < 1 or posicao > minhaLista.lista_tam():
        messagebox.showerror("Erro", "Posição de remoção inválida.")
        return

    dado = minhaLista.remove(posicao)
    exibir_lista()
    removido_label.config(text=f"Dado removido = {dado}")

    # Atualiza o contador de elementos após a remoção
    contador_label.config(text=f"Total de elementos: {minhaLista.lista_tam()}")


def buscar_por_valor():
    valor = buscar_valor_entry.get()

    if not valor:
        messagebox.showerror("Erro", "Preencha o campo de busca.")
        return

    try:
        valor = int(valor)
    except ValueError:
        messagebox.showerror(
            "Erro", "Valor de busca deve ser um número inteiro.")
        return

    posicoes = []

    for i in range(1, minhaLista.lista_tam() + 1):
        if minhaLista.elemento(i) == valor:
            posicoes.append(i)

    if posicoes:
        positions_str = ', '.join(map(str, posicoes))
        messagebox.showinfo(
            "Resultado", f"Elemento {valor} encontrado nas posições: {positions_str}")
    else:
        messagebox.showinfo(
            "Resultado", f"Elemento {valor} não encontrado na lista.")



def buscar_por_posicao():
    posicao = buscar_posicao_entry.get()

    if not posicao:
        messagebox.showerror("Erro", "Preencha ambos os campos de entrada.")
        return

    try:
        posicao = int(posicao)
    except ValueError:
        messagebox.showerror(
            "Erro", "Posição de busca deve ser um número inteiro.")
        return

    if posicao < 1 or posicao > minhaLista.lista_tam():
        messagebox.showerror("Erro", "Posição de busca inválida.")
        return

    elemento = minhaLista.valor(posicao)
    messagebox.showinfo(
        "Resultado", f"Elemento na posição {posicao}: {elemento}")


# Criação da janela principal
root = tk.Tk()
root.title("Lista sequencial")


# Ajuste do tamanho da janela principal para 1280x720
root.geometry("1280x740")

# Definição de cores azul e cinza
cor_azul = "#3498db"
cor_cinza = "#bdc3c7"

# Definição do fundo da janela principal como cinza
root.configure(bg=cor_cinza)

# Criação de widgets
estilo_label = {"bg": cor_cinza, "font": ("Arial", 14), "fg": "black"}
estilo_entry = {"bg": "white", "font": ("Arial", 14), "width": 10}
estilo_botao = {"bg": cor_azul, "fg": "white", "font": ("Arial", 14)}

posicao_label = tk.Label(root, text="Posição:", **estilo_label)
valor_label = tk.Label(root, text="Valor:", **estilo_label)
posicao_entry = tk.Entry(root, **estilo_entry)
valor_entry = tk.Entry(root, **estilo_entry)
inserir_button = tk.Button(
    root, text="Inserir", command=inserir_elemento, **estilo_botao)

remover_label = tk.Label(root, text="Posição para remover:", **estilo_label)
remover_entry = tk.Entry(root, **estilo_entry)
remover_button = tk.Button(
    root, text="Remover", command=remover_elemento, **estilo_botao)

# Criação de um canvas maior para desenhar os quadrados e setas
resultado = tk.Canvas(root, width=1260, height=500,
                      bg="white", scrollregion=(0, 0, 1260, 500))

removido_label = tk.Label(root, text="", **estilo_label)

# Rótulo para exibir o contador de elementos
contador_label = tk.Label(root, text="Total de elementos: 0", **estilo_label)

# Widgets para busca por valor
buscar_valor_label = tk.Label(root, text="Buscar por valor:", **estilo_label)
buscar_valor_entry = tk.Entry(root, **estilo_entry)
buscar_valor_button = tk.Button(
    root, text="Buscar", command=buscar_por_valor, **estilo_botao)

# Widgets para busca por posição
buscar_posicao_label = tk.Label(
    root, text="Buscar por posição:", **estilo_label)
buscar_posicao_entry = tk.Entry(root, **estilo_entry)
buscar_posicao_button = tk.Button(
    root, text="Buscar", command=buscar_por_posicao, **estilo_botao)

# Layout dos widgets
posicao_label.grid(row=0, column=0, padx=10, pady=5)
valor_label.grid(row=0, column=2, padx=10, pady=5)
posicao_entry.grid(row=0, column=1, padx=10, pady=5)
valor_entry.grid(row=0, column=3, padx=10, pady=5)
inserir_button.grid(row=0, column=4, padx=10, pady=5)

remover_label.grid(row=1, column=0, padx=10, pady=5)
remover_entry.grid(row=1, column=1, padx=10, pady=5)
remover_button.grid(row=1, column=2, padx=10, pady=5)

buscar_valor_label.grid(row=2, column=0, padx=10, pady=5)
buscar_valor_entry.grid(row=2, column=1, padx=10, pady=5)
buscar_valor_button.grid(row=2, column=2, padx=10, pady=5)

buscar_posicao_label.grid(row=2, column=3, padx=10, pady=5)
buscar_posicao_entry.grid(row=2, column=4, padx=10, pady=5)
buscar_posicao_button.grid(row=2, column=5, padx=10, pady=5)

contador_label.grid(row=3, column=0, columnspan=6, padx=10, pady=10)

resultado.grid(row=4, column=0, columnspan=6, padx=10, pady=10)
removido_label.grid(row=5, column=0, columnspan=6, padx=10, pady=10)

# Criação de uma instância da classe ListaEncadeadaSimples
minhaLista = LSQ()
exibir_lista()

# Inicialização da interface gráfica
root.mainloop()




