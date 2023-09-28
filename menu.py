import tkinter as tk
import os
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Menu")

# Ajuste do tamanho da janela principal para 1280x720
root.geometry("1280x740")


#função para chamar as GUI de cada lista
def Abrir_arquivo(file_name):
    os.system(f"python {file_name}")


#funcções para os botôes
def Abrir_arquivo1():
    Abrir_arquivo("LSQ/LSQ_GUI.py")


def Abrir_arquivo2():
    Abrir_arquivo("LSE/LSE_GUI.py")


def Abrir_arquivo3():
    Abrir_arquivo("LDE/DoublyLinkedList_GUI.py")

# Definição de cores azul e cinza
cor_azul = "#3498db"
cor_cinza = "#bdc3c7"

# Ajustando a altura da faixa
faixa_cinza = tk.Frame(root, bg=cor_cinza, height=100)
faixa_cinza.pack(fill="x")  # Preenche horizontalmente

# Configurando o tamanho da fonte e a cor do texto
label = tk.Label(faixa_cinza, text="Implementação Gráfica Da Estrutura De Dados Lista",
                 font=("Arial", 18), fg="black", background=cor_cinza)
# Adicionando um espaço vertical entre o texto e a faixa cinza
label.pack(pady=20)

# Criando um Frame para o fundo branco
fundo_branco = tk.Frame(root, bg="white")
fundo_branco.pack(fill="both", expand=True)

# Criando botões retangulares para abrir os arquivos
botao1 = tk.Button(fundo_branco, text="Lista Sequencial",
                    width=50, height=3, font= 40, background= cor_azul,  command=Abrir_arquivo1)
botao2 = tk.Button(fundo_branco, text="Lista Simplesmente Encadeada",
                    width=50, height=3, font=40, background=cor_azul, command=Abrir_arquivo2)
botao3 = tk.Button(fundo_branco, text="Lista Duplamente Encadeada",
                    width=50, height=3, font=40, background=cor_azul, command=Abrir_arquivo3)

# Posicionando os botões no centro do Frame
botao1.pack(pady=(120, 10))
botao2.pack(pady=10)
botao3.pack(pady=(10, 120)) 


root.mainloop()
