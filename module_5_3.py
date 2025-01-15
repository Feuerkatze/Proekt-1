class House:
    def __init__(self, name, number_of_floors ):
        self.name = name # имя
        self.number_of_floores = number_of_floors # кол-во этажей
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




h0 = House('Котедж', 6)
h0.go_to(2) # переезд
print(len(h0)) # количество всех этажей
print(h0) # Хорактеристики здания
print()
print()

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__