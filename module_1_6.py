my_dict = {"Дима":20.1997, 'Саша':19.1995}
print(my_dict)
print(my_dict["Дима"])
print(my_dict.get("Паша"))
my_dict.update({"Паша":15.1989,"Даша":18.1998})
print(my_dict)
Дм = my_dict.pop("Дима")
print(Дм)
print(my_dict)
print(my_dict.items())
my_set={3,5,7,9,11,1,3,5,7,9,1} # работа с множеством
print(my_set)
print(my_set.add(13)) #Добавление 2 элементов в множество по одному
print(my_set.add(15)) #Добавление 2 элементов в множество по одному
print(my_set)
print(my_set.update([17,19,17,19])) #Добавление 2 элементов в множество списком
print(my_set)
my_set.discard(3)
print(my_set)