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
    def __init__(self, root_gui):
        self.window = root_gui

        # Setting up 2 canvas'
        # One for tree visuals
        self.visualizer_canvas = tk.Canvas(self.window, width=1290, height=520, bg="white", relief="groove", bd=4)
        self.visualizer_canvas.place(x=23, y=25)

        # One for traversal_list (maybe not)
        self.traversal_list_canvas = tk.Canvas(self.window, width=2000, height=108, bg="light gray", relief="groove")
        self.traversal_list_canvas.place(x=0, y=735)

        #Setting up scrollbar for visualizer canvas (x and y)
        

# Setting it up and booting
window = tk.Tk()
window.title("Árvore Binária de Pesquisa")
window.geometry("1350x780")
window.config(bg="#bdc3c7")

ABP_GUI(window)
window.mainloop()