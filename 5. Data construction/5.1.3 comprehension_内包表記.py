# List Comprehension -------------------

# Original
squares = []
for x in range(5):
    squares.append(x ** 2)
print(squares)  # -> [0, 1, 4, 9, 16]

# map Function
squares = list(map(lambda x: x ** 2, range(5)))
print(squares)  # -> [0, 1, 4, 9, 16]

# List Comprehension
squares = [x ** 2 for x in range(5)]
print(squares)  # -> [0, 1, 4, 9, 16]

# List Comprehension 2 -------------------

# Original
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs)  # -> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# List Comprehension
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs)  # -> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# List Comprehension 3 -------------------

vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled
print([x * 2 for x in vec])  # -> [-8, -4, 0, 4, 8]

# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])  # -> [0, 2, 4]

# apply a function to all the elements
print([abs(x) for x in vec])  # -> [4, 2, 0, 2, 4]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# call a method on each element
print([weapon.strip() for weapon in freshfruit])  # -> ['banana', 'loganberry', 'passion fruit']

# create a list of 2-tuples like (number, square)
print([(x, x ** 2) for x in range(5)])  # -> [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flatten a list using a listcomp with two
print([num for elem in vec for num in elem])  # -> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 式部分の関数のネスト
from math import pi

print([str(round(pi, i)) for i in range(1, 4)])  # -> ['3.1', '3.14', '3.142']

# List Comprehension 4 -------------------

# 行と列を入れ替える

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# 下の全てのprint文の結果-> [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# Original
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

# One List Comprehension
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# Two List Comprehension
print([[row[i] for row in matrix] for i in range(4)])

# zip Function
print(list(zip(*matrix)))
