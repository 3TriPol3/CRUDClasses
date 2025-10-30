# class MyTasks_2:
#     def __init__(self):
#         self.__list_contacts = [
#             {"id": 1, "name": "Иван", "phone": "+79123456789", "email": "ivan@mail.ru"},
#             {"id": 2, "name": "Мария", "phone": "+79123456790", "email": "maria@mail.ru"}
#         ]
#         self.id = 3  # Следующий ID для нового контакта
#
#     @property
#     def contacts(self):
#         return self.__list_contacts
#
#     @contacts.setter
#     def contacts(self, dict):
#         dict['id'] = self.id
#         self.__list_contacts.append(dict)
#         self.id += 1
#
#
# if __name__ == "__main__":
#     contact = MyTasks_2()
#     print(contact.contacts)
#     contact.contacts = {"name": "Анна", "phone": "+79123456791", "email": "anna@mail.ru"}
#     print(contact.contacts)



class MyTasks_2:
    '''
    Класс для контактов в телефоне в виде  {"id": 1, "name": "Иван", "phone": "+79123456789", "email": "ivan@mail.ru"}
    Класс хранит список словарей [
    {"id": 1, "name": "Иван", "phone": "+79123456789", "email": "ivan@mail.ru"}
    ]
    '''
    def __init__(self):
        self.__list_contacts = [
            {"id": 1, "name": "Иван", "phone": "+79123456789", "email": "ivan@mail.ru"}
        ]
        self.id = 2 # Следующий ID для нового контакта

    #Геттер - выводит список контактов
    @property
    def contacts(self):
        '''
        Returns:
        Список словарей
        '''
        return self.__list_contacts

    # Сеттер - добавит в список словарь с контактами
    @contacts.setter
    def contacts(self, dict):
        dict['id'] = self.id # Присвоить ключу id в словаре значение атрибута self.id
        self.contacts.append(dict) # Через геттер contacts получаем список словарей и добавляем новый словарь
        self.id += 1 # Увеличить на 1

    # # Аналог Геттера
    # def get_contacts(self):
    #     return self.__list_contacts
    #
    # # Аналог Сеттера
    # def set_contacts(self, dict):
    #     dict['id'] = self.id
    #     self.get_contacts().append(dict)
    #     self.id += 1


if __name__ == "__main__":
    con = MyTasks_2()
    print(con.contacts)
    con.contacts = {"name": "Света"}
    print(con.contacts)
    con.contacts = {}
    print(con.contacts)
    # print("**************************")
    # print(con.get_contacts())
    # con.set_contacts({"name": "Пётр"})
    # print(con.get_contacts())