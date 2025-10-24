class MyTasks_3:
    '''
    : Список покупок с полями: id, product, quantity, bought
    '''

    def __init__(self):
        '''
        Конструктор в котором задаю атрибуты списка покупок и идентификаторы списка покупок
        Список покупок - состоит из словарей
        '''
        self.__shopping_list = [
            {"id": 1, "product": "Хлеб", "quantity": 1, "bought": False},
            {"id": 2, "product": "Молоко", "quantity": 2, "bought": True}
        ] # Атрибут класса - список с одной покупкой
        self.id = 2 # Атрибут класса - для автоматического создания id

    # Методы CRUD - Create, Read, Update, Delete
    # Добавить прордукт - Create
    def add(self, product, quantity, bought):
        '''
        Создаёт новую покупку в виде словаря: {"id": 1, "product": "Хлеб", "quantity": 1, "bought": False}
        И добавляет в список атрибута self.shopping_list
        :Params
            product(str): Имя в виде строки
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
        return self.__shopping_list

    # Найти по имени - Read
    def show_name(self, name):
        for dict in self.__shopping_list:
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
        for dict in self.__shopping_list:
            if dict['id'] == id:
                if 'id' in kwargs:
                    if self.show_name(kwargs['name']) is not None:
                        return f'Запись с таким телефонным номером уже существует'
                dict.update(kwargs)

    # Удалить - Delete
    def delete(self, id):
        for dict in self.__shopping_list:
            if dict['id'] == id:
                self.__shopping_list.remove(dict)

if __name__ == "__main__":
    contact = MyTasks_3()
    print(contact.contacts)
    contact.add('Максим', '+79123456789', 'ivan@mail.ru' ) # Добавление контакта
    print(contact.contacts)
    print(contact.show_name('Иван')) # Найти по имени
    print(contact.contacts)
    contact.update(1, phone='+79199999999') # Обновить телефон
    print(contact.contacts)
    contact.delete(2) # Удалить контакт
    print(contact.contacts)
