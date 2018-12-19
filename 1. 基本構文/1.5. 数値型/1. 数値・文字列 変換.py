
# 1. 10進数・各基数文字列の相互変換

# 1.1. 各基数で「整数を表記」

# 2進数
print(0b10, 0B10)  # -> 2 2
# 8進数
print(0o10, 0O10)  # -> 8 8
# 16進数
print(0x10, 0X10)  # -> 16 16
# 各基数同士の四則演算も可能
print(0b10 + 0o10 + 0x10)  # -> 26
# 数値中に`_`を挿入しても無視される
print(0b_1111_1111_1111)  # -> 4095
print()

# 1.2. 10進数 を各基数表記の「文字列に変換」

i = 255
print(bin(i), type(bin(i)))  # -> 0b11111111 <class 'str'>
print(oct(i), type(oct(i)))  # -> 0o377 <class 'str'>
print(hex(i), type(hex(i)))  # -> 0xff <class 'str'>
print()

# 1.3. 各基数表記の文字列・浮動小数点数 を10進数の整数に変換

# (a) `int(整数表記の文字列型[, base=基数])`

"""
・第2引数を基数にして表記したものが第1引数になったと考える場合の、
  第1引数の10進数表記をint型で返す
・第2引数のデフォルトは`10`
・基数を0にすると、文字列のプレフィックス（0b, 0o, 0xまたは0B, 0O, 0X）
  をもとに変換される
"""

# 10進数として評価
print(int('10'))  # -> 10
print(int('10', 0))  # -> 10

# 2進数として評価
print(int('10', 2))  # -> 2
print(int('0b10', 0))  # -> 2
print(int('0B10', 0))  # -> 2

# 8進数として評価
print(int('10', 8))  # -> 8
print(int('0o10', 0))  # -> 8
print(int('0O10', 0))  # -> 8

# 16進数として評価
print(int('10', 16))  # -> 16
print(int('0x10', 0))  # -> 16
print(int('0X10', 0))  # -> 16

# (b) `int(float型)`

"""引数の整数部をint型として返す"""

print(int(123.456))  # -> 123
print()

# 2. 漢数字の文字列を浮動小数点数に変換

"""
`unicodedata`モジュールの`unicodedata.numeric()`関数を使うと
Unicodeの漢数字一文字を浮動小数点float型の数値に変換できる

一文字でないとエラーTypeError、数字ではない文字もエラーValueErrorになる
"""

import unicodedata

print(unicodedata.numeric('五'))  # -> 5.0
print(type(unicodedata.numeric('五')))  # -> <class 'float'>
print(unicodedata.numeric('十'))  # -> 10.0
print(unicodedata.numeric('参'))  # -> 3.0
print(unicodedata.numeric('億'))  # -> 100000000.0
print()

# 3. 数値の整数部・小数部を取得

# (a) math モジュールを使わず

a = 1.5
'整数部'
print(int(a))  # -> 1
'小数部'
print(a - int(a))  # -> 0.5
print()

# (b) math モジュールを使う

"""
`math.modf(float)`
引数の「小数部」・「整数部」の順番で、`float`型のタプルを返す
"""

import math

print(math.modf(1.5))  # -> (0.5, 1.0)
print(type(math.modf(1.5)))  # -> <class 'tuple'>

# 多重代入を併用
f, i = math.modf(1.5)
print(i)  # -> 1.0
print(f)  # -> 0.5

# 負の値を引数にする場合
f, i = math.modf(-1.5)
print(i)  # -> -1.0
print(f)  # -> -0.5

# 整数を引数にする場合
f, i = math.modf(100)
print(i)  # -> 100.0
print(f)  # -> 0.0
print()

