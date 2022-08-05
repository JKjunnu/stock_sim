import tkinter as tk
from tkinter import ttk

class Sell_stock(tk.Frame):
    def __init__(self , parent , controller):
        self.controller = controller
        tk.Frame.__init__(self , parent)
        self.bind('<<ShowFrame>>' , self.display_stock_data)
    def display_stock_data(self , event):
        print(self.controller.app_data['Selected_ticker_sell'].get())