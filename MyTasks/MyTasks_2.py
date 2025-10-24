class MyTasks_2:
    '''
    : Система для хранения контактов с полями: id, name, phone, email
    '''

    def __init__(self):
        '''
        Конструктор в котором задаю атрибуты телефонной книги и идентификаторы телефонной книги
        Телефонная книга - состоит из словарей
        '''
        self.__contacts = [
            {"id": 1, "name": "Иван", "phone": "+79123456789", "email":"ivan@mail.ru"},
        ] # Атрибут класса - список с одной телефонной записью
        self.id = 2 # Атрибут класса - для автоматического создания id

    # Методы CRUD - Create, Read, Update, Delete
    # Добавить контакт - Create
    def add(self, name, phone, email):
        '''
        Создаёт новую запись в телефонной книге в виде словаря: {"id": 1, "name": "Иван", "phone": "+79123456789", "email":"ivan@mail.ru"}
        И добавляет в список атрибута self.contacts
        :Params
            name(str): Имя в виде строки
            id(int): Создаётся автогматически с помощью атрибута self.id
            phone(int): Телефонный номер int
            email(str): Электронная почта в виде строки
        :Returns:
        '''
        self.contacts.append(
            {
                "id": self.id,
                "name": name,
                "phone": phone,
                "email": email
            }
        )
        self.id += 1 # Увеличить на 1, следующий id будет на 1 больше
        return True

        # Показать всё
    @property
    def contacts(self):
        '''
        Выводит информацию о всех записях в телефонной книге
        :Returns: Возвращает список словарей с записями
        '''
        return self.__contacts

    # Найти по имени - Read
    def show_name(self, name):
        for dict in self.__contacts:
            if dict['name'] == name:
                return dict
            else:
                return f'Запись с таким именем не существует'

    # Отметить выполненое - Update
    def update(self, id, **kwargs):
        '''
        Обновляет запись в телефонной книге
        :Params:
        id Словарь с данным id
        kwargs "Любой ключ":"значение этого ключа"
        :Returns:
            contact - словарь
        '''
        for dict in self.__contacts:
            if dict['id'] == id:
                if 'id' in kwargs:
                    if self.show_name(kwargs['name']) is not None:
                        return f'Запись с таким телефонным номером уже существует'
                dict.update(kwargs)

    # Удалить - Delete
    def delete(self, id):
        for dict in self.__contacts:
            if dict['id'] == id:
                self.__contacts.remove(dict)

if __name__ == "__main__":
    contact = MyTasks_2()
    print(contact.contacts)
    contact.add('Максим', '+79123456789', 'maxim@mail.ru' ) # Добавление контакта
    contact.add('Антон', '+79384174814', 'anton@mail.ru')
    print(contact.contacts)
    print(contact.show_name('Иван')) # Найти по имени
    print(contact.contacts)
    contact.update(1, phone='+79199999999') # Обновить телефон
    print(contact.contacts)
    contact.delete(2) # Удалить контакт
    print(contact.contacts)
