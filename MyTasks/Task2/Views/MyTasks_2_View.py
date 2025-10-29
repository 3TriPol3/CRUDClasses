from tkinter import *
from tkinter import ttk
from MyTasks.Task2.Controllers.My_Tasks_2Controller import My_Tasks_2Controller


class MyTasks_2_View(Tk):
    def __init__(self):
        super().__init__()
        self.title("Телефонная книга")
        self.geometry('1000x400')

        # Раздел Добавить
        self.frame_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_add.pack(anchor='center', fill=X, padx=10, pady=10)

        self.add_title = ttk.Label(self.frame_add, text="Добавить контакт")
        self.add_title.pack()

        # Имя
        self.name_label = ttk.Label(self.frame_add, text="Имя")
        self.name_label.pack()
        self.input_name = ttk.Entry(self.frame_add)
        self.input_name.pack()

        # Телефон
        self.phone_label = ttk.Label(self.frame_add, text="Телефон")
        self.phone_label.pack()
        self.input_phone = ttk.Entry(self.frame_add)
        self.input_phone.pack()

        # Email
        self.email_label = ttk.Label(self.frame_add, text="Email")
        self.email_label.pack()
        self.input_email = ttk.Entry(self.frame_add)
        self.input_email.pack()

        self.add_button = ttk.Button(self.frame_add, text="Добавить", command=self.add_contact)
        self.add_button.pack(pady=5)

        # Кнопки управления
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(padx=10, pady=10)

        self.find_button = ttk.Button(
            self.button_frame,
            text="Найти по имени",
            command=self.find_contact
        )
        self.find_button.pack(side=LEFT, padx=5)

        self.update_button = ttk.Button(
            self.button_frame,
            text="Обновить телефон",
            command=self.update_phone
        )
        self.update_button.pack(side=LEFT, padx=5)

        self.delete_button = ttk.Button(
            self.button_frame,
            text="Удалить",
            command=self.delete_contact
        )
        self.delete_button.pack(side=LEFT, padx=5)

        # Таблица
        self.frame_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_table.pack(anchor='center', fill=BOTH, expand=True, padx=10, pady=10)

        columns = ('id', 'name', 'phone', 'email')
        self.tree = ttk.Treeview(self.frame_table, columns=columns, show="headings")
        self.tree.pack(fill=BOTH, expand=True)

        self.tree.heading('id', text="ID")
        self.tree.heading('name', text="Имя")
        self.tree.heading('phone', text="Телефон")
        self.tree.heading('email', text="Email")

        self.update_table()

    def update_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        contacts = My_Tasks_2Controller.get()
        for dict in contacts:
            self.tree.insert("", END, values=(
                dict["id"],
                dict["name"],
                dict["phone"],
                dict["email"]
            ))

    def add_contact(self):
        name = self.input_name.get().strip()
        phone = self.input_phone.get().strip()
        email = self.input_email.get().strip()

        if not all([name, phone, email]):
            return

        My_Tasks_2Controller.add(name, phone, email)
        self.clear_input_fields()
        self.update_table()

    def find_contact(self):
        name = self.input_name.get().strip()
        if not name:
            return

        result = My_Tasks_2Controller.find_by_name(name)
        self.show_found_contacts(result)
        self.update_table()

    def update_phone(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        contact_id = int(self.tree.item(selected_item, "values")[0])
        new_phone = self.input_phone.get().strip()

        if not new_phone:
            return

        My_Tasks_2Controller.update_phone(contact_id, new_phone)
        self.update_table()

    def delete_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        contact_id = int(self.tree.item(selected_item, "values")[0])
        My_Tasks_2Controller.delete(contact_id)
        self.update_table()

    def clear_input_fields(self):
        self.input_name.delete(0, END)
        self.input_phone.delete(0, END)
        self.input_email.delete(0, END)

    def show_found_contacts(self, contacts):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for dict in contacts:
            self.tree.insert("", END, values=(
                dict["id"],
                dict["name"],
                dict["phone"],
                dict["email"]
            ))


if __name__ == "__main__":
    app = MyTasks_2_View()
    app.mainloop()