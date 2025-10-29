from MyTasks.Task16.Models.Pet import Pet


class PetController:
    '''
    Класс для управления моделью Pet
    методы:
     добавить питомца,
     поставить прививку,
     вывести список 'питомцы владельца',
     найти по типу
    '''
    # CRUD
    obj = Pet()  # создал объект класса Pet

    @classmethod
    def add(cls, name, type, age, owner, vaccinated=False):
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

    # поставить прививку,
    @classmethod
    def vaccinated(cls, id):
        '''
        поменять значения ключа vaccinated на True, по ИД питомца
         в цикле перебрать спиок с питомцами
        :return:
        '''
        for dict in cls.get():
            if dict['id'] == id:
                dict['vaccinated'] = True
                return dict


    # вывести список 'питомцы владельца',
    @classmethod
    def list_owner(cls,owner):
        list = []
        for dict in cls.get():
            if dict['owner'] == owner:
                list.append(dict['name'])
        return list
    # найти по типу
    @classmethod
    def type_pet(cls,type):
        result = f'Нет - {type}'
        for dict in cls.get():
            if dict['type'] == type:
                result = f'Есть {type}'
        return result

if __name__ == "__main__":
    print(PetController.get())
    print(PetController.add('Машка', "Кошка", 5, 'Мария'))
    print(PetController.get())
    print(PetController.vaccinated(3))