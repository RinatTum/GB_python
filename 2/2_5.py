my_list = [9, 8, 6, 4, 3, 3, 2]

number = ""

while number != "q":
    i = 0
    number = input("Enter number: \nTo quit enter - q\n")

    if number.isdigit():
        for n in my_list:
            if int(number) <= n:
                i += 1
            else:
                break
        my_list.insert(i, float(number))
    print(my_list)
