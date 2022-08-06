import tkinter as tk
from tkinter import ttk

class Transactions(tk.Frame):
    def __init__(self , parent , controller):
        self.controller = controller
        tk.Frame.__init__(self , parent)
        print("Hi")