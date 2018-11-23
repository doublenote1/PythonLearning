# ****** 要素の取得(インデックス・スライス) ******

# === リスト・タプル(インデックス参照) ===

squares = [1, 4, 9, 16, 25, 36]

'''
 リスト squares のインデックス
 +---+---+---+----+----+----+
 | 1 | 4 | 9 | 16 | 25 | 36 |
 +---+---+---+----+----+----+
 0   1   2   3    4    5    6
-6  -5  -4  -3   -2   -1
'''

print(squares[0])  # -> 1
print(squares[-1])  # -> 36

# インデックス範囲外
try:
    print(squares[10])
except IndexError as e:
    print(e)  # -> list index out of range
print()

# === 文字列(インデックス参照) ===

word = 'Python'

'''
 文字列 'Python' のインデックス
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
'''

print(word[0])  # -> P
print(word[-1])  # -> n

# インデックス範囲外
try:
    print(word[10])
except IndexError as e:
    print(e)  # -> list index out of range
print()

# === スライス参照 ===

'''
文字列の場合を例に説明(リスト・タプル共通)
<リスト・文字列>[ <開始インデックス> : <終了インデックス> : <ステップ数> ]
'''

print(word[0:2], word[2:6], sep=',')  # Py,thon
print(word[-6:-4], word[-4:6], sep=',')  # Py,thon
print(word[0:-1:2])  # Pto
print()

# --- デフォルト値 ---

'''
開始インデックス : 0
終了インデックス : 文字列のサイズ
ステップ数       : 1
'''

print(word[:0] + word[0:])  # -> Python
print(word[:1] + word[1:])  # -> Python
print(word[:6] + word[6:])  # -> Python

# スライス内では存在しないインデックスに対応
print(word[:7] + word[7:])  # -> Python
# どの要素も選択されないと何もかえらない
print(word[4:2])
print(word[2:2])
print(word[10:20])

# 全体のコピー
print(word[:])  # -> Python
print()

# --- slice 関数 ---

sl = slice(1, 5, 2)
print(sl)  # -> slice(1, 5, 2)
print(type(sl))  # -> <class 'slice'>
print(word[sl])  # -> yh

sl = slice(1, 5)
print(sl)  # -> slice(1, 5, None)
print(word[sl])  # -> ytho

sl = slice(2)
print(sl)  # -> slice(None, 2, None)
print(word[sl])  # -> Py

sl = slice(None)
print(sl)  # -> slice(None, None, None)
print(word[sl])  # -> Python

print()

# ****** 要素の追加・変更・削除 ******

# === 文字列 ===

'''文字列要素は 追加・変更・削除不可(immutable)'''

word = 'Python'

try:
    word[0] = 'J'
except TypeError as e:
    print(e)  # -> 'str' object does not support item assignment

print('J' + word[1:])  # -> Jython
print()

# === リスト・タプル ===

cubes = [1, 8, 27, 65, 125]
print(cubes)  # -> [1, 8, 27, 65, 125]

# --- 要素の追加 ---

cubes.append(6 ** 3)
print(cubes)  # -> [1, 8, 27, 65, 125, 216]
cubes += [7 ** 3]
print(cubes)  # -> [1, 8, 27, 65, 125, 216, 343]
cubes += [8 ** 3, 9 ** 3]
print(cubes)  # -> [1, 8, 27, 65, 125, 216, 343, 512, 729]
print()

# --- 要素の変更 ---

cubes[3] = 4 ** 3
print(cubes)  # -> [1, 8, 27, 64, 125, 216, 343, 512, 729]
print()

# --- 要素の削除 ---

nums = list(range(9))
print(nums)  # -> [0, 1, 2, 3, 4, 5, 6, 7, 8]
del nums[0]
print(nums)  # -> [1, 2, 3, 4, 5, 6, 7, 8]
del nums[-1]
print(nums)  # -> [1, 2, 3, 4, 5, 6, 7]
del nums[3:5]
print(nums)  # -> [1, 2, 3, 6, 7]
del nums[::2]
print(nums)  # -> [2, 6]
del nums[:]
print(nums)  # -> []
print()

# --- スライスへ代入(要素の変更・削除) ---

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)  # -> ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 範囲変更
letters[2:5] = ['C', 'D', 'E']
print(letters)  # -> ['a', 'b', 'C', 'D', 'E', 'f', 'g']

# 範囲削除
letters[2:5] = []
print(letters)  # -> ['a', 'b', 'f', 'g']

# 全体を上書き
letters[:] = [1, 2, 3]
print(letters)  # -> [1, 2, 3]

# すべて削除
letters[:] = []
print(letters)  # -> []

print()

# ****** 演算 ******

# リスト・タプル
print([1, 2, 3] + [4, 5] * 3)  # -> [1, 2, 3, 4, 5, 4, 5, 4, 5]

# 文字列
print('Py' + 'Thon' * 3)  # -> PyThonThonThon

print()

# ****** 入れ子のリスト ******

s = ['a', 'b', 'c']
n = [1, 2, 3]
nest = [s, n, 'string', 100]
print(nest)  # -> [['a', 'b', 'c'], [1, 2, 3], 'string', 100]
print(nest[0])  # -> ['a', 'b', 'c']
print(nest[0][1])  # -> b
print(nest[2])  # -> string
print(len(nest))  # -> 4
print()
