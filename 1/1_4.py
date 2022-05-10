# 1 урок 4 задание

number = abs(int(input("Enter number: ")))
max_digit = 0
digit = 0

while number:
    digit = number % 10

    if digit >= max_digit:
        max_digit = digit
    number = number // 10

print(max_digit)
