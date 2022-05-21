import json

with open("text_7_json.json", "w", encoding="utf-8") as write_f, open('text_7.txt', encoding='utf-8') as f:
    profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f}
    file = [i for i in profit.values() if i > 0]
    result = [profit, {"average_profit": round(sum(file) / len(file))}]

    json.dump(result, write_f, ensure_ascii=False, indent=4)


