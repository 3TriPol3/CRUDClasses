class MyTasks_2:
    def __init__(self):
        self.__list_contacts = [
            {"id": 1, "name": "Иван", "phone": "+79123456789", "email": "ivan@mail.ru"},
            {"id": 2, "name": "Мария", "phone": "+79123456790", "email": "maria@mail.ru"}
        ]
        self.id = 3  # Следующий ID для нового контакта

    @property
    def contacts(self):
        return self.__list_contacts

    @contacts.setter
    def contacts(self, dict):
        dict['id'] = self.id
        self.__list_contacts.append(dict)
        self.id += 1


if __name__ == "__main__":
    contact = MyTasks_2()
    print(contact.contacts)
    contact.contacts = {"name": "Анна", "phone": "+79123456791", "email": "anna@mail.ru"}
    print(contact.contacts)