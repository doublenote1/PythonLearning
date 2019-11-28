# === 階乗: ===
# math.factorial()

import math

print(math.factorial(5))
print(math.factorial(0))

"""非整数値、負の値はエラー ValueError になる"""

try:
    print(math.factorial(1.5))
except ValueError as e:
    print(e)
try:
    print(math.factorial(-1))
except ValueError as e:
    print(e)
print()

# === 順列の総数を算出 ===

"""
順列は、異なる n 個のものから r 個選んで一列に並べる場合の数
順列の総数は以下の式で求められる
p = n! / (n - r)!
"""

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

print(permutations_count(4, 2))
print(permutations_count(4, 4))
"""整数 int型を返すように、整数乗算を行う // 演算子を用いている"""
print()

# === リストから順列を生成、列挙: ===
# itertools.permutations()

"""
・総数だけでなく、リスト（配列）などから順列を生成して列挙することも可能
・第一引数にイテラブル（リストや集合 set型）、第二引数に選択する個数を渡すと、
  その順列のイテレータを返す
"""
import itertools

l = ['a', 'b', 'c', 'd']
p = itertools.permutations(l, 2)
print(type(p))
print()

"""すべて列挙するにはforループでまわせばOK"""
for v in itertools.permutations(l, 2):
    print(v)
# ('a', 'b')
# ('a', 'c')
# ('a', 'd')
# ('b', 'a')
# ('b', 'c')
# ('b', 'd')
# ('c', 'a')
# ('c', 'b')
# ('c', 'd')
# ('d', 'a')
# ('d', 'b')
# ('d', 'c')
print()

"""
・有限個のイテレータなので、list() でリスト型に変換することもできる
・リストの要素数を len() で取得すると、
  階乗から算出した順列の総数と一致していることが確認できる
"""
p_list = list(itertools.permutations(l, 2))
print(p_list)
print(len(p_list))
print()

"""第二引数を省略すると、すべての要素を選択する場合の順列が返される"""
for v in itertools.permutations(l):
    print(v)
# ('a', 'b', 'c', 'd')
# ('a', 'b', 'd', 'c')
# ('a', 'c', 'b', 'd')
# ('a', 'c', 'd', 'b')
# ('a', 'd', 'b', 'c')
# ('a', 'd', 'c', 'b')
# ('b', 'a', 'c', 'd')
# ('b', 'a', 'd', 'c')
# ('b', 'c', 'a', 'd')
# ('b', 'c', 'd', 'a')
# ('b', 'd', 'a', 'c')
# ('b', 'd', 'c', 'a')
# ('c', 'a', 'b', 'd')
# ('c', 'a', 'd', 'b')
# ('c', 'b', 'a', 'd')
# ('c', 'b', 'd', 'a')
# ('c', 'd', 'a', 'b')
# ('c', 'd', 'b', 'a')
# ('d', 'a', 'b', 'c')
# ('d', 'a', 'c', 'b')
# ('d', 'b', 'a', 'c')
# ('d', 'b', 'c', 'a')
# ('d', 'c', 'a', 'b')
# ('d', 'c', 'b', 'a')

print(len(list(itertools.permutations(l))))
print()

"""
・itertools.permutations() では、要素が値ではなく位置に基づいて一意的に扱われる
・値が重複していても特に考慮されない
"""
l = ['a', 'a']
for v in itertools.permutations(l, 2):
    print(v)
print()

"""
以下で説明する、
itertools.combinations()
itertools.combinations_with_replacement()
でも同様。
"""

# === 組み合わせの総数を算出 ===

"""
組み合わせは、異なる n 個のものから r 個選ぶ場合の数
順列のように順番を考慮しない
組み合わせの総数は以下の式で求められる
c = n! / (r! * (n - r)!)
階乗を返す関数 math.factorial() を使って以下のように算出できる
"""
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

print(combinations_count(4, 2))
"""整数int型を返すように、整数乗算を行う // 演算子を用いている"""
print()

# === リストから組み合わせを生成、列挙: ==
# itertools.combinations()

"""
・総数だけでなく、リスト（配列）などからすべての組み合わせを生成して列挙することも可能
・第一引数にイテラブル（リストや集合 set型）、
  第二引数に選択する個数を渡すと、その組み合わせのイテレータを返す
"""
l = ['a', 'b', 'c', 'd']
c = itertools.combinations(l, 2)
print(type(c))
for v in itertools.combinations(l, 2):
    print(v)
# ('a', 'b')
# ('a', 'c')
# ('a', 'd')
# ('b', 'c')
# ('b', 'd')
# ('c', 'd')
c_list = list(itertools.combinations(l, 2))
print(c_list)
print(len(c_list))
print()

# === 重複組み合わせの総数を算出 ===

"""
・重複組み合わせは、異なる n 個のものから重複を許して r 個選ぶ場合の数
・重複組み合わせの総数は、異なる n + r - 1 個のものから r 個選ぶ組み合わせの数に等しい
・したがって、上で定義した組み合わせの総数を算出する関数を使えばよい
"""
def combinations_with_replacement_count(n, r):
    return combinations_count(n + r - 1, r)

print(combinations_with_replacement_count(4, 2))
print()

# === リストから重複組み合わせを生成、列挙: ===
# itertools.combinations_with_replacement()

"""
・総数だけでなく、リスト（配列）などから
  すべての重複組み合わせを生成して列挙することも可能
・第一引数にイテラブル（リストや集合set型）、
  第二引数に選択する個数を渡すと、
  その重複組み合わせのイテレータを返す
"""
h = itertools.combinations_with_replacement(l, 2)
print(type(h))
for v in itertools.combinations_with_replacement(l, 2):
    print(v)
# ('a', 'a')
# ('a', 'b')
# ('a', 'c')
# ('a', 'd')
# ('b', 'b')
# ('b', 'c')
# ('b', 'd')
# ('c', 'c')
# ('c', 'd')
# ('d', 'd')

h_list = list(itertools.combinations_with_replacement(l, 2))
print(h_list)
print(len(h_list))
print()

# === 文字列からアナグラムを作成 ===

s = 'arc'
for v in itertools.permutations(s):
    print(v)
# ('a', 'r', 'c')
# ('a', 'c', 'r')
# ('r', 'a', 'c')
# ('r', 'c', 'a')
# ('c', 'a', 'r')
# ('c', 'r', 'a')

"""一文字ずつのタプルを文字列に結合してリスト化するには以下のようにすればよい"""
anagram_list = [''.join(v) for v in itertools.permutations(s)]
print(anagram_list)
print()
