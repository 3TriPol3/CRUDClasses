from tkinter import *
from tkinter import ttk
from MyTasks.Task3.Controllers.My_Tasks_3Controller import My_Tasks_3Controller


class MyTasks_3_View(Tk):
    def __init__(self):
        super().__init__()
        self.title("Список покупок")
        self.geometry('800x400')

        # Раздел Добавить
        self.frame_add = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_add.pack(anchor='center', fill=X, padx=10, pady=10)

        self.add_title = ttk.Label(self.frame_add, text="Добавить продукт")
        self.add_title.pack()

        # Продукт
        self.product_label = ttk.Label(self.frame_add, text="Продукт")
        self.product_label.pack()
        self.input_product = ttk.Entry(self.frame_add)
        self.input_product.pack()

        # Количество
        self.quantity_label = ttk.Label(self.frame_add, text="Количество")
        self.quantity_label.pack()
        self.input_quantity = ttk.Entry(self.frame_add)
        self.input_quantity.pack()

        self.add_button = ttk.Button(self.frame_add, text="Добавить", command=self.add_product)
        self.add_button.pack(pady=5)

        # Кнопки управления
        self.button_frame = ttk.Frame(self)
        self.button_frame.pack(padx=10, pady=10)

        self.mark_bought_button = ttk.Button(
            self.button_frame,
            text="Отметить как купленный",
            command=self.mark_bought
        )
        self.mark_bought_button.pack(side=LEFT, padx=5)

        self.show_unbought_button = ttk.Button(
            self.button_frame,
            text="Показать некупленное",
            command=self.show_unbought
        )
        self.show_unbought_button.pack(side=LEFT, padx=5)

        self.delete_button = ttk.Button(
            self.button_frame,
            text="Удалить",
            command=self.delete_product
        )
        self.delete_button.pack(side=LEFT, padx=5)

        # Таблица
        self.frame_table = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[10, 10])
        self.frame_table.pack(anchor='center', fill=BOTH, expand=True, padx=10, pady=10)

        columns = ('id', 'product', 'quantity', 'bought')
        self.tree = ttk.Treeview(self.frame_table, columns=columns, show="headings")
        self.tree.pack(fill=BOTH, expand=True)

        self.tree.heading('id', text="ID")
        self.tree.heading('product', text="Продукт")
        self.tree.heading('quantity', text="Количество")
        self.tree.heading('bought', text="Статус")

        self.update_table()

    def update_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        products = My_Tasks_3Controller.get()
        for dict in products:
            status = "Куплен" if dict["bought"] else "Не куплен"
            self.tree.insert("", END, values=(
                dict["id"],
                dict["product"],
                dict["quantity"],
                status
            ))

    def add_product(self):
        product_text = self.input_product.get().strip()
        quantity_text = self.input_quantity.get().strip()

        if not product_text or not quantity_text:
            return

        try:
            quantity = int(quantity_text)
        except ValueError:
            return

        My_Tasks_3Controller.add(product_text, quantity)
        self.clear_input_fields()
        self.update_table()

    def mark_bought(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        product_id = int(self.tree.item(selected_item, "values")[0])
        My_Tasks_3Controller.mark_bought(product_id)
        self.update_table()

    def show_unbought(self):
        result = My_Tasks_3Controller.show_unbought()
        self.show_found_products(result)
        self.update_table()

    def delete_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        product_id = int(self.tree.item(selected_item, "values")[0])
        My_Tasks_3Controller.delete(product_id)
        self.update_table()

    def clear_input_fields(self):
        self.input_product.delete(0, END)
        self.input_quantity.delete(0, END)

    def show_found_products(self, products):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for dict in products:
            status = "Куплен" if dict["bought"] else "Не куплен"
            self.tree.insert("", END, values=(
                dict["id"],
                dict["product"],
                dict["quantity"],
                status
            ))


if __name__ == "__main__":
    app = MyTasks_3_View()
    app.mainloop()