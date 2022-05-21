with open("task_2.txt", "r", encoding='utf-8') as task_2:
    count_word = 0
    line_list = task_2.readlines()
    print(f" Кол-во строк: {len(line_list)}")
    for i, el in enumerate(line_list, 1):
        count_word = len(el.split())
        print(f" Кол-во слов в {i} - й строке : {count_word}")


with open("task_2.txt", "r", encoding='utf-8') as task_2_comp:
    compr = [f"{count}. {line.strip()} - {len(line.split())} words"
             for count, line in enumerate(task_2_comp, 1)]
    print(*compr, f"Total lines - {len(compr)}", sep="\n")
