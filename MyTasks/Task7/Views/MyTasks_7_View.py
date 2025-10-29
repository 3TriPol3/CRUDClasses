from tkinter import *
from tkinter import ttk
from MyTasks.Task7.Controllers.My_Tasks_7Controller import My_Tasks_7Controller


class MyTasks_7_View(Tk):
    def __init__(self):
        super().__init__()
        self.title("Библиотека книг")
        self.geometry('1000x450')

        # Раздел Добавить
        self.frame_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_add.pack(anchor='center', fill=X, padx=10, pady=10)

        self.add_title = ttk.Label(self.frame_add, text="Добавить книгу")
        self.add_title.pack()

        # Название
        self.title_label = ttk.Label(self.frame_add, text="Название")
        self.title_label.pack()
        self.input_title = ttk.Entry(self.frame_add)
        self.input_title.pack()

        # Автор
        self.author_label = ttk.Label(self.frame_add, text="Автор")
        self.author_label.pack()
        self.input_author = ttk.Entry(self.frame_add)
        self.input_author.pack()

        # Год
        self.year_label = ttk.Label(self.frame_add, text="Год")
        self.year_label.pack()
        self.input_year = ttk.Entry(self.frame_add)
        self.input_year.pack()

        # Прочитана
        self.read_label = ttk.Label(self.frame_add, text="Прочитана?")
        self.read_label.pack()
        self.input_read = ttk.Entry(self.frame_add)
        self.input_read.pack()

        self.add_button = ttk.Button(self.frame_add, text="Добавить", command=self.add_book)
        self.add_button.pack(pady=5)

        # Кнопки управления
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(padx=10, pady=10)

        self.mark_read_button = ttk.Button(
            self.button_frame,
            text="Отметить как прочитанную",
            command=self.mark_read
        )
        self.mark_read_button.pack(side=LEFT, padx=5)

        self.find_button = ttk.Button(
            self.button_frame,
            text="Найти по автору",
            command=self.find_by_author
        )
        self.find_button.pack(side=LEFT, padx=5)

        self.filter_button = ttk.Button(
            self.button_frame,
            text="Книги за год",
            command=self.filter_by_year
        )
        self.filter_button.pack(side=LEFT, padx=5)

        # Таблица
        self.frame_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_table.pack(anchor='center', fill=BOTH, expand=True, padx=10, pady=10)

        columns = ('id', 'title', 'author', 'year', 'read')
        self.tree = ttk.Treeview(self.frame_table, columns=columns, show="headings")
        self.tree.pack(fill=BOTH, expand=True)

        self.tree.heading('id', text="ID")
        self.tree.heading('title', text="Название")
        self.tree.heading('author', text="Автор")
        self.tree.heading('year', text="Год")
        self.tree.heading('read', text="Прочитана")

        self.update_table()

    def update_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        books = My_Tasks_7Controller.get()
        for dict in books:
            read_status = "Да" if dict["read"] else "Нет"
            self.tree.insert("", END, values=(
                dict["id"],
                dict["title"],
                dict["author"],
                dict["year"],
                read_status
            ))

    def add_book(self):
        title = self.input_title.get().strip()
        author = self.input_author.get().strip()
        year = self.input_year.get().strip()
        read = self.input_read.get().strip()

        My_Tasks_7Controller.add(title, author, year, read)
        self.clear_input_fields()
        self.update_table()

    def mark_read(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        book_id = int(self.tree.item(selected_item, "values")[0])
        My_Tasks_7Controller.mark_read(book_id)
        self.update_table()

    def find_by_author(self):
        author = self.input_author.get().strip()
        if not author:
            return

        result = My_Tasks_7Controller.find_by_author(author)
        self.show_found_books(result)

    def filter_by_year(self):
        year = self.input_year.get().strip()
        if not year:
            return

        try:
            year = int(year)
        except ValueError:
            return

        result = My_Tasks_7Controller.filter_by_year(year)
        self.show_found_books(result)

    def clear_input_fields(self):
        self.input_title.delete(0, END)
        self.input_author.delete(0, END)
        self.input_year.delete(0, END)
        self.input_read.delete(0, END)

    def show_found_books(self, books):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for dict in books:
            read_status = "Да" if dict["read"] else "Нет"
            self.tree.insert("", END, values=(
                dict["id"],
                dict["title"],
                dict["author"],
                dict["year"],
                read_status
            ))