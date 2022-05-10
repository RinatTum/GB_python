#

a = int(input("First day result: "))
b = int(input("Needed result: "))
day = 1
while a <= b:
    a *= 1.1
    day += 1
print(f'On {day}-th day sportsman achieve result — no less than {b} km.')