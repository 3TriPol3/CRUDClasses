from tkinter import *
from tkinter import ttk

from MyTasks.Task16.Controllers.PetController import PetController


class PetView(Tk):
    '''
    Функции: добавить питомца, отметить прививку, питомцы владельца,
найти по типу
    '''

    def __init__(self):
        super().__init__()
        self.title("Учет домашних животных")
        self.geometry('1500x500')

        # раздел Добавить
        self.fram_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.fram_add.pack(anchor='center', fill=X, padx=10, pady=10)

        self.add_title = ttk.Label(self.fram_add, text="Добавить питомца")
        self.add_title.pack()

        # name
        self.name = ttk.Label(self.fram_add, text="Введите имя питомца")
        self.name.pack()

        # Окна ввода данных
        self.input_name = ttk.Entry(self.fram_add)
        self.input_name.pack()

        # type
        self.type = ttk.Label(self.fram_add, text="Введите тип питомца")
        self.type.pack()

        # Окна ввода данных
        self.input_type = ttk.Entry(self.fram_add)
        self.input_type.pack()

        # age
        self.age = ttk.Label(self.fram_add, text="Введите возраст питомца")
        self.age.pack()

        # Окна ввода данных
        self.input_age = ttk.Entry(self.fram_add)
        self.input_age.pack()

        # owner
        self.owner = ttk.Label(self.fram_add, text="Введите имя хозяина питомца")
        self.owner.pack()
        # Окна ввода данных
        self.input_owner = ttk.Entry(self.fram_add)
        self.input_owner.pack()
        # Кнопка
        self.add_button = ttk.Button(self.fram_add, text="Добавить", command=self.add_pet)
        self.add_button.pack()
        # вывод
        #Таблица
        self.frame_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_table.pack(anchor='center', fill=X, padx=10, pady=10)


        columns = ('id','name','type','age','owner','vaccinated')
        self.tree =ttk.Treeview(self.frame_table,columns=columns,show="headings")
        self.tree.pack(fill=BOTH,expand=1)
        self.table()

    def table(self):
        # Очистить таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)
        # список животных
        pets = PetController.get()
        list_pets = [] # сюда будут передаваться кортежи с описанием животных
        for pet in pets:
            list_pets.append(
                (
                    pet['id'],
                    pet['name'],
                    pet['type'],
                    pet['age'],
                    pet['owner'],
                    pet['vaccinated'],
                 )
            )
        # перевести на русский язык названия столбцов
        self.tree.heading('id', text="№")
        self.tree.heading('name', text="Имя")
        self.tree.heading('type', text="Тип")
        self.tree.heading('age', text="Возраст")
        self.tree.heading('owner', text="Имя хозяина")
        self.tree.heading('vaccinated', text="Вакцинация")
        for pet in list_pets:
            self.tree.insert("",END,values=pet)

    def add_pet(self):
        PetController.add(
            name=self.input_name.get(),
            type=self.input_type.get(),
            age=self.input_age.get(),
            owner=self.input_owner.get()
        )
        self.table()