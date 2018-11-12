# ****** 内包表記基本 ******

'''
・リスト内包表記
 [<仮引数に入れた要素を含んだ式> for <要素の仮引数> in <対象のイテラブル>]

・集合内包表記
リスト内包表記の [] が {} になる

・ジェネレータ内包表記
リスト内包表記の [] が () になる

・辞書内包表記
{<<キー: 値> の形に仮引数を含んだ式> for <要素の仮引数> in <対象のイテラブル>}
'''

vec = [-4, -2, 0, 2, 4]

# === リスト ===

# 要素を２倍
print([x * 2 for x in vec])

# if 文で要素をフィルタリング
print([x for x in vec if x >= 0])

# 関数を利用
print([abs(x) for x in vec])

# メソッドを利用
words = ['  aaa', '  bbb ', 'aaa bbb  ']
print([word.strip() for word in words])

# (連番, 連番を２乗した値)のタプルのリスト
print([(x, x ** 2) for x in range(5)])

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ネストした要素をならす
print([num for elem in vec for num in elem])

# 式部分の関数のネスト
from math import pi

print([str(round(pi, i)) for i in range(1, 6)])
print()

# === 集合 ===

lst = [1, 2, 3, 1, 2, 3]
print({x * 2 for x in lst})
print()

# === ジェネレータ ===

gen = (i ** 2 for i in range(5))
print(type(gen))
for i in gen:
    print(i, end=', ')
print()
print()

# === 辞書 ===

names = ['Alice', 'Bob', 'Charlie']
print({name: len(name) for name in names})
print()

# ****** 様々なリストの作り方 ******

# === リストの要素を加工 ===

# --- for 文 ---

squares = []
for x in range(5):
    squares.append(x ** 2)
print(squares)

# --- map 関数とラムダ式 ---

squares = list(map(lambda x: x ** 2, range(5)))
print(squares)

# --- リスト内包表記 ---

squares = [x ** 2 for x in range(5)]
print(squares)
print()

# === 複数のリストの組み合わせ ===

# --- for 文---

combs = []
list1, list2 = [1, 2, 3], [1, 2, 3]

for x in list1:
    for y in list2:
        if x != y:
            combs.append((x, y))
print(combs)

# --- for 文 itertools.product メソッド ---

from itertools import product as multi_iter

combs = []
for x, y in multi_iter(list1, list2):
    if x != y:
        combs.append((x, y))
print(combs)

# --- リスト内包表記 ---

combs = [(x, y) for x in list1 for y in list2 if x != y]
print(combs)
print()

# === 行と列を入れ替える ===

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# --- for 文 ２回 ---

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

# --- リスト内包表記 １回 ---

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# --- リスト内包表記 ２回 ---

print([[row[i] for row in matrix] for i in range(4)])

# --- zip 関数 ---
print(list(zip(*matrix)))
