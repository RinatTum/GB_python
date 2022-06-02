class ZeroError(Exception):

    def __init__(self, text):
        self.text = text


a = input("Enter numerator: ")
b = input("Enter denominator: ")

try:
    if float(b) == 0:
        raise ZeroError("You entered negative number!")
    res = round(float(a) / float(b), 4)
except (ValueError, ZeroError) as err:
    print(err)
else:
    print(f"Result: {res}")

