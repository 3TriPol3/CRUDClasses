class MyTasks_5:
    def __init__(self):
        self.__list_students = [
            {"id": 1, "name": "Анна", "age": 20, "grade": "A"},
            {"id": 2, "name": "Петр", "age": 19, "grade": "B"}
        ]
        self.id = 3  # Следующий ID для нового студента

    @property
    def students(self):
        return self.__list_students

    @students.setter
    def students(self, dict):
        dict['id'] = self.id
        self.__list_students.append(dict)
        self.id += 1


if __name__ == "__main__":
    student = MyTasks_5()
    print(student.students)
    student.students = {"name": "Иван", "age": 21, "grade": "C"}
    print(student.students)