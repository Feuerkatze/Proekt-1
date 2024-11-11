def get_multiplied_digits(number = 402):
    str_number = str(number)
    first= int(str_number[0])
    if 1< int(len(str_number)):
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


get= get_multiplied_digits(40203)
print(get)
get1= get_multiplied_digits(70803)
print(get1)
get2= get_multiplied_digits()
print(get2)