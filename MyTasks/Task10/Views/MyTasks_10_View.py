from tkinter import *
from tkinter import ttk
from MyTasks.Task10.Controllers.My_Tasks_10Controller import My_Tasks_10Controller


class MyTasks_10_View(Tk):
    def __init__(self):
        super().__init__()
        self.title("Дневник питания")
        self.geometry('1000x450')

        # Раздел Добавить
        self.frame_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_add.pack(anchor='center', fill=X, padx=10, pady=10)

        self.add_title = ttk.Label(self.frame_add, text="Добавить прием пищи")
        self.add_title.pack()

        # Прием пищи
        self.meal_label = ttk.Label(self.frame_add, text="Прием пищи")
        self.meal_label.pack()
        self.input_meal = ttk.Entry(self.frame_add)
        self.input_meal.pack()

        # Еда
        self.food_label = ttk.Label(self.frame_add, text="Еда")
        self.food_label.pack()
        self.input_food = ttk.Entry(self.frame_add)
        self.input_food.pack()

        # Калории
        self.calories_label = ttk.Label(self.frame_add, text="Калории")
        self.calories_label.pack()
        self.input_calories = ttk.Entry(self.frame_add)
        self.input_calories.pack()

        # Время
        self.time_label = ttk.Label(self.frame_add, text="Время")
        self.time_label.pack()
        self.input_time = ttk.Entry(self.frame_add)
        self.input_time.pack()

        self.add_button = ttk.Button(self.frame_add, text="Добавить", command=self.add_meal)
        self.add_button.pack(pady=5)

        # Кнопки управления
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(padx=10, pady=10)

        self.total_button = ttk.Button(
            self.button_frame,
            text="Калории за день",
            command=self.show_total_calories
        )
        self.total_button.pack(side=LEFT, padx=5)

        self.find_button = ttk.Button(
            self.button_frame,
            text="Найти по времени",
            command=self.find_by_time
        )
        self.find_button.pack(side=LEFT, padx=5)

        # Таблица
        self.frame_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_table.pack(anchor='center', fill=BOTH, expand=True, padx=10, pady=10)

        columns = ('id', 'meal', 'food', 'calories', 'time')
        self.tree = ttk.Treeview(self.frame_table, columns=columns, show="headings")
        self.tree.pack(fill=BOTH, expand=True)

        self.tree.heading('id', text="ID")
        self.tree.heading('meal', text="Прием пищи")
        self.tree.heading('food', text="Еда")
        self.tree.heading('calories', text="Калории")
        self.tree.heading('time', text="Время")

        self.update_table()

    def update_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        meals = My_Tasks_10Controller.get()
        for dict in meals:
            self.tree.insert("", END, values=(
                dict["id"],
                dict["meal"],
                dict["food"],
                dict["calories"],
                dict["time"]
            ))

    def add_meal(self):
        meal = self.input_meal.get().strip()
        food = self.input_food.get().strip()
        calories = self.input_calories.get().strip()
        time = self.input_time.get().strip()

        My_Tasks_10Controller.add(meal, food, calories, time)
        self.clear_input_fields()
        self.update_table()

    def show_total_calories(self):
        total = My_Tasks_10Controller.total_calories()
        self.show_found_meals(total)

    def find_by_time(self):
        time = self.input_time.get().strip()
        if not time:
            return

        result = My_Tasks_10Controller.find_by_time(time)
        self.show_found_meals(result)

    def clear_input_fields(self):
        self.input_meal.delete(0, END)
        self.input_food.delete(0, END)
        self.input_calories.delete(0, END)
        self.input_time.delete(0, END)

    def show_found_meals(self, meals):
        for item in self.tree.get_children():
            self.tree.delete(item)
        if isinstance(meals, list):
            for dict in meals:
                self.tree.insert("", END, values=(
                    dict["id"],
                    dict["meal"],
                    dict["food"],
                    dict["calories"],
                    dict["time"]
                ))
        else:
            self.tree.insert("", END, values=("—", "—", "—", meals, "—"))


if __name__ == "__main__":
    app = MyTasks_10_View()
    app.mainloop()