from random import randint
source_list = [randint(1, 10) for el in range(1, 25)]
my_list = [i for i in source_list if source_list.count(i) == 1]
print(source_list)
print(my_list)
