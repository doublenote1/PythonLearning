# === 直積（デカルト積）とは ===

"""
直積（デカルト積）は、複数の集合から要素を一つずつ取り出した組み合わせの集合
例えば2つのリストがあったとき、すべてのペアの組み合わせのリストが直積
"""

# === itertools.product() の基本的な使い方 ===

"""
引数に2つのリストを指定すると itertools.product型のオブジェクトが返る
itertools.product型はジェネレータなので、それをそのまま print() しても中身は出力されない。
"""

import itertools
from pprint import pprint

l1 = ['a', 'b', 'c']
l2 = ['X', 'Y', 'Z']

p = itertools.product(l1, l2)
print(p)  # -> <itertools.product object at 0x1026edd80>
print(type(p))  # -> <class 'itertools.product'>

for v in p:
    print(v)
# ('a', 'X')
# ('a', 'Y')
# ('a', 'Z')
# ('b', 'X')
# ('b', 'Y')
# ('b', 'Z')
# ('c', 'X')
# ('c', 'Y')
# ('c', 'Z')

"""タプルではなくそれぞれの要素を別々に取得することも可能"""
for v1, v2 in itertools.product(l1, l2):
    print(v1, v2)
# a X
# a Y
# a Z
# b X
# b Y
# b Z
# c X
# c Y
# c Z

"""
以下のような各リストをネストしたforループ（多重ループ）と
同じ結果が得られていることが分かる
"""
for v1 in l1:
    for v2 in l2:
        print(v1, v2)
# a X
# a Y
# a Z
# b X
# b Y
# b Z
# c X
# c Y
# c Z

"""
list() でリスト化することも可能
タプルを要素とするリストとなる
"""
l_p = list(itertools.product(l1, l2))
pprint(l_p)
# [('a', 'X'),
#  ('a', 'Y'),
#  ('a', 'Z'),
#  ('b', 'X'),
#  ('b', 'Y'),
#  ('b', 'Z'),
#  ('c', 'X'),
#  ('c', 'Y'),
#  ('c', 'Z')]

print(type(l_p))  # -> <class 'list'>
print(type(l_p[0]))  # -> <class 'tuple'>

"""
・引数はイテラブルオブジェクトであれば、
  タプル でも リスト でも rangeオブジェクト でもなんでもいい
・引数にはイテラブルオブジェクトを2個以上指定できる。
"""

t = ('one', 'two')
d = {'key1': 'value1', 'key2': 'value2'}
r = range(2)

pprint(list(itertools.product(t, d, r)))
# [('one', 'key1', 0),
#  ('one', 'key1', 1),
#  ('one', 'key2', 0),
#  ('one', 'key2', 1),
#  ('two', 'key1', 0),
#  ('two', 'key1', 1),
#  ('two', 'key2', 0),
#  ('two', 'key2', 1)]

# === 同じリストを繰り返し使用: 引数repeat ===

"""
キーワード引数 repeat に繰り返しの回数を指定すると、
イテラブルオブジェクトを繰り返し使用して直積を生成する
"""
l1 = ['a', 'b']
pprint(list(itertools.product(l1, repeat=3)))
"""引数は (l1, l1, l1) となる"""
# [('a', 'a', 'a'),
#  ('a', 'a', 'b'),
#  ('a', 'b', 'a'),
#  ('a', 'b', 'b'),
#  ('b', 'a', 'a'),
#  ('b', 'a', 'b'),
#  ('b', 'b', 'a'),
#  ('b', 'b', 'b')]

"""イテラブルオブジェクトを複数指定した場合は次のようになる"""
l1 = ['a', 'b']
l2 = ['X', 'Y']
pprint(list(itertools.product(l1, l2, repeat=2)))
"""引数は (l1, l2, l1, l2) となる"""
# [('a', 'X', 'a', 'X'),
#  ('a', 'X', 'a', 'Y'),
#  ('a', 'X', 'b', 'X'),
#  ('a', 'X', 'b', 'Y'),
#  ('a', 'Y', 'a', 'X'),
#  ('a', 'Y', 'a', 'Y'),
#  ('a', 'Y', 'b', 'X'),
#  ('a', 'Y', 'b', 'Y'),
#  ('b', 'X', 'a', 'X'),
#  ('b', 'X', 'a', 'Y'),
#  ('b', 'X', 'b', 'X'),
#  ('b', 'X', 'b', 'Y'),
#  ('b', 'Y', 'a', 'X'),
#  ('b', 'Y', 'a', 'Y'),
#  ('b', 'Y', 'b', 'X'),
#  ('b', 'Y', 'b', 'Y')]
