with open("text_3.txt", "r", encoding='utf-8') as task_3:
    line_list = task_3.readlines()
    sum_salary = 0

    print("Employees with less than 20000 income: ")
    for el in line_list:
        line = el.split()
        sum_salary += float(line[1])
        if float(line[1]) < 20000:
            print(line[0])
print(f"Average income: {sum_salary / len(line_list)}")


with open("text_3.txt", "r", encoding='utf-8') as f:
    employees_dict = {line.split()[0]: float(line.split()[1])
                      for line in f}
    print(f"Average_salary = {round(sum(employees_dict.values()) / len(employees_dict), 3)}\n"
          f"Employees with salary less than 20k {[e[0] for e in employees_dict.items() if e[1] < 20000]}")

