products = []

features = {"название": "", "цена": "", "количество": ""}
analytics = {"название": [], "цена": [], "количество": []}
num = 0
while True:
    if input("To quit enter q") == "q":
        break
    num += 1
    f_copy = features.copy()
    for f in features:
        pro = input(f'Enter feature: "{f}":')
        f_copy[f] = int(pro) if f in "цена количество" and pro.isdigit() else pro
        analytics[f].append(f_copy[f])
    products.append((num, f_copy))

    print(f"\nProducts: \n{products}")
    print(f"\nanalytics: \n {'*' * 30}")
    for key, value in analytics.items():
        print(f"{key:>30}: {value}")
    print("*" * 30)
