from MyTasks.Task6.Models.MyTasks_6 import MyTasks_6


class My_Tasks_6Controller:
    obj = MyTasks_6()

    @classmethod
    def add(cls, amount, category, date, description):
        cls.obj.expenses = {
            "amount": amount,
            "category": category,
            "date": date,
            "description": description
        }

    @classmethod
    def get(cls):
        return cls.obj.expenses

    @classmethod
    def total_by_category(cls, category):
        total = 0
        for expense in cls.get():
            if expense["category"].lower() == category.lower():
                total += expense["amount"]
        return total

    @classmethod
    def expenses_in_period(cls, start_date, end_date):
        result = []
        for expense in cls.get():
            if start_date <= expense["date"] <= end_date:
                result.append(expense)
        return result


if __name__ == "__main__":
    print("Все расходы:", My_Tasks_6Controller.get())
    My_Tasks_6Controller.add(200, "Развлечения", "2024-01-22", "Кино")
    print("После добавления:", My_Tasks_6Controller.get())
    print("Сумма по 'Еда':", My_Tasks_6Controller.total_by_category("Еда"))
    print("Расходы с 2024-01-20 по 2024-01-21:", My_Tasks_6Controller.expenses_in_period("2024-01-20", "2024-01-21"))