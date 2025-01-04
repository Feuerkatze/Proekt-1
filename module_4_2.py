def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

muni = inner_function() # выдаст ошибку - функция inner_function в пространстве локальном
print(muni)
