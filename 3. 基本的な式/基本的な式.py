# === 数値型 ===

print(17 / 3)  # '/' は常に浮動小数点を返す
print(9 / 3)
print(17 // 3)  # 商
print(17 % 3)  # 余り
print(5 * 3 + 2)
print(2 ** 7)  # 階乗
print(4 * 3.75 - 1)  # 複数の型の計算
print()

# === 文字列型 ===

# エスケープシーケンスを無効化（raw 文字列）

print('C:\some\name\test\\')
print(r'C:\some\name\test' + '\\')  # 末尾に奇数子の '\' は使えない
print(r'C:\some\name\test\\')  # 末尾に偶数個の '\' は使える
print()

# 三連引用符

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 文字列演算

print(3 * 'un' + 'ium')
print('Py' 'thon')  # 2つのリテラル同士のみ結合
print('Put several strings within parentheses '
      'to have them joined together.')
print()

# インデックス・スライス

word = 'Python'

'''
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
'''

# インデックス

print(word[0], end=', ')
print(word[5], end=', ')
print(word[-1], end=', ')
print(word[-2], end=', ')
print(word[-6])
try:
    print(word[10])
except IndexError as e:
    print('print(word[10]) -> ERROR: ' + str(e))
print()

# スライス

print(word[0:2], end=', ')
print(word[2:5])

print(word[:2], end=', ')
print(word[4:], end=', ')
print(word[-2:])
print()

print(word[:0] + word[0:], end=', ')
print(word[:1] + word[1:], end=', ')
print(word[:2] + word[2:], end=', ')
print(word[:3] + word[3:], end=', ')
print(word[:4] + word[4:], end=', ')
print(word[:5] + word[5:], end=', ')
print(word[:6] + word[6:], end=', ')
print(word[:7] + word[7:])  # スライス内では存在しないインデックスに対応
print()

# 文字列は 不変（immutable）

try:
    word[0] = 'J'
    word[2:] = 'py'
except TypeError as e:
    print("word[0] = 'J' -> ERROR: " + str(e))
    print("word[2:] = 'py' -> ERROR: " + str(e))
print('J' + word[1:])
print(word[:2] + 'py')
print()

# 文字列の長さ

print('Length of \'' + word + '\' is ' + str(len(word)))
print()

# === リスト型 ===

squares = [1, 4, 9, 16, 25]
print(squares[0], end=' | ')
print(squares[-1], end=' | ')
print(squares[-3:], end=' | ')
print(squares[:])

more = [36, 49, 64, 81, 100]
print(squares + more)
print()

cubes = [1, 8, 27, 65, 125]
print(cubes, end=' -> ')
cubes[3] = 4 ** 3
print(cubes)
cubes.append(6 ** 3)
cubes.append(7 ** 3)
print(cubes)
print()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)
letters[:] = [1, 2, 3]
print(letters, end=' -> ')
print('Length of <letters> is ' + str(len(letters)))
print()

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print('x =', x)
print('x[0] = ', x[0])
print('x[0][1] = ', x[0][1])
