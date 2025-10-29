from MyTasks.Task7.Models.MyTasks_7 import MyTasks_7


class My_Tasks_7Controller:
    obj = MyTasks_7()

    @classmethod
    def add(cls, title, author, year, read):
        cls.obj.books = {
            "title": title,
            "author": author,
            "year": year,
            "read": read
        }

    @classmethod
    def get(cls):
        return cls.obj.books

    @classmethod
    def mark_read(cls, book_id):
        for book in cls.get():
            if book["id"] == book_id:
                book["read"] = not book["read"]
                return True
        return False

    @classmethod
    def find_by_author(cls, author):
        result = []
        for book in cls.get():
            if author.lower() in book["author"].lower():
                result.append(book)
        return result

    @classmethod
    def filter_by_year(cls, year):
        result = []
        for book in cls.get():
            if book["year"] == year:
                result.append(book)
        return result


if __name__ == "__main__":
    print("Все книги:", My_Tasks_7Controller.get())
    My_Tasks_7Controller.add("Над пропастью во ржи", "Сэлинджер", 1951, False)
    print("После добавления:", My_Tasks_7Controller.get())
    My_Tasks_7Controller.mark_read(1)
    print("После отметки как прочитанной:", My_Tasks_7Controller.get())
    print("Книги автора 'Оруэлл':", My_Tasks_7Controller.find_by_author("Оруэлл"))
    print("Книги года 1967:", My_Tasks_7Controller.filter_by_year(1967))