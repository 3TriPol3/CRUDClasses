
class Pet:
    '''
    Класс для описания питомцев ветеринарной клиники


        '''
    def __init__(self):
        self.__list_pets =[
            {"id": 1, "name": "Барсик", "type": "кот", "age": 3, "owner": "Мария","vaccinated": False}
        ] # список питомцев
        self.id = 2

    @property
    def pets(self):
        '''
        Returns:
             список питомцев
        '''
        return self.__list_pets
    @pets.setter
    def pets(self,dict):
        dict['id'] = self.id
        self.pets.append(dict)
        self.id +=1


if __name__ == "__main__":
    pet = Pet()
    print(pet.pets)
    pet.pets = {"name": "Барсик", "type": "кот", "age": 3, "owner": "Мария","vaccinated": True}
    print(pet.pets)