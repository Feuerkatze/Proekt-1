grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
stu = students.sort()
print(students)
Aaron= students[0],(sum(grades[0]))/(len(grades[0]))
print(Aaron)
Bilbo= students[1],(sum(grades[1]))/(len(grades[1]))
print(Bilbo)
Johnny= students[2],(sum(grades[2]))/(len(grades[2]))
print(Johnny)
Khendrik= students[3],(sum(grades[3]))/(len(grades[3]))
print(Khendrik)
Steve= students[4],(sum(grades[4]))/(len(grades[4]))
print(Steve)
Sred_bal= dict({Aaron,Bilbo,Johnny,Khendrik,Steve})
print("Средние баллы студентов :", Sred_bal)