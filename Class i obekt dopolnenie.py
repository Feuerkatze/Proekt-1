class House:
    houses_history = [] # названия зданий - история
    def __new__(cls, *args, **kwargs):
        global houses_history
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    def __init__(self, name, number_of_floors, **kwargs ):
        for key, vale in kwargs.items(): # - для возможности добавления при создании обьекта - здания дополнительные параметры
            setattr(self, key, vale)   # - аргументы для определённого  создаваемого обекта
        self.name = name # имя
        self.number_of_floores = number_of_floors # кол-во этажей
        #global houses_history  # для добавления названий в список houses_history для истории через инит при создании
        #self.houses_history.append(name) # для добавления названий в список houses_history для истории через инит при создании


    def go_to(self, new_floor): # номерэтажа на который нужно приехать.
        new_floor = int(new_floor)
        if new_floor < 1 or self.number_of_floores < new_floor:
            print('"Такого этажа не существует"', f'"{self.name}" - переезд  невозможен!')
        else:  # если возможно поднятие по этажам до необходимого
            for i in range(1,new_floor+1) :
                if i>=1 and i<= new_floor:
                    print(i, f' этаж в здании "{self.name}"')
    def __len__(self):  # количество всех этажей
        return self.number_of_floores
    def __str__(self): # Хорактеристики здания
        return  f'Название: {self.name}, кол-во этажей:{self.number_of_floores}.'
    def __eq__(self, other): # True, если количество этажей одинаковое self и other
        return self.number_of_floores == other.number_of_floores
    def __lt__(self,other): # (<)
        return self.number_of_floores < other.number_of_floores
    def __le__(self,other): # (<=)
        return self.number_of_floores <= other.number_of_floores
    def __gt__(self,other): # (>)
        return self.number_of_floores > other.number_of_floores
    def __ge__(self,other): # (>=)
        return self.number_of_floores >= other.number_of_floores
    def __ne__(self,other): # (!=)
        return self.number_of_floores != other.number_of_floores
    def __add__(self, value): # увеличивает к-во этажей на переданное значение value, возвращает объект self
        self.number_of_floores = self.number_of_floores + value
        return self
    def __iadd__(self,value):
        self.number_of_floores += value
        return self
    def __radd__(self,value):
        self.number_of_floores = value + self.number_of_floores
        return self
    def  __del__(self):# в котором будет выводиться строка:
        print(f'"{self.name}" снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10, material = 'kamen', grunt = 'scheben') # при создание обьекта добавил
print(House.houses_history) # аргументы параметры зданий материала строения и грунт - на что ставили
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2 # Удаление объектов
del h3

print(House.houses_history)
print(h1.material)
print(h1.grunt)