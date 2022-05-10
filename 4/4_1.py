from sys import argv

def salary():
    try:
        name, hours, wage_rate, premium = argv
        print((float(hours) * float(wage_rate)) + float(premium))
        print(argv)
    except ValueError:
        print("Incorrect arguments. Please enter hours, wage rate and premium.")


salary()
