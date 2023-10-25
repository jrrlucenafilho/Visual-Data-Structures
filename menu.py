import tkinter as tk
import os

root = tk.Tk()
root.title("Menu")

# Ajuste do tamanho da janela principal para 1280x720
root.geometry("1280x740")


#função para chamar as GUI de cada lista
def Abrir_arquivo(file_name):
    os.system(f"python {file_name}")


#funções para os botôes
def Abrir_arquivo1():
    Abrir_arquivo("LSQ/LSQ_GUI.py")

def Abrir_arquivo2():
    Abrir_arquivo("LSE/LSE_GUI.py")

def Abrir_arquivo3():
    Abrir_arquivo("LDE/DoublyLinkedList_GUI.py")

def Abrir_arquivo4():
    Abrir_arquivo("FS/FilaSeq_GUI.py")

def Abrir_arquivo5():
    Abrir_arquivo("PS/PilhaSeq_GUI.py")

def Abrir_arquivo6():
    Abrir_arquivo("ABP/ABP_GUI.py")

# Definição de cores azul e cinza
cor_azul = "#3498db"
cor_cinza = "#bdc3c7"

# Ajustando a altura da faixa
faixa_cinza = tk.Frame(root, bg=cor_cinza, height=100)
faixa_cinza.pack(fill="x")  # Preenche horizontalmente

# Configurando o tamanho da fonte e a cor do texto
label = tk.Label(faixa_cinza, text="Implementação Gráfica De Estruturas de Dados",
                 font=("Arial", 18), fg="black", background=cor_cinza)
# Adicionando um espaço vertical entre o texto e a faixa cinza
label.pack(pady=20)

# Criando um Frame para o fundo branco
fundo_branco = tk.Frame(root, bg="white")
fundo_branco.pack(fill="both", expand=True)

#Criando labelframes para a parte 1 e 2 do projeto
parte_1_label_frame = tk.LabelFrame(fundo_branco, text="Projeto 1", width=50, bg="white", font=("Arial",13,"bold"), fg="black")
parte_2_label_frame = tk.LabelFrame(fundo_branco, text="Projeto 2", width=50, bg="white", font=("Arial",13,"bold"), fg="black")

# Criando botões retangulares para abrir os arquivos
botao1 = tk.Button(parte_1_label_frame, text="Lista Sequencial",
                    width=50, height=3, font= 40, background= cor_azul,  command=Abrir_arquivo1)
botao2 = tk.Button(parte_1_label_frame, text="Lista Simplesmente Encadeada",
                    width=50, height=3, font=40, background=cor_azul, command=Abrir_arquivo2)
botao3 = tk.Button(parte_1_label_frame, text="Lista Duplamente Encadeada",
                    width=50, height=3, font=40, background=cor_azul, command=Abrir_arquivo3)
botao4 = tk.Button(parte_2_label_frame, text="Fila Sequencial",
                    width=50, height=3, font=40, background=cor_azul, command=Abrir_arquivo4)
botao5 = tk.Button(parte_2_label_frame, text="Pilha Sequencial",
                    width=50, height=3, font=40, background=cor_azul, command=Abrir_arquivo5)
botao6 = tk.Button(parte_2_label_frame, text="Árvore Binária de Busca",
                    width=50, height=3, font=40, background=cor_azul, command=Abrir_arquivo6)

#Poicionando LabelFrames
parte_1_label_frame.pack(side="left", padx=30, pady=10)
parte_2_label_frame.pack(side="right", padx=30, pady=10)

# Posicionando os botões no centro do Frame
botao1.pack(padx=10, pady=10)
botao2.pack(padx=10, pady=10)
botao3.pack(padx=10, pady=10)
botao4.pack(padx=10, pady=10)
botao5.pack(padx=10, pady=10)
botao6.pack(padx=10, pady=10)


root.mainloop()
