from tkinter import *
from tkinter import ttk
from MyTasks.Task8.Controllers.My_Tasks_8Controller import My_Tasks_8Controller


class MyTasks_8_View(Tk):
    def __init__(self):
        super().__init__()
        self.title("Учет сотрудников")
        self.geometry('1000x450')

        # Раздел Добавить
        self.frame_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_add.pack(anchor='center', fill=X, padx=10, pady=10)

        self.add_title = ttk.Label(self.frame_add, text="Добавить сотрудника")
        self.add_title.pack()

        # Имя
        self.name_label = ttk.Label(self.frame_add, text="Имя")
        self.name_label.pack()
        self.input_name = ttk.Entry(self.frame_add)
        self.input_name.pack()

        # Должность
        self.position_label = ttk.Label(self.frame_add, text="Должность")
        self.position_label.pack()
        self.input_position = ttk.Entry(self.frame_add)
        self.input_position.pack()

        # Зарплата
        self.salary_label = ttk.Label(self.frame_add, text="Зарплата")
        self.salary_label.pack()
        self.input_salary = ttk.Entry(self.frame_add)
        self.input_salary.pack()

        # Отдел
        self.department_label = ttk.Label(self.frame_add, text="Отдел")
        self.department_label.pack()
        self.input_department = ttk.Entry(self.frame_add)
        self.input_department.pack()

        self.add_button = ttk.Button(self.frame_add, text="Добавить", command=self.add_employee)
        self.add_button.pack(pady=5)

        # Кнопки управления
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(padx=10, pady=10)

        self.raise_button = ttk.Button(
            self.button_frame,
            text="Повысить зарплату",
            command=self.raise_salary
        )
        self.raise_button.pack(side=LEFT, padx=5)

        self.filter_button = ttk.Button(
            self.button_frame,
            text="Сотрудники отдела",
            command=self.filter_by_department
        )
        self.filter_button.pack(side=LEFT, padx=5)

        self.fire_button = ttk.Button(
            self.button_frame,
            text="Уволить",
            command=self.fire_employee
        )
        self.fire_button.pack(side=LEFT, padx=5)

        # Таблица
        self.frame_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_table.pack(anchor='center', fill=BOTH, expand=True, padx=10, pady=10)

        columns = ('id', 'name', 'position', 'salary', 'department')
        self.tree = ttk.Treeview(self.frame_table, columns=columns, show="headings")
        self.tree.pack(fill=BOTH, expand=True)

        self.tree.heading('id', text="ID")
        self.tree.heading('name', text="Имя")
        self.tree.heading('position', text="Должность")
        self.tree.heading('salary', text="Зарплата")
        self.tree.heading('department', text="Отдел")

        self.update_table()

    def update_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        employees = My_Tasks_8Controller.get()
        for dict in employees:
            self.tree.insert("", END, values=(
                dict["id"],
                dict["name"],
                dict["position"],
                dict["salary"],
                dict["department"]
            ))

    def add_employee(self):
        name = self.input_name.get().strip()
        position = self.input_position.get().strip()
        salary = self.input_salary.get().strip()
        department = self.input_department.get().strip()

        My_Tasks_8Controller.add(name, position, salary, department)
        self.clear_input_fields()
        self.update_table()

    def raise_salary(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        employee_id = int(self.tree.item(selected_item, "values")[0])
        amount = self.input_salary.get().strip()
        if not amount:
            return

        try:
            amount = int(amount)
        except ValueError:
            return

        My_Tasks_8Controller.increase_salary(employee_id, amount)
        self.update_table()

    def filter_by_department(self):
        department = self.input_department.get().strip()
        if not department:
            return

        result = My_Tasks_8Controller.get_by_department(department)
        self.show_found_employees(result)

    def fire_employee(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        employee_id = int(self.tree.item(selected_item, "values")[0])
        My_Tasks_8Controller.fire(employee_id)
        self.update_table()

    def clear_input_fields(self):
        self.input_name.delete(0, END)
        self.input_position.delete(0, END)
        self.input_salary.delete(0, END)
        self.input_department.delete(0, END)

    def show_found_employees(self, employees):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for dict in employees:
            self.tree.insert("", END, values=(
                dict["id"],
                dict["name"],
                dict["position"],
                dict["salary"],
                dict["department"]
            ))