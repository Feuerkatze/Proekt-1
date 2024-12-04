data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]#исходные данные задачи
def calculate_structure_sum(*data_structure):
    peremennai = data_structure
    summa = 0
    for i in peremennai:
        if isinstance(i, list):
            summa += calculate_structure_sum(*i)
        elif isinstance(i, tuple):
            summa += calculate_structure_sum(*i)
        elif isinstance(i, set):
            summa += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            no = i.items()
            summa += calculate_structure_sum(*no)
        elif isinstance(i, int):
            summa +=(i)
        elif isinstance(i, str):
            summa +=(len(i))
    return summa

result = calculate_structure_sum(*data_structure)
print(result)
