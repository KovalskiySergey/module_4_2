def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function() # Вызов функции отдельно, на уровне "test_function" приведет к ошибке,
    # при вызове на втором уровне приведет к пустой консоли
test_function()





