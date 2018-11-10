# ****** 数値型 ******

print(17 / 3)  # '/' は常に浮動小数点を返す
print(9 / 3)
print(17 // 3)  # 商
print(17 % 3)  # 余り
print(5 * 3 + 2)  # 優先順位有り
print(2 ** 7)  # 階乗
print(4 * 3.75 - 1)  # 複数の型の計算
print()

# ****** 文字列型 ******

# === エスケープシーケンス ===

# \\         : '\' 文字そのもの
# \'         : シングルクオーテーション
# \"         : ダブルクオーテーション
# \a         : ベル
# \b         : バックスペース
# \f         : 改ページ
# \r         : キャリッジリターン
# \n         : 改行
# \t         : 水平タブ
# \v         : 垂直タブ
# \N{name}   : Unicode データベース中で名前 name を持つ文字
# \uxxxx     : 16ビットの16進数値xxxxを持つUnicode文字
# \Uxxxxxxxx : 32ビットの16進数値xxxxxxxxを持つUnicode文字
# \ooo       : 8進数oooを持つASCII文字
# \xhh       : 16進数hhを持つASCII文字
# \0         : NULL

# === 文字列演算 ===

print(3 * 'un' + 'ium')
print()

# === エスケープシーケンスを無効化(raw 文字列) ===

print('C:\some\\name\\test')  # 通常文字列
print(r'C:\some\name\test')  # raw 文字列

# 末尾に奇数個の '\' を表現したい場合
print('C:\some\\name\\test\\')  # 通常文字列
print(r'C:\some\name\test' + '\\')  # raw 文字列 + 通常文字列

# 末尾に偶数個の '\' を表現したい場合
print('C:\some\\name\\test\\\\')  # 通常文字列
print(r'C:\some\name\test\\')  # raw 文字列
print()

# ****** インデックス・スライス ******

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
    word[2:] = 'py'
except TypeError as e:
    print("word[0] = 'J' -> ERROR: " + str(e))
    print("word[2:] = 'py' -> ERROR: " + str(e))
print('J' + word[1:])
print(word[:2] + 'py')
print()

# === 文字列の長さ ===

print('Length of \'' + word + '\' is ' + str(len(word)))
print()

# ****** リスト型 ******

# 要素の取得
squares = [1, 4, 9, 16, 25]
print(squares[0], end=' | ')
print(squares[-1], end=' | ')
print(squares[-3:], end=' | ')
print(squares[:])
print()

# リストの連結
print(squares + [36, 49, 64, 81, 100])
print()

# 要素の変更
cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 4 ** 3
print(cubes)
print()

# 要素の追加
cubes.append(6 ** 3)
cubes.append(7 ** 3)
print(cubes)
print()

# スライスへ代入

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

letters[2:5] = ['C', 'D', 'E']
print(letters)

letters[2:5] = []
print(letters)

letters[:] = []
print(letters)

letters[:] = [1, 2, 3]
print(letters)

# 要素のサイズ取得
print(len(letters))
print()

# 入れ子のリスト
s = ['a', 'b', 'c']
n = [1, 2, 3]
nest = [s, n, 'string', 100]
print('nest =', nest)
print('nest[0] =', nest[0])
print('nest[0][1] =', nest[0][1])
print('nest[2] =', nest[2])
print('size =', len(nest))
