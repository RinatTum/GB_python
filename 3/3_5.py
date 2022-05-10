def sum_num():
    s = 0
    while True:
        my_list = input("Enter number, input 'q' to exit: ").split()
        for num in my_list:
            if num.lower() == 'q':
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print("Value error")
        print(f'Sum = {s}')

print(sum_num())
