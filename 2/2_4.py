user_str = input("Enter a sentence: ").split()

for n, i in enumerate(user_str, 1):
    print(f"{n}. {i:.10}")
