from tkinter import *
from tkinter import ttk
from MyTasks.Task1.Controllers.My_Tasks_1Controller import My_Tasks_1Controller


class MyTasks_1_View(Tk):
    def __init__(self):
        super().__init__()
        self.title("Список дел")
        self.geometry('800x400')

        # Раздел Добавить
        self.frame_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_add.pack(anchor='center', fill=X, padx=10, pady=10)

        self.add_title = ttk.Label(self.frame_add, text="Добавить задачу")
        self.add_title.pack()

        # Задача
        self.task_label = ttk.Label(self.frame_add, text="Введите задачу")
        self.task_label.pack()
        self.input_task = ttk.Entry(self.frame_add)
        self.input_task.pack()

        self.add_button = ttk.Button(self.frame_add, text="Добавить", command=self.add_task)
        self.add_button.pack(pady=5)

        # Кнопки управления
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(padx=10, pady=10)

        self.complete_button = ttk.Button(
            self.button_frame,
            text="Отметить как выполненную",
            command=self.mark_complete
        )
        self.complete_button.pack(side=LEFT, padx=5)

        self.delete_button = ttk.Button(
            self.button_frame,
            text="Удалить",
            command=self.delete_task
        )
        self.delete_button.pack(side=LEFT, padx=5)

        # Таблица
        self.frame_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_table.pack(anchor='center', fill=BOTH, expand=True, padx=10, pady=10)

        columns = ('id', 'task', 'completed')
        self.tree = ttk.Treeview(self.frame_table, columns=columns, show="headings")
        self.tree.pack(fill=BOTH, expand=True)

        self.tree.heading('id', text="ID")
        self.tree.heading('task', text="Задача")
        self.tree.heading('completed', text="Статус")

        self.update_table()

    def update_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        tasks = My_Tasks_1Controller.get()
        for dict in tasks:
            status = "Выполнено" if dict["completed"] else "Не выполнено"
            self.tree.insert("", END, values=(dict["id"], dict["task"], status))

    def add_task(self):
        task_text = self.input_task.get().strip()
        if not task_text:
            return

        My_Tasks_1Controller.add(task_text)
        self.input_task.delete(0, END)
        self.update_table()

    def mark_complete(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        task_id = int(self.tree.item(selected_item, "values")[0])
        My_Tasks_1Controller.completed(task_id)
        self.update_table()

    def delete_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        task_id = int(self.tree.item(selected_item, "values")[0])
        My_Tasks_1Controller.delete(task_id)
        self.update_table()


if __name__ == "__main__":
    app = MyTasks_1_View()
    app.mainloop()