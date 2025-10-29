from MyTasks.Task9.Models.MyTasks_9 import MyTasks_9


class My_Tasks_9Controller:
    obj = MyTasks_9()

    @classmethod
    def add(cls, title, genre, platform, completed):
        cls.obj.games = {
            "title": title,
            "genre": genre,
            "platform": platform,
            "completed": completed
        }

    @classmethod
    def get(cls):
        return cls.obj.games

    @classmethod
    def find_by_genre(cls, genre):
        result = []
        for game in cls.get():
            if genre.lower() in game["genre"].lower():
                result.append(game)
        return result

    @classmethod
    def mark_completed(cls, game_id):
        for game in cls.get():
            if game["id"] == game_id:
                game["completed"] = not game["completed"]
                return True
        return False

    @classmethod
    def filter_by_platform(cls, platform):
        result = []
        for game in cls.get():
            if platform.lower() in game["platform"].lower():
                result.append(game)
        return result


if __name__ == "__main__":
    print("Все игры:", My_Tasks_9Controller.get())
    My_Tasks_9Controller.add("Cyberpunk 2077", "RPG", "PS5", False)
    print("После добавления:", My_Tasks_9Controller.get())
    My_Tasks_9Controller.mark_completed(1)
    print("После отметки как пройденной:", My_Tasks_9Controller.get())
    print("Игры жанра RPG:", My_Tasks_9Controller.find_by_genre("RPG"))
    print("Игры для платформы PC:", My_Tasks_9Controller.filter_by_platform("PC"))