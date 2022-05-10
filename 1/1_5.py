# 1 урок 5 задание

revenue = int(input("Your revenue: "))
expanse = int(input("Your expanse: "))

if revenue > expanse:
    print("You work with profit:)")
    profit = revenue - expanse
    profitability = round(profit / revenue, 2) * 100
    print(f"Profitability: {profitability}.")
    workers = int(input("Amount of workers: "))
    print(f"Profit for one worker: {round(profit / workers, 2)}")
else:
    print("You work with loss:(")
