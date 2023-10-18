import tkinter as tk
from tkinter import messagebox

'''
TODO:
#Tree GUI
def show_tree():
    pass

def insert_element():
    pass

def remove_element():
    pass

def preorder_traversal():
    pass

def inorder_traversal():
    pass

def postorder_traversal():
    pass

def find_element():
    pass
'''

class ABP_GUI:
    # Constructor
    def __init__(self, root):
        self.window = root

        # Canvas for tree visuals
        self.visual_canvas = tk.Canvas(self.window, width=1290, height=520, bg="white", relief="groove", bd=4, scrollregion=(0, 0, 1260, 500))
        self.visual_canvas.place(x=23, y=25)
        self.visual_canvas.grid(row=0, column=0, sticky="nsew")

        # Design choice (botton line)
        self.below_canvas = tk.Canvas(self.window, width=1800, height=25, bg="light gray", relief="groove")
        self.below_canvas.place(x=0, y=765)

        # Setting up y scrollbar for visualizer canvas
        self.vertical_scrollbar = tk.Scrollbar(self.window, command=self.visual_canvas.yview)
        self.visual_canvas.config(yscrollcommand=self.vertical_scrollbar.set)
        self.vertical_scrollbar.grid(row=0, column=1, sticky="ns")
        self.visual_canvas.bind("<Configure>", self.on_config_scrollbars)

        # Setting up x scrollbar for visualizer canvas
        self.horizontal_scrollbar = tk.Scrollbar(self.window, command=self.visual_canvas.xview, orient=tk.HORIZONTAL)
        self.visual_canvas.config(xscrollcommand=self.horizontal_scrollbar.set)
        self.horizontal_scrollbar.grid(row=1, column=0, sticky="ew")
        self.visual_canvas.bind("<Configure>", self.on_config_scrollbars)

        # Setting up init vars

        self.do_testing_stuff()


    '''Utility Funcs'''
    # Updates scrollbars based on canvas
    def on_config_scrollbars(self, event):
        self.visual_canvas.configure(scrollregion=self.visual_canvas.bbox("all"))

    # Generic Testing func
    def do_testing_stuff(self):
        for i in range(1, 3000):
            self.visual_canvas.create_text(i * 20, 50, text=f"Item {i}", font=("Helvetica", 12))
            self.visual_canvas.create_text(150, i * 20, text=f"Item {i}", font=("Helvetica", 12))


# Setting it up and booting
root = tk.Tk()
root.title("Árvore Binária de Pesquisa")
root.geometry("1350x780")
root.config(bg="#bdc3c7")

ABP_GUI(root)
root.mainloop()