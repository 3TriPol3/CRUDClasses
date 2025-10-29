from MyTasks.Task1.Models.MyTasks_1 import MyTasks_1


class My_Tasks_1Controller:
    obj = MyTasks_1()  # Создал объект класса MyTasks_1

    # Добавить дело - Create
    @classmethod
    def add(cls, task):
        cls.obj.tasks = {
            "task": task,
            "completed": False
        }
        return True

    # Прокси-метод
    @classmethod
    def get(cls):
        return cls.obj.tasks

    # Отметить выполненной
    @classmethod
    def completed(cls, id):
        for dict in cls.get():
            if dict["id"] == id:
                dict["completed"] = True
                return dict
        return f"Задачи с ID {id} нет"

    # Удалить
    @classmethod
    def delete(cls, id):
        for i, dict in enumerate(cls.get()):
            if dict["id"] == id:
                del cls.get()[i]
                return True
        return f"Задачи с ID {id} нет"


if __name__ == "__main__":
    print(My_Tasks_1Controller.get())
    print(My_Tasks_1Controller.add("Приготовить ужин"))
    print(My_Tasks_1Controller.get())
    print(My_Tasks_1Controller.completed(2))
    print(My_Tasks_1Controller.delete(1))
    print(My_Tasks_1Controller.get())