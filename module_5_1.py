class House:
    def __init__(self, name, number_of_floors ):
        self.name = name # имя
        self.number_of_floores = number_of_floors # кол-во этажей
    def go_to(self, new_floor): # номерэтажа(int)на который нужно приехать.
        n_f = int(new_floor)
        if n_f < 1 or self.number_of_floores < n_f:
            print('"Такого этажа не существует"', f'"{self.name}" - переезд  невозможен!')
        else:
            for i in range(1,n_f+1) :
                if i>=1 and i<= n_f:
                    print(i, f' этаж в "{self.name}"')



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
h3 = House('Котедж', 3)
h3.go_to(2)
