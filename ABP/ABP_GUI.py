import tkinter as tk
from tkinter import messagebox
from time import sleep
from ABP import ABP

class ABP_GUI:
    def __init__(self, root):
        self.window = root

        #Canvas for tree visuals
        self.tree_canvas = tk.Canvas(self.window, width=1290, height=520, bg="white", relief="groove", bd=4, scrollregion=(0, 0, 1260, 500))
        self.tree_canvas.place(x=25, y=25)
        self.tree_canvas.grid(row=0, column=0, sticky="nsew")

        #Config canvas to fill it's horizontal space with the window's own
        self.window.grid_columnconfigure(0, weight=1)

        #Botton line
        self.below_canvas = tk.Canvas(self.window, width=1800, height=25, bg="light gray", relief="groove")
        self.below_canvas.place(x=0, y=765)

        #Setting up init vars
        self.color_blue = "#3498db" 
        self.color_gray = "#bdc3c7"
        self.null_word_label = None #Null that appears when tree is empty
        self.insert_node_button = None
        self.input_entry = None #Input writebox
        self.tree_node = None #Circle-Node
        self.input_label = None #Input label
        self.confirm_add_button = None #Smaller Add button for confirmation
        self.node_number_label = None #Text of number inside node
        self.remove_button = None   #Delete button 
        self.pre_order_traversal_button = None  #One button for each kind of traversal
        self.in_order_traversal_button = None
        self.post_order_traversal_button = None
        self.traversal_text = None #Text that'll pop up in a msgbox containing traversal result
        self.search_element_button = None
        self.chosen_input_option = None #Will diff between search and removal
        self.clear_tree_button = None   #Clears tree from traversal coloring

        #Setting up initial positions
        self.notation_index = 0
        self.vertical_counter = 0
        self.connect_arrow = 0
        self.go_right = 1
        self.go_left = 0
        self.position_controller = 0
        self.node_index = 0
        self.display_counter_box = -1

        #Node position and gap controllers
        self.label_x_position = 519
        self.label_y_position = 99 + 50
        self.gap_controller = 100
        
        #Init'ing lists
        #This one will hold the tree nodes themselves (the tree itself)
        self.node_value_holder = []
        #Used for traversing
        self.value_printer = []

        #First-to-be-called funcs
        self.build_null_root()
        self.build_buttons()

        #BiN Tree implm
        self.bin_tree = ABP()

        #Storing node labels here so as to get text later (when traversing)
        #Max is 16 (0-15) since tree height goes up to 4 (max 16 nodes)
        for i in range(15):
            self.value_printer.append(i)
            self.value_printer[i] = tk.Label(self.tree_canvas,text=" ", font=("Arial",15,"bold","italic"))

    #Builds root as null at beginning and it's arrow
    def build_null_root(self):
        root_label = tk.Label(self.tree_canvas, text="Raíz", font=("Arial",17,"bold"), fg="black", bg="white")
        root_label.place(x=575, y=10+50)

        #Calc arrow positions
        root_arrow = (595, 80+50, 595 - 15,(80 + 43) / 2+50, 595 - 5, (80 + 43) / 2+50, 595 - 5, 43+50, 595 + 5, 43+50, 595 + 5, (80 + 43) / 2+50, 595 + 15, (80 + 43) / 2+50)
        self.tree_canvas.create_polygon(root_arrow,  width=3, fill=self.color_blue, outline="black")

        #Null word
        self.null_word_label = tk.Label(self.tree_canvas, text="NULL", font=("Arial",17,"bold","italic"), fg="#2E37FE", bg="white")
        self.null_word_label.place(x=565, y=90+50)

    #UI buttons
    def build_buttons(self):
        #Insert button
        self.insert_node_button = tk.Button(self.window,text="Inserir",
                                            font=("Arial",17,"bold"),
                                            bg=self.color_blue,
                                            fg="white",
                                            relief="raised",
                                            bd=4,
                                            command=lambda: self.handle_input_setup(1),
                                            state="normal")
        self.insert_node_button.place(x=25, y=635)

        #Delete button
        self.remove_button = tk.Button(self.window,
                                       text="Remover",
                                       font=("Arial", 16, "bold"),
                                       bg=self.color_blue,
                                       fg="white",
                                       relief="raised",
                                       bd=4,
                                       command=lambda: self.handle_input_setup(2),
                                       state="normal")
        self.remove_button.place(x=220, y=635)

        #Search button
        self.search_element_button = tk.Button(self.window,
                                       text="Buscar",
                                       font=("Arial", 16, "bold"),
                                       bg=self.color_blue,
                                       fg="white",
                                       bd=4,
                                       command=lambda: self.handle_input_setup(3),
                                       state="normal")
        self.search_element_button.place(x=425, y=635)

        #LabelFrame to group traversal buttons
        traversal_menu_label_frame = tk.LabelFrame(self.window,
                                                text="Caminhamento",
                                                width=50,
                                                bg=self.color_gray,
                                                font=("Arial",13,"bold"),
                                                fg="black")
        traversal_menu_label_frame.place(x=1080, y=535)

        #1 button for each traversal type
        self.pre_order_traversal_button = tk.Button(traversal_menu_label_frame,
                                                    text="Pré-Ordem",
                                                    font=("Arial",10,"bold"),
                                                    bg=self.color_blue,
                                                    fg="white",
                                                    bd=4,
                                                    command=lambda: self.traversing_decision_making(1),
                                                    state="normal")
        self.pre_order_traversal_button.pack(padx=10, pady=5)

        self.in_order_traversal_button = tk.Button(traversal_menu_label_frame,
                                                   text="Em-Ordem",
                                                   font=("Arial", 10, "bold"),
                                                   bg=self.color_blue,
                                                   fg="white",
                                                   bd=4,
                                                   command=lambda: self.traversing_decision_making(2),
                                                   state="normal")
        self.in_order_traversal_button.pack(padx=10, pady=5)

        self.post_order_traversal_button = tk.Button(traversal_menu_label_frame,
                                                    text="Pós-Ordem",
                                                    font=("Arial", 10, "bold"),
                                                    bg=self.color_blue,
                                                    fg="white",
                                                    bd=4,
                                                    command=lambda: self.traversing_decision_making(3),
                                                    state="normal")
        self.post_order_traversal_button.pack(padx=10, pady=5)

        self.clear_tree_button = tk.Button(traversal_menu_label_frame,
                                                    text="Limpar",
                                                    font=("Arial", 10, "bold"),
                                                    bg=self.color_blue,
                                                    fg="white",
                                                    bd=4,
                                                    command=lambda: self.traversing_decision_making(4),
                                                    state="normal")
        self.clear_tree_button.pack(padx=10, pady=5)

    #Handles button behavior
    def handle_input_setup(self, option):
        #Eases life
        self.chosen_input_option = option

        self.disable_input_buttons()
        self.input_label = tk.Label(self.window, text="Insira um valor inteiro", fg="black", bg=self.color_gray, font=("Arial", 10, "bold"))
        self.input_label.place(x=725+30, y=610)

        self.input_entry = tk.Entry(self.window, fg=self.color_blue, bg="white", relief="sunken", bd=4, width=20, font=("Arial", 10, "bold"))
        self.input_entry.place(x=725+30, y=635)
        self.input_entry.focus()

        self.confirm_add_button = tk.Button(self.window, text="Insira", fg="white", bg=self.color_blue, relief="raised", bd=4, width=10, font=("Arial", 8, "bold"), state="normal")
        self.confirm_add_button.place(x=600+30, y=635)

        if option == 1:
            #Insert case
            self.confirm_add_button['text'] = "Inserir"
            self.window.unbind('<space>')
            self.confirm_add_button['command'] =  lambda: self.filter_input_value(False,option)
            self.window.bind('<Return>', lambda e: self.filter_input_value(e,option))

        elif option == 2:
            #Delete Case
            self.input_label['text'] = "Insira o valor a ser removido:"
            self.confirm_add_button['text'] = "Remover"
            self.window.unbind('<Return>')
            self.confirm_add_button['command'] = lambda: self.filter_input_value(False,option)
            self.window.bind('<space>', lambda e: self.filter_input_value(e, option))
        else:
            #Search element case (And clearing)
            self.input_label['text'] = "Insira o valor a ser pesquisado:"
            self.confirm_add_button['text'] = "Pesquisar"
            self.window.unbind('<Return>')
            self.confirm_add_button['command'] = lambda: self.filter_input_value(False,option)
            self.window.bind('<space>', lambda e: self.filter_input_value(e, option))

    #Warnings and such (for the 3 non-labelframe buttons)
    def filter_input_value(self, e, option):
        self.input_label.place_forget()
        self.input_entry.place_forget()
        self.confirm_add_button.place_forget()

        #Int check
        try:
            if(int(self.input_entry.get())):
                if option == 1: #Insert option
                    if(len(self.node_value_holder)) == 0:
                        self.null_word_label.place_forget()

                    self.build_root_node()
                elif option == 2:   #Remove option
                    if self.node_value_holder: #Empty check
                        self.remove_node()
                    else:
                        messagebox.showerror("Erro", "Árvore vazia, nada para remover")
                else: #3, Search option
                    if self.node_value_holder:
                        self.search_node()
                    else:
                        messagebox.showerror("Erro", "Árvore vazia, nada para buscar")
        except:
            messagebox.showerror("Erro", "Valor Inválido ou não encontrado")

        self.enable_input_buttons()

    #First node (root) added
    def build_root_node(self):
        try:
            self.tree_node = self.tree_canvas.create_oval(505, 85+50, 555, 135+50, width=2, fill="blue2", outline="black")
            self.node_number_label = tk.Label(self.window, text=self.input_entry.get(), fg="white", bg="blue2", font=("Arial", 12, "bold"))
            self.node_number_label.place(x=self.label_x_position, y=self.label_y_position)

            if len(self.node_value_holder) == 0:
                    self.push_first_node()
            else:
                self.notation_index = 0
                self.position_controller = 70 + 80 - 5
                self.node_index = 0
                temp_node_value = self.input_entry.get()
                self.go_right = 1
                self.gap_controller = 210   #Each row
                self.go_left = 0
                self.vertical_counter = 0

                #Node position control
                while True:
                    if self.go_right == 1:
                        if self.position_controller < 0:    #4th row moves slightly more to the side
                            self.position_controller = 25
                            self.left_movement_in_row()
                            self.position_controller = -1
                        else:
                            self.right_movement_in_row()
                    else:   #Here if node travels left
                        self.left_movement_in_row()

                    #Node Finds it's position
                    if (self.position_controller == -1) or (self.position_controller == 70+self.gap_controller-5) or (self.position_controller == 80+70+80+self.gap_controller-5):
                        break

                    #Compare with a node value and movement direction giving
                    if int(temp_node_value) < int(self.node_value_holder[self.node_index][2]):
                        self.decision_making_about_left_side_direction()
                    elif int(temp_node_value) > int(self.node_value_holder[self.node_index][2]):
                        self.decision_making_about_right_side_direction()
                    else:
                        messagebox.showerror("Erro","Valor já presente na ABP")
                        self.vertical_counter = 4
                        break

                    self.vertical_down_movement()

                    self.vertical_counter += 1
                    if self.vertical_counter > 3:
                        messagebox.showwarning("Restrição","ABP de no Máximo 4 de altura")
                        break
                    elif self.vertical_counter == 3:
                        #Shortened gap for 4th row
                        self.gap_controller -= 150
                    else:
                        #Gap for other rows
                        self.gap_controller -= 85

                    if self.go_right == 1:
                        self.right_moving_final_direction_giving()
                    elif self.go_left == 1:
                        self.left_moving_final_direction_giving()

            if self.vertical_counter <= 3:  #Till 4th row
                self.build_arrow()
            else:
                #Limits to 4 rows, warns and deletes rows that exceed it
                self.tree_canvas.delete(self.tree_node)
                self.node_number_label.place_forget()
                self.reset_and_store()
        except:
            print("Error on line 303")

    #Connecty current node to parent with an arrow
    def build_arrow(self):
        if self.notation_index == 0:
           self.connect_arrow = -1
        else:
            for node in self.node_value_holder:
                if int((self.notation_index-1) / 2) == node[3]:
                    #Searchs for parent_node's index in holder list
                    node_current = self.tree_canvas.coords(self.tree_node)
                    node_parent = self.tree_canvas.coords(node[0])
                    if self.go_right == 1:
                        if self.vertical_counter == 3:
                            #For last row if going right shortens distance a bit
                            current_x = (node_current[0] + node_current[2]) / 2 - 2
                            current_y = (node_current[1] + node_current[3]) / 2 - 25
                            parent_x = (node_parent[0] + node_parent[2]) / 2 + 12
                            parent_y = (node_parent[1] + node_parent[3]) / 2 + 24
                            arrow_coord = (current_x,current_y,parent_x,parent_y)
                        else:
                            arrow_coord = self.right_side_arrow_coordinate_maker(node_current, node_parent)
                    else:
                        if self.vertical_counter == 3:  
                            #For last row if going left
                             current_x = (node_current[0] + node_current[2]) / 2
                             current_y = (node_current[1] + node_current[3]) / 2 -25
                             parent_x = (node_parent[0] + node_parent[2]) / 2 - 18
                             parent_y = (node_parent[1] + node_parent[3]) / 2 + 19
                             arrow_coord = (current_x, current_y, parent_x, parent_y)
                        else:
                            arrow_coord = self.left_side_arrow_coordinate_maker(node_current, node_parent)
                    self.connect_arrow = self.tree_canvas.create_line(arrow_coord, width=3, fill="black")
                    break

        self.store_data()

    #Stores node data into 'self.node_value_holder'
    def store_data(self):
        node_data = self.store_single_node_data(self.tree_node, self.node_number_label, self.input_entry.get(), self.notation_index, self.connect_arrow)
        if self.notation_index > 0:
            parent_node_index = int((self.notation_index-1) / 2)
            for temp_node in self.node_value_holder:
                if temp_node[3] == parent_node_index:
                    if self.notation_index % 2 == 0:
                        temp_node[6] = node_data    #Link up right side
                    else:
                        temp_node[5] = node_data    #Links up left side

        self.reset_and_store()

    #Reset and store node data
    def reset_and_store(self):
        self.label_x_position = 519
        self.label_y_position = 99 + 50
        #print(self.node_value_holder)

    #Position calcs for when it goes left
    def right_side_arrow_coordinate_maker(self, current_node, parent_node):
        current_x = (current_node[0] + current_node[2]) / 2 - 18
        current_y = (current_node[1] + current_node[3]) / 2 - 18
        parent_x = (parent_node[0] + parent_node[2]) / 2 + 25
        parent_y = (parent_node[1] + parent_node[3]) / 2
        arrow_coord = (current_x,current_y,parent_x,parent_y)

        return arrow_coord

    #Position calcs for when it goes right
    def left_side_arrow_coordinate_maker(self, current_node, parent_node):
        current_x = (current_node[0] + current_node[2]) / 2 + 18
        current_y = (current_node[1] + current_node[3]) / 2 - 18
        parent_x = (parent_node[0] + parent_node[2]) / 2 - 25
        parent_y = (parent_node[1] + parent_node[3]) / 2
        arrow_coord = (current_x,current_y,parent_x,parent_y)

        return arrow_coord

    #First node placement (root)
    def push_first_node(self):
        x_move_counter = 0
        while x_move_counter < 70 - 5:
            self.node_number_label.place_forget()
            self.label_x_position += 2
            self.node_number_label.place(x=self.label_x_position, y=self.label_y_position)
            self.tree_canvas.move(self.tree_node, 2, 0)
            x_move_counter += 2
            self.window.update()

    #For each row it moves right
    def right_movement_in_row(self):
        try:
            x_move_counter = 0
            while x_move_counter < self.position_controller:
                self.node_number_label.place_forget()
                self.label_x_position += 2
                self.node_number_label.place(x=self.label_x_position, y=self.label_y_position)
                self.tree_canvas.move(self.tree_node, 2, 0)
                x_move_counter += 2
                self.window.update()
        except:
            print("Erro", "Interrupção")

    #For each row it moves left
    def left_movement_in_row(self):
        try:
            x_move_counter = 0
            while x_move_counter < self.position_controller:
                self.node_number_label.place_forget()
                self.label_x_position -= 2
                self.node_number_label.place(x=self.label_x_position, y=self.label_y_position)
                self.tree_canvas.move(self.tree_node, -2, 0)
                x_move_counter += 2
                self.window.update()
        except:
            print("Erro", "Interrupção")

    #Small square with comparisor operator
    def decision_making_about_left_side_direction(self):
        try:
            self.go_left = 1
            self.go_right = 0
            greater_than_symbol_label = tk.Label(self.window, text=">", fg=self.color_blue, bg="white", font=("Arial", 20, "bold"))
            greater_than_symbol_label.place(x=self.label_x_position - 40, y=self.label_y_position - 10)
            self.window.update()

            sleep(1)

            greater_than_symbol_label.place_forget()
        except:
            print("Erro", "Interrupção")

    #Small square with comparisor operator
    def decision_making_about_right_side_direction(self):
        try:
            self.go_right = 1
            self.go_left = 0
            less_than_symbol_label = tk.Label(self.window, text="<", fg=self.color_blue, bg="white", font=("Arial", 20, "bold"))
            less_than_symbol_label.place(x=self.label_x_position - 40, y=self.label_y_position - 10)
            self.window.update()

            sleep(1)

            less_than_symbol_label.place_forget()
        except:
            print("Erro", "Interrupção")

    def vertical_down_movement(self):
        try:
            y_move_counter = 0
            while y_move_counter < 106:
                self.node_number_label.place_forget()
                self.label_y_position += 4
                self.node_number_label.place(x=self.label_x_position, y=self.label_y_position)
                self.tree_canvas.move(self.tree_node, 0, 4)
                y_move_counter += 4
                sleep(0.01)
                self.window.update()
        except:
            print("Erro", "Interrupção")

    #Final right distance movement
    def right_moving_final_direction_giving(self):
        try:
            for node in self.node_value_holder:
                if int((self.notation_index + 1) * 2) == int(node[3]):
                    self.node_index = self.node_value_holder.index(node)
                    self.position_controller = 70 + 80 + self.gap_controller - 5
                    break
            else:
                if self.vertical_counter == 3:
                    self.position_controller = -1
                else:
                    self.position_controller = 70 + self.gap_controller - 5
            self.notation_index = (self.notation_index + 1) * 2
        except:
            print("Erro", "Interrupção")

    #Final left distance movement
    def left_moving_final_direction_giving(self):
        try:
            for node in self.node_value_holder:
                if int((self.notation_index + 1) * 2) - 1 == int(node[3]):
                    self.node_index = self.node_value_holder.index(node)
                    self.position_controller = 80 + 70 + self.gap_controller - 5
                    break
            else:
                self.position_controller = 80 + 70 + 80 + self.gap_controller - 5
            self.notation_index = ((self.notation_index + 1) * 2) - 1
        except:
            print("Erro", "Interrupção")

    #Handles Traversing
    def traversing_decision_making(self, option):
        self.disable_input_buttons()

        if len(self.node_value_holder) == 0:
            messagebox.showwarning("Erro", "Árvore Vazia, sem valores para caminhamento")
        else:
            if self.display_counter_box > -1: #For every box empty to fresh input
                for each_box_index in range(self.display_counter_box + 1):
                    self.value_printer[each_box_index].config(text=" ")
                self.display_counter_box = -1
            if option == 1: #Pre-order
                self.pre_order_traversing(self.node_value_holder[0])
            elif option == 2:   #In-order
                self.in_order_traversing(self.node_value_holder[0])
            elif option == 3:   #Post-order
                self.post_order_traversing(self.node_value_holder[0])
            elif option == 4:   #Clear tree colors (just a preorder with common colors and less wait time)
                self.pre_order_clearing(self.node_value_holder[0])

        self.enable_input_buttons()

    #Recursively prints until control node reachs nullptr (is a leaf)
    def pre_order_traversing(self, control_node):
        if control_node is None:
            return
        else:
            self.tree_canvas.itemconfig(control_node[0], fill="red", outline="black")
            self.display_counter_box += 1
            self.value_printer[self.display_counter_box].config(text=control_node[2])
            control_node[1].config(bg="red",fg="white")
            self.window.update()
            sleep(0.8)
            self.window.update()

            self.pre_order_traversing(control_node[5])
            self.pre_order_traversing(control_node[6])

    def in_order_traversing(self, control_node):
        if control_node is None:
            return
        else:
            self.in_order_traversing(control_node[5])

            self.tree_canvas.itemconfig(control_node[0], fill="green", outline="black")
            self.display_counter_box += 1
            self.value_printer[self.display_counter_box].config(text=control_node[2])
            control_node[1].config(bg="green", fg="white")
            self.window.update()
            sleep(0.8)
            self.window.update()

            self.in_order_traversing(control_node[6])

    def post_order_traversing(self, control_node):
        if control_node is None:
            return
        else:
            self.post_order_traversing(control_node[5])
            self.post_order_traversing(control_node[6])

            self.tree_canvas.itemconfig(control_node[0], fill="blue4", outline="black")
            self.display_counter_box += 1
            self.value_printer[self.display_counter_box].config(text=control_node[2])
            control_node[1].config(bg="blue4", fg="white")
            self.window.update()
            sleep(0.8)
            self.window.update()

    #Recursively changes color of tree back to normal
    def pre_order_clearing(self, control_node):
        if control_node is None:
            return
        else:
            self.tree_canvas.itemconfig(control_node[0], fill="blue", outline="black")
            self.display_counter_box += 1
            self.value_printer[self.display_counter_box].config(text=control_node[2])
            control_node[1].config(bg="blue",fg="white")
            self.window.update()

            self.pre_order_clearing(control_node[5])
            self.pre_order_clearing(control_node[6])

    #Node removal
    def remove_node(self):
        searched_node = self.input_entry.get()
        p_node = None

        if len(self.node_value_holder) == 0:
            messagebox.showwarning("Erro", "ABP vazia!")
        else:
            node = self.node_value_holder[0]    #starting from first node

            #Search for node
            while True:
                if node is None:
                    messagebox.showwarning("Não Encontrado","Nó não está presente na árvore")
                    break
                if int(node[2]) == int(searched_node):  #Finds node by comparing nums (strs)
                    break
                if int(searched_node) > int(node[2]):   #Checks if it's supposed to go to right
                    p_node = node
                    node = node[6]
                else:   #Else it's supposed to go to left
                    p_node = node
                    node =  node[5]

            if node is not None:
                if node[5] is None and node[6] is None:
                    #No child node exists
                    self.no_child_node_exist(node, p_node)

                elif node[5] is None and node[6] is not None:
                    #No left child node, but right child node exists
                    self.left_none_right_exist(node)

                elif node[5] is not None and node[6] is None:
                    #No right child node, but left child node exists
                    self.right_none_left_exist(node)

                elif node[5] is not None and node[6] is not None:
                       #Both child nodes exist, right first
                    self.left_none_right_exist(node)

                if len(self.node_value_holder) == 0:
                    #When all nodes are deleted, add_null_word label again
                    self.notation_index = 0
                    self.null_word_label.place(x=565, y=90 + 50)

    def search_node(self):
        searched_node = self.input_entry.get()

        if len(self.node_value_holder) == 0:
            messagebox.showwarning("Erro", "ABP vazia!")
        else:
            node = self.node_value_holder[0]    #Starting from first node

            #Search for node
            while True:
                #Changes colors throughough search (back and forth)
                self.tree_canvas.itemconfig(node[0], fill="cyan2", outline="black")
                node[1].config(bg="cyan2", fg="black")
                self.window.update()
                sleep(1)

                self.tree_canvas.itemconfig(node[0], fill="blue", outline="black")
                node[1].config(bg="blue", fg="white")
                self.window.update()
                sleep(1)

                if node is None:
                    messagebox.showwarning("Não Encontrado","Nó não está presente na árvore")
                    break
                if int(node[2]) == int(searched_node):  #Finds node by comparing nums (strs)
                    break
                if int(searched_node) > int(node[2]):   #Checks if it's supposed to go to right
                    node = node[6]
                else:   #Else it's supposed to go to left
                    node =  node[5]

            #Changes colors an extra time when searched node is found
            self.tree_canvas.itemconfig(node[0], fill="white", outline="red")
            node[1].config(bg="white", fg="black")
            self.window.update()
            sleep(1)

            self.tree_canvas.itemconfig(node[0], fill="blue", outline="black")
            node[1].config(bg="blue", fg="white")
            self.window.update()
            sleep(1)

    def no_child_node_exist(self, node, p_node):
        if(self.chosen_input_option == 2):
            if p_node is None:
                pass
            else:
                if p_node[5] is node:
                    p_node[5] = None

                else:
                    p_node[6] = None

        self.tree_canvas.itemconfig(node[0], fill="white", outline="red")
        node[1].config(bg="white", fg="black")
        self.window.update()
        sleep(1)

        #Actual removal
        if(self.chosen_input_option == 2):
            self.node_visual_erase_and_pop(node)
        #print(self.node_value_holder)

    def left_none_right_exist(self, node):
        p_temp = None
        temp = node[6]
        left_side_existence_checking_of_one_side_down_label_node = 0
        while temp[5]:
            left_side_existence_checking_of_one_side_down_label_node = 1
            p_temp=temp
            temp=temp[5]

        if(self.chosen_input_option == 2):
            self.color_indicator_to_delete(node=node, temp=temp)

        if left_side_existence_checking_of_one_side_down_label_node == 1:
            node[2] = temp[2]
            node[1].config(text=temp[2])
            if temp[6]:
                temp[2] = temp[6][2]
                temp[1].config(text=temp[6][2])
                p_temp=temp
                temp=temp[6]
                p_temp[6]=None
            else:
                p_temp[5] = None
        else:
            temp1 = None
            p_temp=node
            while True:
                p_temp[2]=temp[2]
                p_temp[1].config(text=temp[2])
                if temp[6]:
                    p_temp=temp
                    temp=temp[6]
                    if temp[5]:
                        temp1 = temp[5]
                        temp[5] = None
                else:
                    break

            p_temp[6] = None

            if temp1:
                take_temp1_val = temp1[2]
                self.tree_canvas.delete(temp1[0])
                self.tree_canvas.delete(temp1[4])
                temp1[1].place_forget()
                self.node_value_holder.pop(self.node_value_holder.index(temp1))

                p_node_coord = self.tree_canvas.coords(node[6][0])
                c_right_node_coord = self.tree_canvas.coords(node[6][6][0])

                node_coord = self.make_node_to_the_left_manually(p_node_coord, c_right_node_coord)
                make_circle = self.tree_canvas.create_oval(node_coord, width=3, fill="blue4", outline="black")

                arrow_coord = self.make_left_arrow_for_node_left_manually(node_coord, p_node_coord)
                take_arrow = self.tree_canvas.create_line(arrow_coord, width=3, fill="black")

                label_make = tk.Label(self.window, text=take_temp1_val, fg="white", bg="blue4", font=("Arial", 12, "bold"))
                label_make.place(x=node_coord[0] + 14, y=node_coord[1] + 14)

                notation_index = ((node[6][3] + 1) * 2) - 1

                temp_take = self.store_single_node_data(make_circle, label_make, take_temp1_val, notation_index, take_arrow)

                node[6][5] = temp_take

        #Actual removal only if the remove option was chosen on input
        if(self.chosen_input_option == 2):
            self.node_visual_erase_and_pop(temp)
            
        #print(self.node_value_holder)

    def right_none_left_exist(self, node):
        p_temp = None
        temp = node[5]
        right_side_existence_checking_of_one_side_down_label_node = 0
        while temp[6]:
            right_side_existence_checking_of_one_side_down_label_node = 1
            p_temp = temp
            temp = temp[6]
        if(self.chosen_input_option == 2):
            self.color_indicator_to_delete(node=node, temp=temp)

        if right_side_existence_checking_of_one_side_down_label_node == 1:
            node[2] = temp[2]
            node[1].config(text=temp[2])
            if temp[5]:
                temp[2] = temp[5][2]
                temp[1].config(text=temp[5][2])
                p_temp=temp
                temp=temp[5]
                p_temp[5]=None
            else:
                p_temp[6] = None

        else:
            temp1 = None
            p_temp = node
            while True:
                p_temp[2] = temp[2]
                p_temp[1].config(text=temp[2])
                if temp[5]:
                    p_temp = temp
                    temp = temp[5]
                    if temp[6]:
                        temp1 = temp[6]
                        temp[6] = None
                else:
                    break

            p_temp[5] = None

            if temp1:
                take_temp1_val = temp1[2]
                self.tree_canvas.delete(temp1[0])
                self.tree_canvas.delete(temp1[4])
                temp1[1].place_forget()
                self.node_value_holder.pop(self.node_value_holder.index(temp1))

                p_node_coord = self.tree_canvas.coords(node[5][0])
                c_right_node_coord = self.tree_canvas.coords(node[5][5][0])

                node_coord = self.make_node_to_the_right_manually(p_node_coord, c_right_node_coord)

                make_circle = self.tree_canvas.create_oval(node_coord, width=3, fill="blue4", outline="black")

                arrow_coord = self.make_right_arrow_for_node_right_manually(node_coord, p_node_coord)
                take_arrow = self.tree_canvas.create_line(arrow_coord, width=3, fill="black")

                label_make = tk.Label(self.window, text=take_temp1_val, fg="white", bg="blue4", font=("Arial", 12, "bold"))
                label_make.place(x=node_coord[0] + 14, y=node_coord[1] + 14)

                notation_index = ((node[5][3] + 1) * 2)

                temp_take = self.store_single_node_data(make_circle, label_make, take_temp1_val, notation_index, take_arrow)
                node[5][6]=temp_take

        #Actual removal
        if(self.chosen_input_option == 2):
            self.node_visual_erase_and_pop(temp)
        #print(self.node_value_holder)

    #Colors when removing
    def color_indicator_to_delete(self, node, temp):
        #node is the Target-for-removal node
        #temp is the Replacer node
        self.tree_canvas.itemconfig(temp[0], fill="white", outline="red")
        temp[1].config(bg="white", fg="black")
        self.tree_canvas.itemconfig(node[0], fill="red")
        node[1].config(bg="red", fg="white")

        self.window.update()
        sleep(5)

        #Post-removal colors
        self.tree_canvas.itemconfig(temp[0], fill="blue", outline="black")
        temp[1].config(fg="white", bg="blue")
        self.tree_canvas.itemconfig(node[0], fill="blue", outline="black")
        node[1].config(fg="white", bg="blue")

    #Utility funcs for removal
    #Make node to the left when removing
    def make_node_to_the_left_manually(self, p_node_coord, c_right_node_coord):
        make_initial_x = p_node_coord[0] - (c_right_node_coord[0] - p_node_coord[0])
        make_initial_y = c_right_node_coord[1]
        make_final_x = p_node_coord[2] - (c_right_node_coord[2] - p_node_coord[2])
        make_final_y = c_right_node_coord[3]
        node_coord = (make_initial_x, make_initial_y, make_final_x, make_final_y)

        return node_coord

    #Make arrow for newly created left node
    def make_left_arrow_for_node_left_manually(self, node_coord, p_node_coord):
        current_x = (node_coord[0] + node_coord[2]) / 2 + 18
        current_y = (node_coord[1] + node_coord[3]) / 2 - 18
        parent_x = (p_node_coord[0] + p_node_coord[2]) / 2 - 25
        parent_y = (p_node_coord[1] + p_node_coord[3]) / 2
        arrow_coord = (current_x, current_y, parent_x, parent_y)

        return arrow_coord

    #Make node to the right when removing
    def make_node_to_the_right_manually(self, p_node_coord, c_right_node_coord):
        make_initial_x = p_node_coord[0] + (p_node_coord[0] - c_right_node_coord[0])
        make_initial_y = c_right_node_coord[1]
        make_final_x = p_node_coord[2] + (p_node_coord[2] - c_right_node_coord[2])
        make_final_y = c_right_node_coord[3]
        node_coord = (make_initial_x, make_initial_y, make_final_x, make_final_y)

        return node_coord

    #Make arrow for newly created right node
    def make_right_arrow_for_node_right_manually(self, node_coord, p_node_coord):
        current_x = (node_coord[0] + node_coord[2]) / 2 - 18
        current_y = (node_coord[1] + node_coord[3]) / 2 - 18
        parent_x = (p_node_coord[0] + p_node_coord[2]) / 2 + 25
        parent_y = (p_node_coord[1] + p_node_coord[3]) / 2
        arrow_coord = (current_x, current_y, parent_x, parent_y)

        return arrow_coord

    #Store data in list that holds tree data and parent-children relationships
    def store_single_node_data(self, make_circle, label_make, take_temp1_val, notation_index, take_arrow):
        temp_take = []
        temp_take.append(make_circle)
        temp_take.append(label_make)
        temp_take.append(take_temp1_val)
        temp_take.append(notation_index)
        temp_take.append(take_arrow)
        temp_take.append(None)
        temp_take.append(None)
        self.node_value_holder.append(temp_take)

        return temp_take

    #Disabling and enabling buttons when in down time
    def disable_input_buttons(self):
        self.insert_node_button["state"] = "disabled"
        self.pre_order_traversal_button["state"] = "disabled"
        self.in_order_traversal_button["state"] = "disabled"
        self.post_order_traversal_button["state"] = "disabled"
        self.remove_button["state"] = "disabled"
        self.search_element_button["state"] = "disabled"
        self.clear_tree_button["state"] = "disabled"

    def enable_input_buttons(self):
        self.insert_node_button["state"] = "normal"
        self.pre_order_traversal_button["state"] = "normal"
        self.in_order_traversal_button["state"] = "normal"
        self.post_order_traversal_button["state"] = "normal"
        self.remove_button["state"] = "normal"
        self.search_element_button["state"] = "normal"
        self.clear_tree_button["state"] = "normal"

    #Erasing circle and deleting from tree holder list
    def node_visual_erase_and_pop(self, temp_node):
        self.tree_canvas.delete(temp_node[0])
        self.tree_canvas.delete(temp_node[4])
        temp_node[1].place_forget()
        self.node_value_holder.pop(self.node_value_holder.index(temp_node))

#Setting it up and booting
root = tk.Tk()
root.title("Árvore Binária de Pesquisa")
root.geometry("1250x780")
root.config(bg="#bdc3c7")

ABP_GUI(root)
root.mainloop()