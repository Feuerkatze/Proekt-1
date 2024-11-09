def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a=4, c = [4,2,3])
print_params(a=8,b=6)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [4,"dog", False]
values_dict = {"a": 8, "b":"dog!", "c": False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2,"book"]


print_params(*values_list_2, 42)
