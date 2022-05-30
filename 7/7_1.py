from itertools import zip_longest

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.matrix]))
    def __add__(self, other):
        return Matrix([map(sum, zip_longest(*t, fillvalue=0)) for t in zip_longest(self.matrix, other.matrix, fillvalue=[])])

list_1 = [[1, 2, 3], [4, 5, 6]]

list_2 = [[1, 2, 3], [4, 5, 6], [7, 8]]

matr_1 = Matrix(list_1)

matr_2 = Matrix(list_2)

print(matr_1)
print('*' * 20)
print(matr_1 + matr_2)
