class MyTasks_7:
    def __init__(self):
        self.__library = [
            {"id": 1, "title": "1984", "author": "Оруэлл", "year": 1949, "read": False},
            {"id": 2, "title": "Мастер и Маргарита", "author": "Булгаков", "year": 1967, "read": True}
        ]
        self.id = 3  # Следующий ID для новой книги

    @property
    def books(self):
        return self.__library

    @books.setter
    def books(self, dict):
        dict['id'] = self.id
        self.__library.append(dict)
        self.id += 1


if __name__ == "__main__":
    library = MyTasks_7()
    print("Исходные книги:", library.books)
    library.books = {"title": "Над пропастью во ржи", "author": "Сэлинджер", "year": 1951, "read": False}
    print("Добавлена новая книга:", library.books)