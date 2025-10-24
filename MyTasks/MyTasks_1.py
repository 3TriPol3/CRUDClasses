class MyTasks_1:
    '''
    : Управлять списком задач с полями: id, задача, статус (выполнено/невыполнено)

    '''

    def __init__(self):
        '''
        Конструктор в котором задаю атрибуты список дел и идентификаторы дел
        Список дел - состоит из словарей
        '''
        self.__tasks = [
            {"id": 1, "task": "Купить молоко", "completed": False},
            {"id": 2, "task": "Сделать уроки", "completed": True}
        ] # Атрибут класса - список с двумя делами
        self.id = 3 # Атрибут класса - для автоматического создания id

    # Методы CRUD - Create, Read, Update, Delete
    #Добавить дело - Create
    def add(self, task):
        '''
        Создаёт новое дело в виде словаря: {"id": 1, "task": "Купить молоко", "completed": False}
        И добавляет в список атрибута self.tasks
        :Params
            task(str): Дело в виде строки
            id(int): Создаётся автогматически с помощью атрибута self.id
            completed(boolean): Автоматически присваивается False
        :Returns:
            True
        '''
        self.tasks.append(
            {
                "id": self.id,
                "task": task,
                "completed": False
            }
        )
        self.id += 1 # Увеличить на 1, следующий id будет на 1 больше
        return True
        # Показать всё - Read
    @property
    def tasks(self):
        '''
        Выводит информацию о делах
        :Returns: Возвращает список словарей с делами
        '''
        return self.__tasks
    # Отметить выполненое - Update
    def completed(self, id):
        '''
        Меняет значения completed на True у словаря с id == id из аргумента
        :Params id: Словарь с данным id
        :Returns:
            Task - словарь
        '''
        for dict in self.__tasks:
            if dict['id'] == id:
                dict['complete'] = True
                return dict
    # Удалить - Delete
    def delete(self, id):
        for dict in self.__tasks:
            if dict['id'] == id:
                self.__tasks.remove(dict)

if __name__ == "__main__":
    task = MyTasks_1()
    print(task.tasks)
    task.add("Сходить в ЯМК")
    print(task.tasks)
    print('Метод изменить статус', task.completed(3))
    print(task.tasks)
    task.delete(1)
    print(task.tasks)