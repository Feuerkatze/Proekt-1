numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  # Список простые
not_primes = [] # список составные
for i in numbers:
    for j in numbers[1:-1]:
        num = int(f'{i % j}')
        num1 = int(f'{i % 3}')
        if i==2:
            primes.append(i)
            print(i, ("простое число")) # не обязательная строка кода
            break
        elif i == 1:
            break
        elif j == i:
            break
        elif  num == 0 or num1 ==0:
            not_primes.append(i)
            print(i,("составное число")) # не обязательная строка кода
            break
        elif num != 0 :
            primes.append(i)
            print(i, ("простое число"))# не обязательная строка кода
            break
print("primes    ", primes)
print("not_primes",not_primes)





