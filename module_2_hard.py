import random
def lottery():
    Pole_kamn = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    num = random.choices(Pole_kamn)
    return num

num = lottery()
parol = []
parol1 = []
for i in range(1,10):
    for j in range(2,19):
        for k in num:
            raschet = (k % (i + j))
            if (raschet) == 0:
                parol.append(f'{i}+{j}') #  Наглядное решение - проще проверять- не нужная строка
                parol1.append(f'{i}{j}') # Основа
print("Случайное число:",k)
print("Решение:",*parol) # Наглядное решение - проще проверять- не нужная строка
print("Пароль:",*parol1)