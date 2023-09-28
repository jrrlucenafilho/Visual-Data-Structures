from DoublyLinkedList import DoublyLinkedList
from tkinter import messagebox
import tkinter as tk

'''Show gui listing'''
def show_list():
    result.delete("all")
    x_pos, y_pos = 100, 100 #Starting square pos
    squares_list = []
    max_line_width = 1100
    square_width = 80
    dist_among_squares = 20
    right_margin = 40   #Regarding square-canvas

    #Adding the head square on startup
    head_square = result.create_rectangle(x_pos, y_pos, x_pos + square_width, y_pos + 80, outline="black", width=2, fill="lightblue")
    result.create_text(x_pos + square_width / 2, y_pos + 40, text="Head", font=("Arial", 16), fill="black")

    squares_list.append(head_square)
    x_pos += square_width + dist_among_squares + right_margin  #Adds margin

    #Adding a square for each list node
    for i in range(1, my_list.get_size() + 1):
        data = my_list.get_element(i)

        square = result.create_rectangle(x_pos, y_pos, x_pos + square_width, y_pos + 80, outline="black", width=2, fill="lightblue")
        result.create_text(x_pos + square_width / 2, y_pos + 40, text=str(data), font=("Arial", 16), fill="black")
        squares_list.append(square)
        x_pos += square_width + dist_among_squares + right_margin  #Adds margin

    #Adds tail Square on list's last element
    tail_right_margin = 20  #Regarding canvas and tail square

    tail_square = result.create_rectangle(x_pos, y_pos, x_pos + square_width, y_pos + 80, outline="black", width=2, fill="lightblue")
    result.create_text(x_pos + square_width / 2, y_pos + 40, text="Tail", font=("Arial", 16), fill="black")
    
    squares_list.append(tail_square)
    x_pos += square_width + dist_among_squares + right_margin + tail_right_margin  #Adds margin

    #Updates element counter
    counter_label.config(text=f"Total de elementos: {my_list.get_size()}")

    #Calcs total width of all squares
    total_width = x_pos - dist_among_squares

    #Updates the canvas' width to accomodate all squares
    result.config(scrollregion=(0, 0, total_width, 500))

    #Adds a scrollbar under the canvas
    horizontal_scrollbar = tk.Scrollbar(root, orient="horizontal", command=result.xview)
    result.configure(xscrollcommand=horizontal_scrollbar.set)
    horizontal_scrollbar.grid(row=5, column=0, columnspan=6, sticky="ew")

    #Draws horizontal arrows
    for i in range(len(squares_list) - 1):
        x1, y1, x2, y2 = result.coords(squares_list[i])
        x3, y3, x4, y4 = result.coords(squares_list[i + 1])

        #Calculates positions for square connections
        x_middle_of_square1 = x1 + square_width
        x_middle_of_square2 = x3

        if (i == 0) and (my_list.is_empty() is False):
            #Builds head arrow
            result.create_line(x_middle_of_square1, y1 + 40, x_middle_of_square2, y1 + 40, arrow=tk.LAST, width=2, fill="black")
        elif i == (len(squares_list) - 2) and (my_list.is_empty() is False):
            #Builds tail arrow
            result.create_line(x_middle_of_square1, y1 + 40, x_middle_of_square2, y1 + 40, arrow=tk.FIRST, width=2, fill="black")
        elif my_list.is_empty() is False:
            #Middle-of-list arrows
            result.create_line(x_middle_of_square1, y1 + 50, x_middle_of_square2, y1 + 50, arrow=tk.LAST, width=2, fill="black")
            result.create_line(x_middle_of_square1, y1 + 30, x_middle_of_square2, y1 + 30, arrow=tk.FIRST, width=2, fill="black")

'''Func to insert an element based on what's in the insert boxes'''
def insert_element_gui():
    position = entry_position.get()
    value = entry_value.get()

    if not position or not value:
        messagebox.showerror("Erro", "Preencha ambos os campos de entrada.")
        return

    try:
        position = int(position)
        value = int(value)
    except ValueError:
        messagebox.showerror("Erro", "Posição e valor devem ser números inteiros.")
        return

    if (position < 1) or (position > my_list.get_size() + 1):
        messagebox.showerror("Erro", "Posição de inserção inválida.")
        return

    result.delete("all")
    my_list.insert_element(position, value)
    show_list()

'''Func to remove an element based on what's on input boxes'''
def remove_element_gui():
    position = remove_entry.get()

    if not position:
        messagebox.showerror("Erro", "Preencha o campo de remoção.")
        return

    try:
        position = int(position)
    except ValueError:
        messagebox.showerror("Erro", "Posição de remoção deve ser um número inteiro.")
        return

    if (position < 1) or (position > my_list.get_size()):
        messagebox.showerror("Erro", "Posição de remoção inválida.")
        return

    data = my_list.remove_element(position)

    show_list()

    removed_label.config(text=f"Dado removido = {data}")

    #Updates the element counter after removal
    counter_label.config(text=f"Total de elementos: {my_list.get_size()}")

'''Search by value func'''
def search_by_value_gui():
    value = search_value_entry.get()

    if not value:
        messagebox.showerror("Erro", "Preencha o campo de busca.")
        return

    try:
        value = int(value)
    except ValueError:
        messagebox.showerror("Erro", "Valor de busca deve ser um número inteiro.")
        return

    positions = my_list.search_value_ocurrences(value)

    if positions:
        positions_str = ', '.join(map(str, positions))
        messagebox.showinfo("Resultado", f"Elemento {value} encontrado nas posições: {positions_str}")
    else:
        messagebox.showinfo("Resultado", f"Elemento {value} não encontrado na lista.")

'''Search by position func'''
def search_by_position_gui():
    position = search_entry_position.get()

    if not position:
        messagebox.showerror("Erro", "Preencha o campo de entrada.")
        return

    try:
        position = int(position)
    except ValueError:
        messagebox.showerror("Erro", "Posição de busca deve ser um número inteiro.")
        return

    if (position < 1) or (position > my_list.get_size()):
        messagebox.showerror("Erro", "Posição de busca inválida.")
        return

    element = my_list.search_element_by_pos(position)
    messagebox.showinfo("Resultado", f"Elemento na posição {position}: {element}")

#Main window creation
root = tk.Tk()
root.title("Lista Duplamente Encadeada")

#Set window resolution
root.geometry("1280x740")

#Color defs
color_blue = "#3498db"
color_gray = "#bdc3c7"

#Set bg color
root.configure(bg=color_gray)

#Widget settings
label_style = {"bg": color_gray, "font": ("Arial", 14), "fg": "black"}
entry_style = {"bg": "white", "font": ("Arial", 14), "width": 10}
button_style = {"bg": color_blue, "fg": "white", "font": ("Arial", 14)}

position_label = tk.Label(root, text="Posição:", **label_style)
value_label = tk.Label(root, text="Valor:", **label_style)
entry_position = tk.Entry(root, **entry_style)
entry_value = tk.Entry(root, **entry_style)
insert_button = tk.Button(root, text="Inserir", command=insert_element_gui, **button_style)

remove_label = tk.Label(root, text="Posição para remover:", **label_style)
remove_entry = tk.Entry(root, **entry_style)
remove_button = tk.Button(root, text="Remover", command=remove_element_gui, **button_style)

#Larger canvas for blocks and arrows
result = tk.Canvas(root, width=1260, height=500, bg="white", scrollregion=(0, 0, 1260, 500))

removed_label = tk.Label(root, text="", **label_style)

#Element counter label
counter_label = tk.Label(root, text="Total de elementos: 0", **label_style)

#Search-by-value widgets
search_value_label = tk.Label(root, text="Buscar por valor:", **label_style)
search_value_entry = tk.Entry(root, **entry_style)
search_value_button = tk.Button(root, text="Buscar", command=search_by_value_gui, **button_style)

#Search-by-pos widgets
search_position_label = tk.Label(root, text="Buscar por posição:", **label_style)
search_entry_position = tk.Entry(root, **entry_style)
search_position_button = tk.Button(root, text="Buscar", command=search_by_position_gui, **button_style)

#Widgets' layouts
position_label.grid(row=0, column=0, padx=10, pady=5)
value_label.grid(row=0, column=2, padx=10, pady=5)
entry_position.grid(row=0, column=1, padx=10, pady=5)
entry_value.grid(row=0, column=3, padx=10, pady=5)
insert_button.grid(row=0, column=4, padx=10, pady=5)

remove_label.grid(row=1, column=0, padx=10, pady=5)
remove_entry.grid(row=1, column=1, padx=10, pady=5)
remove_button.grid(row=1, column=2, padx=10, pady=5)

search_value_label.grid(row=2, column=0, padx=10, pady=5)
search_value_entry.grid(row=2, column=1, padx=10, pady=5)
search_value_button.grid(row=2, column=2, padx=10, pady=5)

search_position_label.grid(row=2, column=3, padx=10, pady=5)
search_entry_position.grid(row=2, column=4, padx=10, pady=5)
search_position_button.grid(row=2, column=5, padx=10, pady=5)

counter_label.grid(row=3, column=0, columnspan=6, padx=10, pady=10)

result.grid(row=4, column=0, columnspan=6, padx=10, pady=10)
removed_label.grid(row=5, column=0, columnspan=6, padx=10, pady=10)

#Instantiating list
my_list = DoublyLinkedList()

#tkinter gui init
root.mainloop()