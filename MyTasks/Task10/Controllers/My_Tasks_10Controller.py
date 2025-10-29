from MyTasks.Task10.Models.MyTasks_10 import MyTasks_10


class My_Tasks_10Controller:
    obj = MyTasks_10()

    @classmethod
    def add(cls, meal, food, calories, time):
        cls.obj.meals = {
            "meal": meal,
            "food": food,
            "calories": calories,
            "time": time
        }

    @classmethod
    def get(cls):
        return cls.obj.meals

    @classmethod
    def total_calories(cls):
        total = 0
        for meal in cls.get():
            total += meal["calories"]
        return total

    @classmethod
    def find_by_time(cls, time):
        result = []
        for meal in cls.get():
            if time in meal["time"]:
                result.append(meal)
        return result


if __name__ == "__main__":
    print("Все приемы пищи:", My_Tasks_10Controller.get())
    My_Tasks_10Controller.add("Ужин", "Рыба", 500, "19:00")
    print("После добавления:", My_Tasks_10Controller.get())
    print("Калории за день:", My_Tasks_10Controller.total_calories())
    print("Приемы пищи в 13:00:", My_Tasks_10Controller.find_by_time("13:00"))