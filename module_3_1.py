calls = 0
def count_calls():
    global calls
    calls+=1


def string_info(string):
    print(len(string), string.upper(),string.lower())
    count_calls()




def is_contains(string1, list_to_search):
    for i in list_to_search:
        if (i.lower()) != string1.lower():
            print(False)
            break
        elif (i.lower()) == string1.lower():
            print(i)
            print(True)
            break

    count_calls()


string_info("лень")
string_info("лень")
string_info("не лень")

is_contains("Лень",["лень", "гнев", "жадность"])
string_info("Активность")
is_contains("голод",["лень", "гнев", "жадность"])

print("Функций вызванно :", calls, "раз")