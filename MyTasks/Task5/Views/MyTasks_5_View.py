from tkinter import *
from tkinter import ttk
from MyTasks.Task5.Controllers.My_Tasks_5Controller import My_Tasks_5Controller


class MyTasks_5_View(Tk):
    def __init__(self):
        super().__init__()
        self.title("Список студентов")
        self.geometry('1000x400')

        # Раздел Добавить
        self.frame_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_add.pack(anchor='center', fill=X, padx=10, pady=10)

        self.add_title = ttk.Label(self.frame_add, text="Добавить студента")
        self.add_title.pack()

        # Имя
        self.name_label = ttk.Label(self.frame_add, text="Имя")
        self.name_label.pack()
        self.input_name = ttk.Entry(self.frame_add)
        self.input_name.pack()

        # Возраст
        self.age_label = ttk.Label(self.frame_add, text="Возраст")
        self.age_label.pack()
        self.input_age = ttk.Entry(self.frame_add)
        self.input_age.pack()

        # Оценка
        self.grade_label = ttk.Label(self.frame_add, text="Оценка")
        self.grade_label.pack()
        self.input_grade = ttk.Entry(self.frame_add)
        self.input_grade.pack()

        self.add_button = ttk.Button(self.frame_add, text="Добавить", command=self.add_student)
        self.add_button.pack(pady=5)

        # Кнопки управления
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(padx=10, pady=10)

        self.update_button = ttk.Button(
            self.button_frame,
            text="Обновить оценку",
            command=self.update_grade
        )
        self.update_button.pack(side=LEFT, padx=5)

        self.find_button = ttk.Button(
            self.button_frame,
            text="Найти по имени",
            command=self.find_student
        )
        self.find_button.pack(side=LEFT, padx=5)

        self.delete_button = ttk.Button(
            self.button_frame,
            text="Удалить",
            command=self.delete_student
        )
        self.delete_button.pack(side=LEFT, padx=5)

        # Таблица
        self.frame_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_table.pack(anchor='center', fill=BOTH, expand=True, padx=10, pady=10)

        columns = ('id', 'name', 'age', 'grade')
        self.tree = ttk.Treeview(self.frame_table, columns=columns, show="headings")
        self.tree.pack(fill=BOTH, expand=True)

        self.tree.heading('id', text="ID")
        self.tree.heading('name', text="Имя")
        self.tree.heading('age', text="Возраст")
        self.tree.heading('grade', text="Оценка")

        self.update_table()

    def update_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        students = My_Tasks_5Controller.get()
        for dict in students:
            self.tree.insert("", END, values=(
                dict["id"],
                dict["name"],
                dict["age"],
                dict["grade"]
            ))

    def add_student(self):
        name = self.input_name.get().strip()
        age = self.input_age.get().strip()
        grade = self.input_grade.get().strip()

        if not all([name, age, grade]):
            return

        try:
            age = int(age)
        except ValueError:
            return

        My_Tasks_5Controller.add(name, age, grade)
        self.clear_input_fields()
        self.update_table()

    def update_grade(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        student_id = int(self.tree.item(selected_item, "values")[0])
        new_grade = self.input_grade.get().strip()

        if not new_grade:
            return

        My_Tasks_5Controller.update_grade(student_id, new_grade)
        self.update_table()

    def find_student(self):
        name = self.input_name.get().strip()
        if not name:
            return

        result = My_Tasks_5Controller.find_by_name(name)
        self.show_found_students(result)
        self.update_table()

    def delete_student(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        student_id = int(self.tree.item(selected_item, "values")[0])
        My_Tasks_5Controller.delete(student_id)
        self.update_table()

    def clear_input_fields(self):
        self.input_name.delete(0, END)
        self.input_age.delete(0, END)
        self.input_grade.delete(0, END)

    def show_found_students(self, students):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for dict in students:
            self.tree.insert("", END, values=(
                dict["id"],
                dict["name"],
                dict["age"],
                dict["grade"]
            ))


if __name__ == "__main__":
    app = MyTasks_5_View()
    app.mainloop()