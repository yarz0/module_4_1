def test_function():
    print("Я тестовая функция")
    def inner_function():
        a = "Я в области видимости функции test_function!"
        print(a)
        return a

      # Обращение к переменной внутри функции test_function
    return inner_function()


test_function()

print(a)  # Ошибка, переменная a не определена вне функции test_function
