import tkinter as tk
import src.client.Views.Home as Home
import src.client.Views.Search_Result as Search_Result
import src.client.Views.Stock_dispg as Stock_dispg
import src.client.Views.Stock_buypg as Stock_buypg


class Main_window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Stock Simulator")
        self.geometry("800x600")
        self.resizable(width=False, height=False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        container = tk.Frame(self)
        container.grid(column=0, row=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.app_data = {"Search_str": tk.StringVar() , "Selected_ticker" : tk.StringVar()}
        self.frames = {}
        self.columnconfigure(0, weight=1)
        for F in (Home.HomeView, Search_Result.SearchResult , Stock_dispg.Stock_dispg , Stock_buypg.Stock_buypg):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_page(Home.HomeView)

    def show_page(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")


def launch_client():
    app = Main_window()
    app.mainloop()