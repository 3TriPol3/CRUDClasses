class MyTasks_6:
    def __init__(self):
        self.__list_expenses = [
            {"id": 1, "amount": 1500, "category": "Еда", "date": "2024-01-20", "description": "Продукты"},
            {"id": 2, "amount": 300, "category": "Транспорт", "date": "2024-01-21", "description": "Автобус"}
        ]
        self.id = 3  # Следующий ID для нового расхода

    @property
    def expenses(self):
        return self.__list_expenses

    @expenses.setter
    def expenses(self, dict):
        dict['id'] = self.id
        self.__list_expenses.append(dict)
        self.id += 1


if __name__ == "__main__":
    expense = MyTasks_6()
    print("Исходные расходы:", expense.expenses)
    expense.expenses = {"amount": 200, "category": "Развлечения", "date": "2024-01-22", "description": "Кино"}
    print("Добавлен новый расход:", expense.expenses)