class MyTasks_1:
    '''
    Класс для описания списка задач

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

    @property  # Геттер
    def tasks(self):
        '''

        :Returns:
        список задач
        '''
        return self.__tasks

    @tasks.setter  # Сеттер
    def tasks(self, dict):
        dict['id'] = self.id
        self.tasks.append(dict)
        self.id += 1

if __name__ == "__main__":
    task = MyTasks_1()
    print(task.tasks)
    task.tasks =  {"id": 1, "task": "Купить молоко", "completed": False}
    print(task.tasks)



