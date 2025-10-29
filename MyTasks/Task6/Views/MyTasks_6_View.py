from tkinter import *
from tkinter import ttk
from MyTasks.Task6.Controllers.My_Tasks_6Controller import My_Tasks_6Controller


class MyTasks_6_View(Tk):
    def __init__(self):
        super().__init__()
        self.title("Учет личных расходов")
        self.geometry('1000x450')

        # Раздел Добавить
        self.frame_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_add.pack(anchor='center', fill=X, padx=10, pady=10)

        self.add_title = ttk.Label(self.frame_add, text="Добавить расход")
        self.add_title.pack()

        # Сумма
        self.amount_label = ttk.Label(self.frame_add, text="Сумма")
        self.amount_label.pack()
        self.input_amount = ttk.Entry(self.frame_add)
        self.input_amount.pack()

        # Категория
        self.category_label = ttk.Label(self.frame_add, text="Категория")
        self.category_label.pack()
        self.input_category = ttk.Entry(self.frame_add)
        self.input_category.pack()

        # Дата
        self.date_label = ttk.Label(self.frame_add, text="Дата (ГГГГ-ММ-ДД)")
        self.date_label.pack()
        self.input_date = ttk.Entry(self.frame_add)
        self.input_date.pack()

        # Описание
        self.description_label = ttk.Label(self.frame_add, text="Описание")
        self.description_label.pack()
        self.input_description = ttk.Entry(self.frame_add)
        self.input_description.pack()

        self.add_button = ttk.Button(self.frame_add, text="Добавить", command=self.add_expense)
        self.add_button.pack(pady=5)

        # Кнопки управления
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(padx=10, pady=10)

        self.total_button = ttk.Button(
            self.button_frame,
            text="Сумма по категории",
            command=self.show_total_by_category
        )
        self.total_button.pack(side=LEFT, padx=5)

        self.period_button = ttk.Button(
            self.button_frame,
            text="Расходы за период",
            command=self.show_expenses_in_period
        )
        self.period_button.pack(side=LEFT, padx=5)

        # Таблица
        self.frame_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_table.pack(anchor='center', fill=BOTH, expand=True, padx=10, pady=10)

        columns = ('id', 'amount', 'category', 'date', 'description')
        self.tree = ttk.Treeview(self.frame_table, columns=columns, show="headings")
        self.tree.pack(fill=BOTH, expand=True)

        self.tree.heading('id', text="ID")
        self.tree.heading('amount', text="Сумма")
        self.tree.heading('category', text="Категория")
        self.tree.heading('date', text="Дата")
        self.tree.heading('description', text="Описание")

        self.update_table()

    def update_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        expenses = My_Tasks_6Controller.get()
        for dict in expenses:
            self.tree.insert("", END, values=(
                dict["id"],
                dict["amount"],
                dict["category"],
                dict["date"],
                dict["description"]
            ))

    def add_expense(self):
        amount = self.input_amount.get().strip()
        category = self.input_category.get().strip()
        date = self.input_date.get().strip()
        description = self.input_description.get().strip()

        My_Tasks_6Controller.add(amount, category, date, description)
        self.clear_input_fields()
        self.update_table()

    def show_total_by_category(self):
        category = self.input_category.get().strip()
        total = My_Tasks_6Controller.total_by_category(category)
        self.show_found_expenses(total)

    def show_expenses_in_period(self):
        start_date = self.input_date.get().strip()
        end_date = self.input_description.get().strip()
        expenses = My_Tasks_6Controller.expenses_in_period(start_date, end_date)
        self.show_found_expenses(expenses)

    def clear_input_fields(self):
        self.input_amount.delete(0, END)
        self.input_category.delete(0, END)
        self.input_date.delete(0, END)
        self.input_description.delete(0, END)

    def show_found_expenses(self, expenses):
        for item in self.tree.get_children():
            self.tree.delete(item)
        if isinstance(expenses, list):
            for dict in expenses:
                self.tree.insert("", END, values=(
                    dict["id"],
                    dict["amount"],
                    dict["category"],
                    dict["date"],
                    dict["description"]
                ))
        else:
            self.tree.insert("", END, values=("—", expenses, "—", "—", "—"))