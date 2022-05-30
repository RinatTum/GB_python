class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '+' * (self.nums % rows)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print("Sum is:")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("Sub is:")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "Sub is impossible. Units of first Cell is less then second's)"

    def __mul__(self, other):
        print("Mul is:")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Truediv is:")
        return Cell(self.nums // other.nums)


cell_1 = Cell(20)
cell_2 = Cell(15)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))
