class Pet:
    
    def __init__(self, name, animal_type, age):
        self.__name = name;
        self.__animal_type = animal_type
        self.__age = age
    
    def set_name(self, name):
        self.__name = name
    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    
    def set_age(self, age):
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age

    sound = ''
    
    def sound(self, sound):
        if self.__animal_type == 'Dog':
            sound = 'hav hav'
        elif self.__animal_type == 'Cat':
            sound = 'miyaaaav'
        elif self.__animal_type == 'Bird':
            sound = 'cik cik cik'
        else:
            print('Sorry, there is no sound for your pet that I know')
            sound = 'nothing'
        return '{} sounds {}'.format(self.__name, sound)
