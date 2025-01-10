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



h1 = House('Котедж', 6)
h1.go_to(2) # переезд
print(len(h1)) # количество всех этажей
print(h1) # Хорактеристики здания
print()
print()

h2 = House('ЖК Эльбрус', 10)
h3 = House('ЖК Акация', 20)

print(h2)
print(h3)

print(len(h2))
print(len(h3))