def my_func(arg1, arg2, arg3):
    """ Функция возвращает сумму наибольших двух аргументов """
    my_list = [arg1, arg2, arg3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return "All arguments must be numbers!"


print(my_func(30, 5, 20))
