from MyTasks.Task8.Models.MyTasks_8 import MyTasks_8


class My_Tasks_8Controller:
    obj = MyTasks_8()

    @classmethod
    def add(cls, name, position, salary, department):
        cls.obj.employees = {
            "name": name,
            "position": position,
            "salary": salary,
            "department": department
        }

    @classmethod
    def get(cls):
        return cls.obj.employees

    @classmethod
    def increase_salary(cls, employee_id, amount):
        for emp in cls.get():
            if emp["id"] == employee_id:
                emp["salary"] += amount
                return True
        return False

    @classmethod
    def get_by_department(cls, department):
        result = []
        for emp in cls.get():
            if emp["department"].lower() == department.lower():
                result.append(emp)
        return result

    @classmethod
    def fire(cls, employee_id):
        for i, emp in enumerate(cls.get()):
            if emp["id"] == employee_id:
                del cls.get()[i]
                return True
        return False


if __name__ == "__main__":
    print("Все сотрудники:", My_Tasks_8Controller.get())
    My_Tasks_8Controller.add("Иван", "Тестировщик", 80000, "QA")
    print("После добавления:", My_Tasks_8Controller.get())
    My_Tasks_8Controller.increase_salary(1, 10000)
    print("После повышения зарплаты:", My_Tasks_8Controller.get())
    print("Сотрудники отдела IT:", My_Tasks_8Controller.get_by_department("IT"))
    My_Tasks_8Controller.fire(1)
    print("После увольнения:", My_Tasks_8Controller.get())