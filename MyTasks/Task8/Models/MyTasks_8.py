class MyTasks_8:
    def __init__(self):
        self.__employees = [
            {"id": 1, "name": "Мария", "position": "Разработчик", "salary": 100000, "department": "IT"}
        ]
        self.id = 2  # Следующий ID для нового сотрудника

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, dict):
        dict['id'] = self.id
        self.__employees.append(dict)
        self.id += 1


if __name__ == "__main__":
    emp = MyTasks_8()
    print("Исходные сотрудники:", emp.employees)
    emp.employees = {"name": "Иван", "position": "Тестировщик", "salary": 80000, "department": "QA"}
    print("Добавлен новый сотрудник:", emp.employees)