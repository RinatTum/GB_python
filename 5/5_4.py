from googletrans import Translator

translator = Translator()
with open("text_4.txt", "r", encoding='utf-8') as f:
    with open("new_text_04.txt", 'w', encoding='utf-8') as new_text_04:
        line_list = f.readlines()
        for el in line_list:
            line = el.split()
            word = translator.translate(line[0], dest='ru')
            new_text_04.write(word.text + ' ' + ' '.join(line[1:]) + '\n')
