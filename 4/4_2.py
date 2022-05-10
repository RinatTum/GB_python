from random import randint

source_list = [randint(1, 500) for n in range(1, 50)]
print(source_list)
my_list = [source_list[i] for i in range(1, len(source_list)) if source_list[i] > source_list[i-1]]

print(my_list)
