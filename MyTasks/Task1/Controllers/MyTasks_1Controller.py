from MyTasks.Task1.Models.MyTasks_1 import MyTasks_1

class MyTasks_1Controller:
    '''
   Класс для описания списка задач
     Методы:
     добавить,
     показать все,
     отметить выполненной,
      удалить
     '''
    # CRUD
    obj = MyTasks_1() # Создал объект класса Pet

    # Добавить дело - Create
    @classmethod
    def add(cls, task):
        cls.obj.tasks(
            {
                "task": task,
                "completed": False
            }
        )
        return True

    # Показать всё - Read
    @classmethod
    def tasks(cls):
        '''
        Выводит информацию о делах
        :Returns: Возвращает список словарей с делами
        '''
        return cls.obj.tasks

    # Отметить выполненое - Update
    @classmethod
    def completed(cls, id):
        '''
        Меняет значения completed на True у словаря с id == id из аргумента
        :Params id: Словарь с данным id
        :Returns:
            Task - словарь
        '''
        for dict in cls.obj.tasks:
            if dict['id'] == id:
                dict['complete'] = True
                return dict

    # Удалить - Delete
    @classmethod
    def delete(cls, id):
        for dict in cls.obj.tasks:
            if dict['id'] == id:
                cls.obj.tasks.remove(dict)


if __name__ == "__main__":
    print(MyTasks_1Controller.tasks())
    print(MyTasks_1Controller.add('Купить хлеб'))
    print(MyTasks_1Controller.tasks())
    print(MyTasks_1Controller.completed(2))
    print(MyTasks_1Controller.delete('Мария'))