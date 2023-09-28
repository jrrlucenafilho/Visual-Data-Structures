import tkinter as tk
from tkinter import messagebox
from LSE import ListaEncadeadaSimples

# Função para exibir a lista na GUI
def exibir_lista():
    resultado.delete("all")  # Limpa todos os desenhos anteriores
    x, y = 100, 100  # Posição inicial para desenhar os quadrados
    quadrados = []
    largura_maxima = 1100  # Largura máxima para uma linha (alterada para 1100)
    largura_quadrado = 80  # Largura dos quadrados
    distancia_entre_quadrados = 20  # Distância entre os quadrados
    margem_direita = 40  # Margem entre o quadrado e o limite direito do canvas

    # Adiciona o quadrado "Head" no início
    quadrado_head = resultado.create_rectangle(x, y, x + largura_quadrado, y + 80, outline="black", width=2, fill="lightblue")
    resultado.create_text(x + largura_quadrado / 2, y + 40, text="Head", font=("Arial", 16), fill="black")
    quadrados.append(quadrado_head)
    x += largura_quadrado + distancia_entre_quadrados + margem_direita  # Adiciona a margem

    for i in range(1, minhaLista.tamanho() + 1):
        dado = minhaLista.elemento(i)

        quadrado = resultado.create_rectangle(x, y, x + largura_quadrado, y + 80, outline="black", width=2, fill="lightblue")
        resultado.create_text(x + largura_quadrado / 2, y + 40, text=str(dado), font=("Arial", 16), fill="black")
        quadrados.append(quadrado)
        x += largura_quadrado + distancia_entre_quadrados + margem_direita  # Adiciona a margem

    # Atualiza o contador de elementos
    contador_label.config(text=f"Total de elementos: {minhaLista.tamanho()}")

    # Calcula a largura total dos quadrados desenhados
    largura_total = x - distancia_entre_quadrados

    # Atualiza a largura do canvas para acomodar todos os quadrados
    resultado.config(scrollregion=(0, 0, largura_total, 500))

    # Adiciona uma barra de rolagem horizontal na parte inferior do canvas
    scrollbar_horizontal = tk.Scrollbar(root, orient="horizontal", command=resultado.xview)
    resultado.configure(xscrollcommand=scrollbar_horizontal.set)
    scrollbar_horizontal.grid(row=5, column=0, columnspan=6, sticky="ew")

    # Desenhar setas na direção horizontal
    for i in range(len(quadrados) - 1):
        x1, y1, x2, y2 = resultado.coords(quadrados[i])
        x3, y3, x4, y4 = resultado.coords(quadrados[i + 1])

        # Calcula a posição para a seta conectar os quadrados horizontalmente
        x_meio_quadrado1 = x1 + largura_quadrado
        x_meio_quadrado2 = x3

        seta = resultado.create_line(x_meio_quadrado1, y1 + 40, x_meio_quadrado2, y1 + 40, arrow=tk.LAST, width=2, fill="black")

    # Contador de elementos
    contador = minhaLista.tamanho()

# Função para inserir um elemento na lista com base nos valores dos campos de entrada
def inserir_elemento():
    posicao = posicao_entry.get()
    valor = valor_entry.get()

    if not posicao or not valor:
        messagebox.showerror("Erro", "Preencha o campo de entrada.")
        return

    try:
        posicao = int(posicao)
        valor = int(valor)
    except ValueError:
        messagebox.showerror("Erro", "Posição e valor devem ser números inteiros.")
        return

    if posicao < 1 or posicao > minhaLista.tamanho() + 1:
        messagebox.showerror("Erro", "Posição de inserção inválida.")
        return

    resultado.delete("all")
    minhaLista.insere(posicao, valor)
    exibir_lista()

# Função para remover um elemento da lista com base no valor do campo de entrada
def remover_elemento():
    posicao = remover_entry.get()

    if not posicao:
        messagebox.showerror("Erro", "Preencha o campo de remoção.")
        return

    try:
        posicao = int(posicao)
    except ValueError:
        messagebox.showerror("Erro", "Posição de remoção deve ser um número inteiro.")
        return

    if posicao < 1 or posicao > minhaLista.tamanho():
        messagebox.showerror("Erro", "Posição de remoção inválida.")
        return

    dado = minhaLista.remove(posicao)
    exibir_lista()
    removido_label.config(text=f"Dado removido = {dado}")

    # Atualiza o contador de elementos após a remoção
    contador_label.config(text=f"Total de elementos: {minhaLista.tamanho()}")

# Função para buscar um elemento por valor na lista
def buscar_por_valor():
    valor = buscar_valor_entry.get()

    if not valor:
        messagebox.showerror("Erro", "Preencha o campo de busca.")
        return

    try:
        valor = int(valor)
    except ValueError:
        messagebox.showerror("Erro", "Valor de busca deve ser um número inteiro.")
        return

    posicoes = minhaLista.busca_valor(valor)

    if posicoes:
        positions_str = ', '.join(map(str, posicoes))
        messagebox.showinfo("Resultado", f"Elemento {valor} encontrado nas posições: {positions_str}")
    else:
        messagebox.showinfo("Resultado", f"Elemento {valor} não encontrado na lista.")

# Função para buscar um elemento por posição na lista
def buscar_por_posicao():
    posicao = buscar_posicao_entry.get()

    if not posicao:
        messagebox.showerror("Erro", "Preencha ambos os campos de entrada.")
        return

    try:
        posicao = int(posicao)
    except ValueError:
        messagebox.showerror("Erro", "Posição de busca deve ser um número inteiro.")
        return

    if posicao < 1 or posicao > minhaLista.tamanho():
        messagebox.showerror("Erro", "Posição de busca inválida.")
        return

    elemento = minhaLista.busca_posicao(posicao)
    messagebox.showinfo("Resultado", f"Elemento na posição {posicao}: {elemento}")

# Criação da janela principal
root = tk.Tk()
root.title("Lista Encadeada Simples")

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
inserir_button = tk.Button(root, text="Inserir", command=inserir_elemento, **estilo_botao)

remover_label = tk.Label(root, text="Posição para remover:", **estilo_label)
remover_entry = tk.Entry(root, **estilo_entry)
remover_button = tk.Button(root, text="Remover", command=remover_elemento, **estilo_botao)

# Criação de um canvas maior para desenhar os quadrados e setas
resultado = tk.Canvas(root, width=1260, height=500, bg="white", scrollregion=(0, 0, 1260, 500))

removido_label = tk.Label(root, text="", **estilo_label)

# Rótulo para exibir o contador de elementos
contador_label = tk.Label(root, text="Total de elementos: 0", **estilo_label)

# Widgets para busca por valor
buscar_valor_label = tk.Label(root, text="Buscar por valor:", **estilo_label)
buscar_valor_entry = tk.Entry(root, **estilo_entry)
buscar_valor_button = tk.Button(root, text="Buscar", command=buscar_por_valor, **estilo_botao)

# Widgets para busca por posição
buscar_posicao_label = tk.Label(root, text="Buscar por posição:", **estilo_label)
buscar_posicao_entry = tk.Entry(root, **estilo_entry)
buscar_posicao_button = tk.Button(root, text="Buscar", command=buscar_por_posicao, **estilo_botao)

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
minhaLista = ListaEncadeadaSimples()

# Inicialização da interface gráfica
root.mainloop()
