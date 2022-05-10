

my_list = [16, 32, 'word', True, [2, 69], {1: 'a', 2: 'b'}, None,  (1, 2, 3)]
for el in my_list:
    print(f' The type of the element {el} = {type(el)}')


for i, item in enumerate(my_list, 1):
    print(f"{i} {item} - {type(item)}")
