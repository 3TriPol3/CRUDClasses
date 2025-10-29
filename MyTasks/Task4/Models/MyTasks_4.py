class MyTasks_4:
    def __init__(self):
        self.__list_movies = [
            {"id": 1, "title": "Крестный отец", "year": 1972, "rating": 9.2, "watched": True},
            {"id": 2, "title": "Матрица", "year": 1999, "rating": 8.7, "watched": False}
        ]
        self.id = 3  # Следующий ID для нового фильма

    @property
    def movies(self):
        return self.__list_movies

    @movies.setter
    def movies(self, dict):
        dict['id'] = self.id
        self.__list_movies.append(dict)
        self.id += 1


if __name__ == "__main__":
    movie = MyTasks_4()
    print(movie.movies)
    movie.movies = {"title": "Интерстеллар", "year": 2014, "rating": 8.6, "watched": False}
    print(movie.movies)