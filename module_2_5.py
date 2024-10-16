def get_matrix(n, m , value):
    matrix = []
    for i in range(n):
        fum = []
        matrix.append(fum)
        for j in range(m):
            fum.append(value)
    print(matrix)

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
result4 = get_matrix(5, 3, 8)
print(result4)