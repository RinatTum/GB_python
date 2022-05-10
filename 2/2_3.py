month = int(input("Введите месяц в формате от 1 до 12: "))
periods = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

if month in sum(periods.values(), []):
    for i in periods.items():
        if month in i[1]:
            print(i[0])
            break
