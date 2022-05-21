with open('task_1.txt', 'w', encoding='utf_8') as task1:
    while True:
        text = input("Enter the text: ")
        if not text:
            break
        task1.write(f"{text}\n")
