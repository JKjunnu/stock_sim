import tkinter as tk
from tkinter import ttk
import src.client.Views.Home as Home
import src.backend.server_endpoints.account_info as ai
import src.backend.server_endpoints.stock_info as si


class Stock_buypg(tk.Frame):
    def _init_(self, parent, controller):
        self.controller = controller
        # super()._init_(self, parent)
        tk.Frame._init_(self, parent)
        self.bind("<<ShowFrame>>", self.display_stock_info)
        self.create_widgets()

    def create_widgets(self):
        try:
            acc_info = ai.get_account_info()
            acc_bal = acc_info['balance']
            ticker_name_label = ttk.Label(self, text="text", wraplength=600, font=(
                "TkDefaultFont", 20))
            ticker_name_label.grid(row=0, columnspan=2, padx=300,
                                   pady=10, sticky=tk.E+tk.W)
            acc_bal_label = ttk.Label(
                self, text="Balance : "+str(acc_bal), font=(15))
            acc_bal_label.grid(row=1, column=0, padx=20, sticky=tk.W)
            unit_price_label = ttk.Label(self, text="Unit Price", font=(15))
            unit_price_label.grid(row=2, column=0, padx=20, pady=10)
            stock_price_label = ttk.Label(self, text='Price', font=(15))
            stock_price_label.grid(row=2, column=1, pady=10)
            self.stock_price_label = stock_price_label
            qty_label = ttk.Label(self, text='Qty', font=(15))
            qty_label.grid(row=3, column=0, pady=10)
            qty_entry = ttk.Entry(self, font=(15))
            qty_entry.grid(row=4, column=0, pady=10, sticky=tk.W)

        except Exception as e:
            print(e)

    def display_stock_info(self, event):
        try:
            selected_ticker = self.controller.app_data['selected_ticker'].get()
            live_price = si.get_live_price(selected_ticker)
            self.ticker_name_label['text'] = selected_ticker
            self.stock_price_label['text'] = str(live_price)
        except Exception as e:
            print(e)