# ****** 破壊的 ******

# === 追加・挿入・結合 ===

# 要素の追加:
# list.append(object)

lst = list(range(3))
print(lst)
lst.append('appended')
print(lst)
lst.append([0, 1])
print(lst)
print()

# 要素の挿入:
# list.insert(index, object)

lst = list(range(3))
print(lst)
lst.insert(0, 'inserted')
print(lst)
lst.insert(-1, [0, 1])
print(lst)
print()

# リストの結合:
# list.extend(iterable)

lst = list(range(2))
lst.extend(['A', 'B'])
print(lst)
lst.extend(('X', 'Y'))
print(lst)
lst.extend('あい')
print(lst)
lst += ['①', '②']
print(lst)
print()

# === 削除 ===

# 指定した値と同じの、最初の要素を削除:
# list.remove(x)

lst = list(range(3))
print(lst)
lst.remove(0)
print(lst)
lst.remove(2)
print(lst)
try:
    print(lst.remove(0))
except ValueError as e:
    print(e)
print()

# 指定したインデックスの要素を削除して取得:
# list.pop([index])

lst = list(range(5))
print(lst)
print(lst.pop())
print(lst)
print(lst.pop(0))
print(lst)
print(lst.pop(-1))
print(lst)
try:
    print(lst.pop(3))
except IndexError as e:
    print(e)
print()

# 全ての要素を削除:
# list.clear()

lst.clear()
print(lst)
print()

# === 並び替え ===

'''
イミュータブルは sort() 出来ない為、
sorted() 関数を使う
'''

# 昇順・降順で並び替え:
# list.sort(key=None,reverse=False)

# 昇順
lst = [5, 1, 9, 2, 4]
lst.sort()
print(lst)
# 降順
lst = [5, 1, 9, 2, 4]
lst.sort(reverse=True)
print(lst)
# key 指定
lst = ["Alice", "Bob", "Carl"]
lst.sort(key=len)
print(lst)
print()

# 逆順で並び替え:
# list.reverse()

lst = [5, 1, 9, 2, 4]
lst.reverse()
print(lst)
print()

# ランダムソート（シャッフル）:
# random.shuffle(list[, random])

import random

lst = list(range(5))
random.shuffle(lst)
print(lst)
print()

# ****** 非破壊的 ******

# === 情報取得 ===

# --- インデックス ---

lst = [3, 4, 1, 2, 3, 1, 6, 3, 3]
word = 'strawberry'

# 引数の内容を持った要素の位置インデックスを取得:
# sequence.index(x[,start[,end]])

print(lst.index(1))
print(lst.index(1, 3))
print(word.index('raw'))
try:
    print(lst.index(1, 3, 4))
except ValueError as e:
    print(e)
print()

# --- 要素の数 ---

lst = [3, 4, 1, 2, 3, 1, 6, 3, 3]
word = 'strawberry'

# 全体の要素数:
# len(seq|collection)

print(len(lst))
print(len(word))
print()

# 引数の内容を持った要素の数、もしくは引数の文字列の存在数:
# sequence.count(x)
# str.count(x[,start[,end]])

print(lst.count(3))
print(word.count('r'))
print(word.count('r', 3))
print(word.count('r', 8, 9))
print()

# --- 特定要素 ---

lst = ['abcd', 'za', 'efg']
lst_0 = []
word = 'strawberry'
word_0 = ''

# 最大・最小要素:
# max|min(iterable,*[,key,default])
# max|min(arg1,arg2,*args[,key])

print(max(lst))
print(max(lst, key=len))
print(max(lst_0, default='NOTHING!!!'))
print(max('z','xy','abc', key=len))
print(max(word))
print()
print(min(lst))
print(min(lst, key=len))
print(min(word))
print()

# 最大値・最小値から順にn個の要素を取得:
# import heapq
# heapq.nlargest(n, iterable, key=None)
# heapq.nsmallest(n, iterable, key=None)

import heapq

print(heapq.nlargest(3, lst))
print(heapq.nlargest(3, word))
print(heapq.nsmallest(3, lst))
print(heapq.nsmallest(3, word))
print()

# --- ランダムに要素を選択 ---

random_l = list(range(5))
random_w = 'ABCDE'

import random

# ランダムに要素を一つ選択:
# random.choice(seq)

print(random.choice(random_l))
print(random.choice(random_w))
print()

# ランダムに複数の要素を選択（重複なし）:
# random.sample(population, k)

print(random.sample(random_l, 3))
print(random.sample(random_w, 3))
print()

# ランダムに複数の要素を選択（重複あり）:
# random.choices(population,weights=None,*,cum_weights=None,k=1)

'''
引数weightsでそれぞれの要素が選ばれる重み（確率）を指定できる
weightsに指定するリストの要素の型はintでもfloatでもOK
0にするとその要素は選ばれない。
'''

print(random.choices(random_l))
print(random.choices(random_l, k=3))
print(random.choices(random_l, k=10))
print(random.choices(random_l, k=3, weights=[1, 1, 1, 10, 1]))
print(random.choices(random_l, k=3, weights=[1, 1, 0, 0, 0]))

'''
引数cum_weightsに累積的な重みとして指定することもできる
以下のサンプルコードのcum_weightsは上の一つ目の weights と等価
'''
print(random.choices(random_l, k=3, cum_weights=[1, 2, 3, 13, 14]))
print()

# 乱数シードを固定:
# random.seed(a=None, version=2)

random.seed(0)
print(random.choice(random_l))
print()

# --- 計算値 ---

lst = [1, 2, 3, 4, 5]

# 要素全体の合計:
# sum(iterable[,start])

print(sum(lst))

# 要素全体の平均値

print(sum(lst) / len(lst))
print()

# === 並べ替え ===

# --- 昇順・降順で並び替えしたリストを取得: ---
# sorted(iterable,*,key=None,reverse=False)

# 昇順

print(sorted(lst))
print(sorted(word))

# 降順

print(sorted(lst, reverse=True))
print(sorted(word, reverse=True))

# --- 要素を逆順に取り出すイテレータを取得: ---
# reversed(seq)

print(reversed(lst))
print(reversed(word))
