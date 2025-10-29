from tkinter import *
from tkinter import ttk
from MyTasks.Task4.Controllers.My_Tasks_4Controller import My_Tasks_4Controller


class MyTasks_4_View(Tk):
    def __init__(self):
        super().__init__()
        self.title("Учет фильмов")
        self.geometry('1000x400')

        # Раздел Добавить
        self.frame_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_add.pack(anchor='center', fill=X, padx=10, pady=10)

        self.add_title = ttk.Label(self.frame_add, text="Добавить фильм")
        self.add_title.pack()

        # Название
        self.title_label = ttk.Label(self.frame_add, text="Название")
        self.title_label.pack()
        self.input_title = ttk.Entry(self.frame_add)
        self.input_title.pack()

        # Год
        self.year_label = ttk.Label(self.frame_add, text="Год")
        self.year_label.pack()
        self.input_year = ttk.Entry(self.frame_add)
        self.input_year.pack()

        # Рейтинг
        self.rating_label = ttk.Label(self.frame_add, text="Рейтинг")
        self.rating_label.pack()
        self.input_rating = ttk.Entry(self.frame_add)
        self.input_rating.pack()

        self.add_button = ttk.Button(self.frame_add, text="Добавить", command=self.add_movie)
        self.add_button.pack(pady=5)

        # Кнопки управления
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(padx=10, pady=10)

        self.set_rating_button = ttk.Button(
            self.button_frame,
            text="Поставить оценку",
            command=self.set_rating
        )
        self.set_rating_button.pack(side=LEFT, padx=5)

        self.find_button = ttk.Button(
            self.button_frame,
            text="Найти по названию",
            command=self.find_movie
        )
        self.find_button.pack(side=LEFT, padx=5)

        self.show_unwatched_button = ttk.Button(
            self.button_frame,
            text="Показать непросмотренные",
            command=self.show_unwatched
        )
        self.show_unwatched_button.pack(side=LEFT, padx=5)

        self.delete_button = ttk.Button(
            self.button_frame,
            text="Удалить",
            command=self.delete_movie
        )
        self.delete_button.pack(side=LEFT, padx=5)

        # Таблица
        self.frame_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_table.pack(anchor='center', fill=BOTH, expand=True, padx=10, pady=10)

        columns = ('id', 'title', 'year', 'rating', 'watched')
        self.tree = ttk.Treeview(self.frame_table, columns=columns, show="headings")
        self.tree.pack(fill=BOTH, expand=True)

        self.tree.heading('id', text="ID")
        self.tree.heading('title', text="Название")
        self.tree.heading('year', text="Год")
        self.tree.heading('rating', text="Рейтинг")
        self.tree.heading('watched', text="Статус")

        self.update_table()

    def update_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        movies = My_Tasks_4Controller.get()
        for dict in movies:
            status = "Просмотрен" if dict["watched"] else "Не просмотрен"
            self.tree.insert("", END, values=(
                dict["id"],
                dict["title"],
                dict["year"],
                dict["rating"],
                status
            ))

    def add_movie(self):
        title = self.input_title.get().strip()
        year = self.input_year.get().strip()
        rating = self.input_rating.get().strip()

        if not all([title, year, rating]):
            return

        try:
            year = int(year)
            rating = float(rating)
        except ValueError:
            return

        My_Tasks_4Controller.add(title, year, rating)
        self.clear_input_fields()
        self.update_table()

    def set_rating(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        movie_id = int(self.tree.item(selected_item, "values")[0])
        new_rating = self.input_rating.get().strip()

        if not new_rating:
            return

        try:
            new_rating = float(new_rating)
        except ValueError:
            return

        My_Tasks_4Controller.set_rating(movie_id, new_rating)
        self.update_table()

    def find_movie(self):
        title = self.input_title.get().strip()
        if not title:
            return

        result = My_Tasks_4Controller.find_by_title(title)
        self.show_found_movies(result)
        self.update_table()

    def show_unwatched(self):
        result = My_Tasks_4Controller.show_unwatched()
        self.show_found_movies(result)
        self.update_table()

    def delete_movie(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        movie_id = int(self.tree.item(selected_item, "values")[0])
        My_Tasks_4Controller.delete(movie_id)
        self.update_table()

    def clear_input_fields(self):
        self.input_title.delete(0, END)
        self.input_year.delete(0, END)
        self.input_rating.delete(0, END)

    def show_found_movies(self, movies):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for dict in movies:
            status = "Просмотрен" if dict["watched"] else "Не просмотрен"
            self.tree.insert("", END, values=(
                dict["id"],
                dict["title"],
                dict["year"],
                dict["rating"],
                status
            ))