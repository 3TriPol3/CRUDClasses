from MyTasks.Task16.Models.Pet import Pet

class PetController:
    '''
     Класс для описания питомцев в витиринарной клинике
     Методы:
     добавить питомца,
     отметить прививку,
     питомцы владельца,
     найти по типу
     '''
    # CRUD
    obj = Pet() # Создал объект класса Pet
    @classmethod
    def add(cls, name, type, age, owner, vaccinated = False):
        cls.obj.pets = {
            "name": name,
            "type": type,
            "age": age,
            "owner": owner,
            "vaccinated": vaccinated
        }
        return True


    # Прокси метод
    @classmethod
    def get(cls):
        return cls.obj.pets

    # Поставить прививку
    @classmethod
    def vaccinated(cls, id):
        '''
        поменять значение ключа vaccinated на True, по id питомца
        в цикле перебрать список с питомцами
        :return:
        '''
        for dict in cls.get():
            if dict['id'] == id:
                dict['vaccinated'] = True
                return dict
            else:
                return f'Питомца с id {id} нет в базе данных'


if __name__ == "__main__":
    print(PetController.get())
    print(PetController.add('Машка', 'Кошка', 5, 'Мария'))
    print(PetController.get())
    print(PetController.vaccinated(2))