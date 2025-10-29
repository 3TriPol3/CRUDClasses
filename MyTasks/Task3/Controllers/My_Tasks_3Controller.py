from MyTasks.Task3.Models.MyTasks_3 import MyTasks_3


class My_Tasks_3Controller:
    obj = MyTasks_3()  # Создал объект класса MyTasks_3

    # Добавить продукт - Create
    @classmethod
    def add(cls, product, quantity, bought=False):
        cls.obj.products = {
            "product": product,
            "quantity": quantity,
            "bought": bought
        }
        return True

    # Прокси-метод
    @classmethod
    def get(cls):
        return cls.obj.products

    # Отметить как купленный
    @classmethod
    def mark_bought(cls, id):
        for dict in cls.get():
            if dict["id"] == id:
                dict["bought"] = True
                return dict
        return f"Продукта с ID {id} нет"

    # Показать некупленное
    @classmethod
    def show_unbought(cls):
        result = [dict for dict in cls.get() if not dict["bought"]]
        return result if result else "Все продукты куплены"

    # Удалить продукт
    @classmethod
    def delete(cls, id):
        for i, dict in enumerate(cls.get()):
            if dict["id"] == id:
                del cls.get()[i]
                return True
        return f"Продукта с ID {id} нет"


if __name__ == "__main__":
    print(My_Tasks_3Controller.get())
    print(My_Tasks_3Controller.add("Яблоки", 5))
    print(My_Tasks_3Controller.get())
    print(My_Tasks_3Controller.mark_bought(2))
    print(My_Tasks_3Controller.show_unbought())
    print(My_Tasks_3Controller.delete(1))
    print(My_Tasks_3Controller.get())