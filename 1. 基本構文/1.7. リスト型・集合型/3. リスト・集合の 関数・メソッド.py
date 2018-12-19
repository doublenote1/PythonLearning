# ****** 破壊的 ******

print('****** 破壊的 ******')
print()

# === 増加 ===

# --- 要素を追加 ---

# `list.append(object)`

lst = list(range(3))
print(lst)  # -> [0, 1, 2]
lst.append('appended')
print(lst)  # -> [0, 1, 2, 'appended']
lst.append([0, 1])
print(lst)  # -> [0, 1, 2, 'appended', [0, 1]]
print()

# `set.add(object)`

s = set(range(3))
print(s)  # -> {0, 1, 2}
s.add('added')
print(s)  # -> {0, 1, 2, 'added'}
s.add((0, 1))
print(s)  # -> {0, 1, 2, (0, 1), 'added'}
print()

# --- 要素を挿入 ---

# `list.insert(index, object)`

lst = list(range(3))
print(lst)  # -> [0, 1, 2]
lst.insert(0, 'inserted')
print(lst)  # -> ['inserted', 0, 1, 2]
lst.insert(-1, [0, 1])
print(lst)  # -> ['inserted', 0, 1, [0, 1], 2]
print()

# --- イテラブルを結合 ---

# `list.extend(iterable)`  ※処理速い
# `list += <iterable>`  ※処理遅い

lst = list(range(2))
print(lst)  # -> [0, 1]
lst.extend([2, 3])
print(lst)  # -> [0, 1, 2, 3]
lst.extend((4, 5))
print(lst)  # -> [0, 1, 2, 3, 4, 5]
lst.extend({6, 7})
print(lst)  # -> [0, 1, 2, 3, 4, 5, 6, 7]
lst.extend({8: 'a', 9: 'b'})
print(lst)  # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst.extend(range(10, 12))
print(lst)  # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
lst.extend('AB')
print(lst)  # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'A', 'B']
print()


# === 削除 ===

# --- 指定した値と同じの、最初の要素を削除 ---

# `list|set.remove(x)`
"存在しない値を指定するとエラー発生"

# リスト
lst = list(range(3))
print(lst)  # -> [0, 1, 2]
lst.remove(2)
print(lst)  # -> [0, 1]
try:
    lst.remove(2)
except ValueError as e:
    print(e)  # -> list.remove(x): x not in list
print()

# セット
s = set(range(3))
print(s)  # -> {0, 1, 2}
s.remove(2)
print(s)  # -> {0, 1}
try:
    s.remove(5)
except KeyError as e:
    print(type(e))  # -> <class 'KeyError'>
print()

# 指定した値と同じ要素を全て削除したい時
lst = [0, 1, 0, 2, 3, 0]
while lst.count(0):
    lst.remove(0)
print(lst)  # -> [1, 2, 3]
print()

# `set.discard(x)`
"存在しない値を指定すると何もしない"

s = set(range(3))
print(s)  # -> {0, 1, 2}
s.discard(2)
print(s)  # -> {0, 1}
s.discard(2)
print()

# --- (指定したインデックスの)要素を取得して削除 ---

# `list.pop([index])`

lst = list(range(5))
print(lst)  # -> [0, 1, 2, 3, 4]
print(lst.pop())  # -> 4
print(lst)  # -> [0, 1, 2, 3]
print(lst.pop(0))  # -> 0
print(lst)  # -> [1, 2, 3]
print(lst.pop(-1))  # -> 3
print(lst)  # -> [1, 2]
try:
    print(lst.pop(3))
except IndexError as e:
    print(e)  # -> pop index out of range
print()

# `set.pop()`
"set型からはインデックスを指定できない"

s = set(range(2))
print(s)  # -> {0, 1}
print(s.pop())  # -> 0
print(s)  # -> {1}
print(s.pop())  # -> 1
print(s)  # -> set()
try:
    print(s.pop())
except KeyError as e:
    print(e)  # -> 'pop from an empty set'
print()

# --- 全ての要素を削除 ---

# `list|set.clear()`

lst = list(range(3))
print(lst)  # -> [0, 1, 2]
lst.clear()
print(lst)  # -> []
print()


# === 並び替え ===

"イミュータブルは sort() 出来ない為、sorted() 関数を使う"

# --- 昇順・降順で並び替え ---

# `list.sort(key=None,reverse=False)`

# 昇順
lst = [5, 1, 9, 2, 4]
lst.sort()
print(lst)  # -> [1, 2, 4, 5, 9]

# 降順
lst = [5, 1, 9, 2, 4]
lst.sort(reverse=True)
print(lst)  # -> [9, 5, 4, 2, 1]

# key 指定
lst = ["Alice", "Bob", "Carl"]
lst.sort(key=len)
print(lst)  # -> ['Bob', 'Carl', 'Alice']
print()

# --- 逆順で並び替え ---

# `list.reverse()`

lst = [5, 1, 9, 2, 4]
lst.reverse()
print(lst)  # -> [4, 2, 9, 1, 5]
print()

# --- ランダムソート（シャッフル） ---

# 'random.shuffle(list[, random])'

import random

lst = list(range(5))
random.shuffle(lst)
print(lst)  # -> [2, 4, 1, 0, 3]
print()



# ****** 非破壊的 ******

print('****** 非破壊的 ******')
print()

lst = [3, 4, 1, 2, 3, 1, 6, 3, 3]
s = set(lst)
word = 'strawberry'

# === インデックスを取得 ===

# --- 引数の内容を持った要素の位置インデックスを取得 ---

# `sequence.index(x[,start[,end]])`

print(lst.index(1))  # -> 2
print(lst.index(1, 3))  # -> 5
print(word.index('raw'))  # -> 2
try:
    print(lst.index(1, 3, 4))
except ValueError as e:
    print(e)  # -> 1 is not in list
print()


# === 要素の数を取得 ===

# --- 全体の要素数 ---

# 'len(seq|collection)'

print(len(lst))  # -> 9
print(len(s))  # -> 5
print(len(word))  # -> 10
print()

# --- 引数の内容を持った要素の数、もしくは引数の文字列の存在数 ---

# `sequence.count(x)`
# `str.count(x[,start[,end]])`

print(lst.count(3))  # -> 4
print(word.count('r'))  # -> 3
print(word.count('berry'))  # -> 1
print(word.count('r', 3))  # -> 2
print(word.count('r', 8, 9))  # -> 1
print()

# === 要素全体の計算値を取得 ===

lst = [1, 2, 3, 4, 5]
lst_1_true = [0, 1, 0, 0, 0]
lst_all_false = [0, 0, 0, 0, 0]

# --- 要素全体の合計 ---

# `sum(iterable[,start])`

print(sum(lst))  # -> 15
print()

# --- 要素全体の平均値 ---

print(sum(lst) / len(lst))  # -> 3.0
print()

# --- リスト要素のいずれかが`True`であれば`True`を返す ---

# `any(iterable)`

print(any(lst))  # -> True
print(any(lst_1_true))  # -> True
print(any(lst_all_false))  # -> False
print()

# --- リスト要素すべてが`True`であれば`True`を返す ---

# `all(iterable)`

print(all(lst))  # -> True
print(all(lst_1_true))  # -> False
print(all(lst_all_false))  # -> False
print()


# === 特定の要素を取得 ===

lst = ['abcd', 'za', 'efg', 'abcd', 'za', 'efg']
lst_0 = []

s = set(lst)
s_0 = set()

word = 'strawberry'
word_0 = ''

# --- 最大・最小要素 ---

# `max|min(iterable,*[,key,default])`
# `max|min(arg1,arg2,*args[,key])`
"下記の例はすべて min にも当てはまる"

print(max(lst))  # -> za
print(max(lst, key=len))  # -> abcd
try:
    print(max(lst_0))
except ValueError as e:
    print(e)  # -> max() arg is an empty sequence
print(max(lst_0, default='NOTHING!!!'))  # -> NOTHING!!!
print(max('item000', 'item1', 'item01', key=len))  # -> item000
print()

# --- 最大値・最小値から順にn個の要素を取得 ---

# `import heapq`
# `heapq.nlargest(n, iterable, key=None)`
# `heapq.nsmallest(n, iterable, key=None)`

import heapq

print(heapq.nlargest(3, lst))  # -> ['za', 'za', 'efg']
print(heapq.nlargest(3, s))  # -> ['za', 'efg', 'abcd']
print(heapq.nlargest(3, word))  # -> ['y', 'w', 't']
print(heapq.nsmallest(3, lst))  # -> ['abcd', 'abcd', 'efg']
print(heapq.nsmallest(3, s))  # -> ['abcd', 'efg', 'za']
print(heapq.nsmallest(3, word))  # -> ['a', 'b', 'e']
print()

# --- ランダムに要素を一つ取得 ---

# `random.choice(seq)`

random_l = list(range(5))
random_w = 'ABCDE'

import random

print(random.choice(random_l))  # -> 1
print(random.choice(random_w))  # -> A
print()

# 乱数シードを固定
# `random.seed(a=None, version=2)`
random.seed(0)
print(random.choice(random_l))  # -> 3
print()

# --- ランダムに複数の要素を取得（重複なし） ---

# `random.sample(population, k)`

print(random.sample(random_l, 3))  # -> [3, 4, 2]
print(random.sample(random_w, 3))  # -> ['E', 'A', 'B']
print()

# --- ランダムに複数の要素を取得（重複あり） ---

# `random.choices(population,weights=None,*,cum_weights=None,k=1)`

'''
引数`weights`でそれぞれの要素が選ばれる重み（確率）を指定できる
`weights`に指定するリストの要素の型は`int`でも`float`でもOK
0にするとその要素は選ばれない。
'''

print(random.choices(random_l))  # -> [0]
print(random.choices(random_l, k=3))  # -> [3, 0, 3]
print(random.choices(random_l, k=10))  # -> [3, 3, 4, 4, 3, 2, 0, 4, 0, 1]
print(random.choices(random_l, k=3, weights=[1, 1, 1, 10, 1]))  # -> [3, 0, 3]
print(random.choices(random_l, k=3, weights=[1, 1, 0, 0, 0]))  # -> [1, 0, 1]

'''
引数`cum_weights`に累積的な重みとして指定することもできる
以下のサンプルコードの`cum_weights`は上の一つ目の`weights`と等価
'''

print(random.choices(random_l, k=3, cum_weights=[1, 2, 3, 13, 14]))  # -> [3, 1, 2]
print()

# === 並べ替え ===

# --- 昇順・降順で並び替えしたリストを取得 ---

# `sorted(iterable,*,key=None,reverse=False)`

# 昇順
print(sorted(lst))  # -> [1, 2, 3, 4, 5]
print(sorted(word))  # -> ['a', 'b', 'e', 'r', 'r', 'r', 's', 't', 'w', 'y']

# 降順
print(sorted(lst, reverse=True))  # -> [5, 4, 3, 2, 1]
print(sorted(word, reverse=True))  # -> ['y', 'w', 't', 's', 'r', 'r', 'r', 'e', 'b', 'a']

# --- 要素を逆順に取り出すイテレータを取得 ---

# `reversed(seq)`

print(reversed(lst))  # -> <list_reverseiterator object at 0x0000000003917A90>
print(reversed(word))  # -> <reversed object at 0x0000000003917A90>
