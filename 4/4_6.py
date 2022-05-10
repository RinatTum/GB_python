from itertools import cycle, count
for_cycle = []
for i in count(3):
    if i > 10:
        break
    else:
        print(i)
        for_cycle.append(i)
print(50 * '*')

n = 0
for el in cycle(for_cycle):
    if n > 10:
        break
    print(el)
    n += 1
