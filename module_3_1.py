calls = 0
def count_calls():
    global calls
    calls+=1


def string_info(string):
    count_calls()
    return(len(string), string.upper(),string.lower())


def is_contains(string1, list_to_search):
    count_calls()
    for i in list_to_search:
        if (i.lower()) != string1.lower():
            return(False)
        elif (i.lower()) == string1.lower():
            return(True)


print(string_info("лень"))
print(string_info("лень"))
print(string_info("не лень"))
print(is_contains("Лень",["лень", "гнев", "жадность"]))
print(string_info("Активность"))
print(is_contains("голод",["лень", "гнев", "жадность"]))

print("Функций вызванно :", calls, "раз")
