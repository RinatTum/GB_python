def divide(f_number, s_number):
    f_number = int(f_number)
    s_number = int(s_number)
    while s_number == 0:
        print("It is forbidden to divide by zero!")
        s_number = int(input("Enter number except zero: "))
    div = f_number / s_number
    return print(round(div, 4))


def divide_upgr(f_number, s_number):
    try:
        f_number, s_number = int(f_number), int(s_number)
        div = f_number / s_number
    except ZeroDivisionError:
        return print("It is forbidden to divide by zero!")
    return print(round(div, 4))


if __name__ == "__main__":
    print("First version")
    divide(input("Enter first number: "), input("Enter second number: "))

    print("Second version")
    divide_upgr(input("Enter first number: "), input("Enter second number: "))
