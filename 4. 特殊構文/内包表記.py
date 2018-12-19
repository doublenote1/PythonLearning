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

# === リスト ===

vec = [-3, -2, -1, 0, 1, 2, 3]

# 各要素へ処理
print([x * 2 for x in vec])

# 関数を利用
print([abs(x) for x in vec])

# メソッドを利用
words = ['  aaa', '  bbb ', 'aaa bbb  ']
print([word.strip() for word in words])

# (連番, 連番を２乗した値)のタプルのリスト
print([(x, x ** 2) for x in range(5)])

nest = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# ネストした要素をならす
print([num for elem in nest for num in elem])

# 式部分の関数のネスト
from math import pi

print([str(round(pi, i)) for i in range(1, 6)])
print()

# --- if文で要素をフィルタリング ---

# 条件式
vec = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
print([x for x in vec if x >= 0])
print([x for x in vec if not x >= 0])
print([x for x in vec if (x > 0) and (x % 2 == 0)])
print()

# 特定の文字列を含む
str_l = ['oneXXXaaa', 'twoXXXbbb', 'three999aaa', '000111222']
print([s for s in str_l if 'XXX' in s])
print([s for s in str_l if 'XXX' not in s])
print()

# 特定の文字列で始まる
print([s for s in str_l if s.startswith('t')])
print([s for s in str_l if not s.startswith('t')])
print()

# 特定の文字列で終わる
print([s for s in str_l if s.endswith('aaa')])
print([s for s in str_l if not s.endswith('aaa')])
print()

# 三項演算子で条件を満たす要素に対して処理
print(['ZZZ' if 'XXX' in x else x for x in str_l])
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
