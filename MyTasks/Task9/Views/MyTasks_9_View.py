from tkinter import *
from tkinter import ttk
from MyTasks.Task9.Controllers.My_Tasks_9Controller import My_Tasks_9Controller


class MyTasks_9_View(Tk):
    def __init__(self):
        super().__init__()
        self.title("Коллекция игр")
        self.geometry('1000x450')

        # Раздел Добавить
        self.frame_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_add.pack(anchor='center', fill=X, padx=10, pady=10)

        self.add_title = ttk.Label(self.frame_add, text="Добавить игру")
        self.add_title.pack()

        # Название
        self.title_label = ttk.Label(self.frame_add, text="Название")
        self.title_label.pack()
        self.input_title = ttk.Entry(self.frame_add)
        self.input_title.pack()

        # Жанр
        self.genre_label = ttk.Label(self.frame_add, text="Жанр")
        self.genre_label.pack()
        self.input_genre = ttk.Entry(self.frame_add)
        self.input_genre.pack()

        # Платформа
        self.platform_label = ttk.Label(self.frame_add, text="Платформа")
        self.platform_label.pack()
        self.input_platform = ttk.Entry(self.frame_add)
        self.input_platform.pack()

        # Пройдена
        self.completed_label = ttk.Label(self.frame_add, text="Пройдена?")
        self.completed_label.pack()
        self.input_completed = ttk.Entry(self.frame_add)
        self.input_completed.pack()

        self.add_button = ttk.Button(self.frame_add, text="Добавить", command=self.add_game)
        self.add_button.pack(pady=5)

        # Кнопки управления
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(padx=10, pady=10)

        self.mark_button = ttk.Button(
            self.button_frame,
            text="Отметить как пройденную",
            command=self.mark_completed
        )
        self.mark_button.pack(side=LEFT, padx=5)

        self.find_button = ttk.Button(
            self.button_frame,
            text="Найти по жанру",
            command=self.find_by_genre
        )
        self.find_button.pack(side=LEFT, padx=5)

        self.filter_button = ttk.Button(
            self.button_frame,
            text="Игры для платформы",
            command=self.filter_by_platform
        )
        self.filter_button.pack(side=LEFT, padx=5)

        # Таблица
        self.frame_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_table.pack(anchor='center', fill=BOTH, expand=True, padx=10, pady=10)

        columns = ('id', 'title', 'genre', 'platform', 'completed')
        self.tree = ttk.Treeview(self.frame_table, columns=columns, show="headings")
        self.tree.pack(fill=BOTH, expand=True)

        self.tree.heading('id', text="ID")
        self.tree.heading('title', text="Название")
        self.tree.heading('genre', text="Жанр")
        self.tree.heading('platform', text="Платформа")
        self.tree.heading('completed', text="Пройдена")

        self.update_table()

    def update_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        games = My_Tasks_9Controller.get()
        for dict in games:
            completed_status = "Да" if dict["completed"] else "Нет"
            self.tree.insert("", END, values=(
                dict["id"],
                dict["title"],
                dict["genre"],
                dict["platform"],
                completed_status
            ))

    def add_game(self):
        title = self.input_title.get().strip()
        genre = self.input_genre.get().strip()
        platform = self.input_platform.get().strip()
        completed = self.input_completed.get().strip()

        My_Tasks_9Controller.add(title, genre, platform, completed)
        self.clear_input_fields()
        self.update_table()

    def mark_completed(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        game_id = int(self.tree.item(selected_item, "values")[0])
        My_Tasks_9Controller.mark_completed(game_id)
        self.update_table()

    def find_by_genre(self):
        genre = self.input_genre.get().strip()
        if not genre:
            return

        result = My_Tasks_9Controller.find_by_genre(genre)
        self.show_found_games(result)

    def filter_by_platform(self):
        platform = self.input_platform.get().strip()
        if not platform:
            return

        result = My_Tasks_9Controller.filter_by_platform(platform)
        self.show_found_games(result)

    def clear_input_fields(self):
        self.input_title.delete(0, END)
        self.input_genre.delete(0, END)
        self.input_platform.delete(0, END)
        self.input_completed.delete(0, END)

    def show_found_games(self, games):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for dict in games:
            completed_status = "Да" if dict["completed"] else "Нет"
            self.tree.insert("", END, values=(
                dict["id"],
                dict["title"],
                dict["genre"],
                dict["platform"],
                completed_status
            ))