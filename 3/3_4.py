def my_pow(x, y):
    if x <= 0 or y >= 0:
        return print("Некорректный ввод: x - действительное положительное число, y - целое отрицательное число")
    return x ** y



def my_pow_2(x, y):
    d = x
    if x <= 0 or y >= 0:
        return print("Некорректный ввод: x - действительное положительное число, y - целое отрицательное число")
    for i in range(1, abs(y)):
        x *= d
    return round(1/x, 6)

print(my_pow(4, -2))
print(my_pow_2(4, -1))
