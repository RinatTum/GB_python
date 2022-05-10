# 1 урок 1 задание.

name = input("Enter your name:")

operation = input("Enter operation (+, -): ")

a = int(input("First number: "))
b = int(input("Second number: "))

if operation == "+":
    answer = a + b
    print(f"Hi {name}!, answer to your operation: {answer}.")
elif operation == "-":
    answer = a - b
    print(f"Hi {name}!, answer to your operation: {answer}.")
else:
    print("Your operation is wrong. Enter right operator (+, -)")
