# from MyTasks.Task2.Models.MyTasks_2 import MyTasks_2
#
#
# class My_Tasks_2Controller:
#     obj = MyTasks_2()  # Создал объект класса MyTasks_2
#
#     # Добавить контакт - Create
#     @classmethod
#     def add(cls, name, phone, email):
#         cls.obj.contacts = {
#             "name": name,
#             "phone": phone,
#             "email": email
#         }
#         return True
#
#     # Прокси-метод
#     @classmethod
#     def get(cls):
#         return cls.obj.contacts
#
#     # Найти по имени
#     @classmethod
#     def find_by_name(cls, name):
#         result = []
#         for dict in cls.get():
#             if dict["name"].lower() == name.lower():
#                 result.append(dict)
#         return result if result else f"Контакт '{name}' не найден"
#
#     # Обновить телефон
#     @classmethod
#     def update_phone(cls, id, new_phone):
#         for dict in cls.get():
#             if dict["id"] == id:
#                 dict["phone"] = new_phone
#                 return dict
#         return f"Контакта с ID {id} нет"
#
#     # Удалить контакт
#     @classmethod
#     def delete(cls, id):
#         for i, dict in enumerate(cls.get()):
#             if dict["id"] == id:
#                 del cls.get()[i]
#                 return True
#         return f"Контакта с ID {id} нет"
#
#
# if __name__ == "__main__":
#     print(My_Tasks_2Controller.get())
#     print(My_Tasks_2Controller.add("Петр", "+79123456792", "petr@mail.ru"))
#     print(My_Tasks_2Controller.get())
#     print(My_Tasks_2Controller.find_by_name("Иван"))
#     print(My_Tasks_2Controller.update_phone(2, "+79123456799"))
#     print(My_Tasks_2Controller.delete(1))
#     print(My_Tasks_2Controller.get())


from MyTasks.Task2.Models.MyTasks_2 import MyTasks_2


class My_Tasks_2Controller():
    '''
    Управляет контактами в классе MyTasks_2 (Contact)
    Методы:
        добавить контакт,
        найти по имени,
        обновить телефон,
        удалить контакт
    '''
    obj = MyTasks_2()
    # Прокси метод вывода всех контактов
    @classmethod
    def get(cls):
        return cls.obj.contacts


    # добавить контакт
    @classmethod
    def add(cls, name, phone, email):
        cls.obj.contacts = {
            "name": name,
            "phone": phone,
            "email": email
        }
    #Обновить телефон
    @classmethod
    def update_phone(cls, id, new_phone):
        for dict in cls.get():
            if dict['id'] == id:
                dict['phone'] = new_phone

    @classmethod
    def delete(cls, id):
        for dict in cls.get():
            if dict['id'] == id:
                cls.get().remove(dict)

if __name__ == "__main__":

    print(My_Tasks_2Controller.get())   # Получение(вывод) всех контактов
    My_Tasks_2Controller.add('Василий', "+78888888888", "vas@vas.ru") # Добавление контакта
    print(My_Tasks_2Controller.get())
    My_Tasks_2Controller.update_phone(2, "+77777777777") # Обновление телефона
    print(My_Tasks_2Controller.get())
    My_Tasks_2Controller.delete(1) # Удаление контакта
    print(My_Tasks_2Controller.get())