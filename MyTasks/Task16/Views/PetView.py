from tkinter import *
from tkinter import ttk

class PetView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Учёт домашних животных")
        self.geometry('500x500')

        # Раздел Добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, )
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)
        self.add_title = ttk.Label(self.fram_add, text="Добавить питомца")
        self.add_title.pack()