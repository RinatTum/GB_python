# 1 урок 2 задание

number = int(input("Enter number in seconds: "))

h = number // 3600
m = number % 3600 // 60
s = number % 60

print(f"{h:02d}:{m:02d}:{s:02d}")