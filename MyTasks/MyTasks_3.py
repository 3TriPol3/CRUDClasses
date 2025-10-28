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
        product(str): Название продукта в виде строки
        quantity(int): Количество продуктов
        bought(boolean): Отмечает купил или нет
        :Returns:
        '''
        self.shopping_list.append(
            {
                "id": self.id,
                "product": product,
                "quantity": quantity,
                "bought": False
            }
        )
        self.id += 1 # Увеличить на 1, следующий id будет на 1 больше
        return True

    # Отметить купленным
    def bought(self, id):
        '''
        Меняет значения bought на True у словаря с id == id из аргумента
        :Params id: Словарь с данным id
        :Returns:
        list - словарь
        '''
        for dict in self.__shopping_list:
             if dict['id'] == id:
                dict['bought'] = True
                return dict

    # Вывести некупленное
    def show_not_brought(self):
        for item in self.__shopping_list:
            if not item['bought']:
                print(f"{item['product']} - {item['quantity']} шт.")

    # Удалить - Delete
    def delete(self, id):
        for dict in self.__shopping_list:
            if dict['id'] == id:
                self.__shopping_list.remove(dict)

    # Показать всё
    @property
    def shopping_list(self):
        '''
        Выводит информацию о всех продуктах
        :Returns: Возвращает список словарей с продуктами
        '''
        return self.__shopping_list



if __name__ == "__main__":
    list = MyTasks_3()
    print(list.shopping_list)
    list.add('Шоколад', '4', False) # Добавление продукта
    print(list.shopping_list)
    print('Метод изменить статус', list.bought(3))
    print(list.shopping_list)
    list.show_not_brought()
    print(list.shopping_list)
    list.delete(2)  # Удалить продукт
    print(list.shopping_list)