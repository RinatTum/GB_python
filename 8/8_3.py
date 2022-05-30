class Error:
    def __init__(self):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Enter number: '))
                self.my_list.append(val)
                print(f'List - {self.my_list} \n ')
            except:
                print(f"Incorrect typing")
                y_or_n = input(f'Try again? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'You quit'
                else:
                    return f'You quit'


try_except = Error()
print(try_except.my_input())
