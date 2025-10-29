from MyTasks.Task4.Models.MyTasks_4 import MyTasks_4


class My_Tasks_4Controller:
    obj = MyTasks_4()  # Создал объект класса MyTasks_4

    # Добавить фильм - Create
    @classmethod
    def add(cls, title, year, rating, watched=False):
        cls.obj.movies = {
            "title": title,
            "year": year,
            "rating": rating,
            "watched": watched
        }
        return True

    # Прокси-метод
    @classmethod
    def get(cls):
        return cls.obj.movies

    # Поставить оценку
    @classmethod
    def set_rating(cls, id, new_rating):
        for dict in cls.get():
            if dict["id"] == id:
                dict["rating"] = new_rating
                return dict
        return f"Фильма с ID {id} нет"

    # Найти по названию
    @classmethod
    def find_by_title(cls, title):
        result = []
        for dict in cls.get():
            if title.lower() in dict["title"].lower():
                result.append(dict)
        return result if result else f"Фильм '{title}' не найден"

    # Показать непросмотренные
    @classmethod
    def show_unwatched(cls):
        result = [dict for dict in cls.get() if not dict["watched"]]
        return result if result else "Все фильмы просмотрены"

    # Удалить фильм
    @classmethod
    def delete(cls, id):
        for i, dict in enumerate(cls.get()):
            if dict["id"] == id:
                del cls.get()[i]
                return True
        return f"Фильма с ID {id} нет"


if __name__ == "__main__":
    print(My_Tasks_4Controller.get())
    print(My_Tasks_4Controller.add("Интерстеллар", 2014, 8.6))
    print(My_Tasks_4Controller.get())
    print(My_Tasks_4Controller.set_rating(2, 9.0))
    print(My_Tasks_4Controller.find_by_title("Крест"))
    print(My_Tasks_4Controller.show_unwatched())
    print(My_Tasks_4Controller.delete(1))
    print(My_Tasks_4Controller.get())