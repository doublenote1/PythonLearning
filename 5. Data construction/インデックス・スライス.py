# ****** 文字列 ******

# === インデックス(文字列) ===

word = 'Python'

'''
 文字列 'Python' のインデックス
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
'''

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

# === スライス(文字列) ===

print(word[0:2], word[2:6], sep=', ')
print(word[-6:-4], word[-4:6], sep=', ')
print()

# 最初のインデックスを省略  : 0
# 2番目のインデックスを省略 : 文字列のサイズ

print(word[:0] + word[0:], end=', ')
print(word[:1] + word[1:], end=', ')
print(word[:2] + word[2:], end=', ')
print(word[:3] + word[3:], end=', ')
print(word[:4] + word[4:], end=', ')
print(word[:5] + word[5:], end=', ')
print(word[:6] + word[6:])
print(word[:])
print(word[:7] + word[7:])  # スライス内では存在しないインデックスに対応
print()

# === 文字列は 不変(immutable) ===

try:
    word[0] = 'J'
except TypeError as e:
    print("word[0] = 'J' -> ERROR: " + str(e))

print('J' + word[1:])
print(word[:2] + 'py')
print()

# === 文字列の長さ ===

print('Length of \'' + word + '\' is ' + str(len(word)))
print()
