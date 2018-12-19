"""
■文字列補完

********* 文字列リテラルに値を挿入する方法 *********

・F-strings
    [r]f'{式[!変換指定子][:書式指定子]}'

・format() メソッド
    '{[field_name][!変換指定子][:書式指定子]}'.format(文字列リテラルに渡す値)

・format() 関数
    format(元の値, 書式指定子)

・% 演算子


********* フォーマット文字列リテラル *********

====== 変換指定子 ======

・式もしくは field_name の値を下記の関数で変換
'!read_s': str()
'!r': repr()
'!a': ascii()


====== 書式指定文字列の文法 ======

:[[埋め文字]揃え方向][符号][別形式][ゼロ埋め][最小フィールド幅][数値整形][.精度][表現型]

埋め文字:         フィールドの余りを埋める単一の文字
                  デフォルトは空白文字
                  揃え方向を指定する場合のみ指定可能

揃え方向:         '<': 左寄せ(ほとんどのオブジェクトにおいてのデフォルト)
                  '>': 右寄せ(いくつかのオブジェクトにおいてのデフォルト)
                  '^': 中央揃え
                  '=': 数値のみ右揃えにし符号は離す
                       ＜最小フィールド幅＞の直前が '0' の時はこれがデフォルト

符号:             '+': 正負表示
                  '-': 負のみ表示(デフォルト)
                  ' ': 負のみ表示(正は半角空白)

別形式:           '#': 別形式を出力
                       別形式は、異なる型に対して違った風に定義される
                       整数、浮動小数点数、複素数、10進数の型でのみ有効

                       2・8・16進数の「別形式」:
                          接頭辞を加える
                           2 進数: '0b'
                           8 進数: '0o'
                          16 進数: '0x'

                       浮動小数点数、複素数、10進数の「別形式」:
                          小数点文字の後に数字がなくても変換結果には常に小数点文字が含まれる
                          通常は、数字が続く場合にのみ小数点文字がこれらの変換結果に現われる
                          さらに、'g' と 'G' の変換については、最後の 0 は結果から取り除かれない

ゼロ埋め:         '0': 余白を 0 で埋めます。
                       ＜埋め文字＞が優先される

最小フィールド幅: 変換後の最小文字数を整数で指定します

数値整形:         ',': カンマ区切り
                  '_': 下線区切り
                       10 進数は 3 桁、その他は 4 桁区切りとなる

精度:             ドット '.' を前置した整数で指定します
                  浮動小数点数の表現型 'f', 'F' では小数点以下の桁数
                  'g', 'G' では小数点前後の桁数
                  それ以外の表現型では文字数

表現型:           値の型ごとに表現方法を指定できます


====== 表現型 ======

--- 文字列 ---

'read_s': 	   文字列(デフォルト)
指定なし:  read_s と同じ

--- 整数 ---

'd': 	   10 進数(デフォルト)
'b': 	    2 進数
'o': 	    8 進数
'x', 'X':  16 進数(小文字・大文字)
'n': 	   ロケールに従い区切り文字を挿入。それ以外は d と同じ
'c': 	   数値を Unicode 文字に変換
指定なし:  d と同じ

--- 浮動小数点数 ---

f, F:      固定小数点数(nan, inf の小文字・大文字)デフォルトの精度は 6 です
e, E:      指数表記(小文字・大文字)。デフォルトの精度は 6 です
g, G:      指数部が -4 以上または精度以下で固定小数点数(f, F)
           それ以外は指数表記(e, E)になります
           デフォルトの精度は 6 です
'n':       ロケールに従い区切り文字を挿入。それ以外は g と同じ
'%':       数値が 100 倍されパーセント記号 % 付きになります
指定なし:  g に近く、固定小数点数では少なくとも小数点以下が一桁
           デフォルトの精度は数値の高さと同じです

"""

# ****** F-strings の引数指定方法 ******

a, b = 1, 2
x, y = 'C:', 'folder'
print(f'{a} + {b} = {a + b}')  # -> 1 + 2 = 3
print(rf'{x}\{y}')
print()

# ****** format() メソッド の引数指定方法 ******

# 順番通り引数を指定
print('I like {} and {}!'.format('apple', 'susi'))  # -> I like apple and susi!

# 引数のインデックス指定(同じ要素の複数回指定可能)
print("{0}, {1}, {0}".format("Python", "Ruby"))  # -> Python, Ruby, Python

# 引数のキーワード指定
print('This {food} is {adjective}.'
      .format(food='spam', adjective='horrible'))  # -> This spam is horrible.

# 引数のインデックスとキーワード混在指定
print('The story of {0}, {1}, and {other}.'
      .format('Bill', 'Manfred',
              other='Georg'))  # -> The story of Bill, Manfred, and Georg.

# リスト・タプル引数の要素指定
l = ['one', 'two', 'three']
t = (1, 2, 3)
print('{0[0]}-{0[1]}-{0[2]}'.format(l))  # -> one-two-three
print('{0[0]}-{0[1]}-{0[2]}'.format(t))  # -> 1-2-3

# 辞書引数の要素指定
d1 = {'name': 'Alice', 'age': 20}
d2 = {'name': 'Bob', 'age': 30}
print('{0[name]} is {0[age]} years old.\n'
      '{1[name]} is {1[age]} years old.'.format(d1, d2))

# -> Alice is 20 years old.
# -> Bob is 30 years old.

# 引数の属性指定
class Coord(object):
    def __init__(self, lat, lon):
        self.lat, self.lon = lat, lon

coord = Coord('37.24N', '-115.81W')
print('Coordinates: {0.lat}, {0.lon}'.format(coord))

# リスト・辞書の要素を引数として展開
l = ['one', 'two', 'three']
print('{}-{}-{}'.format(*l))  # -> one-two-three
d = {'name': 'Alice', 'age': 20}
print('{name} is {age} years old.'.format(**d))  # -> Alice is 20 years old.
print()

# 波括弧{}自身を表したい時は、2回繰り返す
print('{{}}-{num}-{{{num}}}'.format(num=100))  # -> {}-100-{100}
print()

# @formatter:off

# ****** 書式指定の例 ******

# === 左・右・中央寄せ／符号整形 ===

# --- 指定文字数の寄せ ---

# 空白詰め(<>^)
print("{:<10}".format("left"))  # -> |left      |
print("{:>10}".format("right"))  # -> |     right|
print("{:^10}".format("center"))  # -> |  center  |
print()

# 埋め込み文字指定
print("{0:*<15}".format("Title"))  # -> |Title**********|
print("{0:-^15}".format("center"))  # -> |----center-----|
print("{0:0>15}".format(100))  # -> |000000000000100|
print()

# 符号を考慮した埋め込み)(=)
# '='を使用しない場合
print('{:0>10}'.format(-100))  # -> |000000-100|
# '='を使用する場合
print('{:0=10}'.format(-100))  # -> |-000000100|
# '+'を明示
print('{:0=+10}'.format(100))  # -> |+000000100|
# 文字列埋め込みに対し、'='は使えない
print('{:0=10}'.format(int('-100')))  # -> |-000000100|
print()

# ゼロ埋めの'='省略
# '='非省略形
print('{:0=10}'.format(100))  # -> |0000000100|
# '='省略型
print('{:010}'.format(100))  # -> |0000000100|
# '='非省略形
print('{:0=10}'.format(-100))  # -> |-000000100|
# '='省略型
print('{:010}'.format(-100))  # -> |-000000100|
print()

# --- 符号整形 ---

# デフォルト
print("{:-}".format(10))  # -> |10|
print("{:-}".format(-10))  # -> |-10|
# アラインメント
print("{:+}".format(10))  # -> |+10|
print("{:+}".format(-10))  # -> |-10|
print("{: }".format(10))  # -> | 10|
print("{: }".format(-10))  # -> |-10|
print()

# アラインメント記号のあとに符号指定記号を書く
print('{:_>6}'.format(100))  # -> ___100
print('{:_>6}'.format(-100))  # -> __-100
print('{:_>+6}'.format(100))  # -> __+100
print('{:_>+6}'.format(-100))  # -> __-100
print('{:_> 6}'.format(100))  # -> __ 100
print('{:_> 6}'.format(-100))  # -> __-100
print()

# === 桁区切り(,_) ===

print("{:,}".format(123456789))  # -> 123,456,789
print('{:_}'.format(123456789))  # -> 123_456_789
print()

# === N進法指定(bodxX) ===

# 2進数
print("{:b}".format(10))  # -> 1010
# 8進数
print("{:o}".format(10))  # -> 10
# 10進数
print("{:d}".format(10))  # -> 12
# 16進数(小文字)
print("{:x}".format(10))  # -> a
# 16進数(大文字)
print("{:X}".format(10))  # -> A
print()

# 0埋め込みとの組み合わせ
print('{:08b}'.format(255))  # -> 11111111
print('{:08o}'.format(255))  # -> 00000377
print('{:08d}'.format(255))  # -> 00000255
print('{:08x}'.format(255))  # -> 000000ff
print('{:08X}'.format(255))  # -> 000000FF
print()

# 接頭辞付与(#)
print('dec: {:#010d}'.format(255))  # -> 0000000255
print('bin: {:#010b}'.format(255))  # -> 0b11111111
print('oct: {:#010o}'.format(255))  # -> 0o00000377
print('hex: {:#010x}'.format(255))  # -> 0x000000ff
print('HEX: {:#010X}'.format(255))  # -> 0X000000FF

print('{:#d}'.format(255))  # -> 00400000255
print('{:#010_}'.format(2416498546455.12546462))  # -> 0000000255
print()

# === 小数点以下数値丸め(.[桁数]f%) ===

# 浮動小数点
print("{:.1f}".format(10.82))  # -> 10.8
print("{:.2f}".format(10.82))  # -> 10.82
print("{:.3f}".format(10.82))  # -> 10.820
print("{:.4f}".format(10.82))  # -> 10.8200
print()

# パーセンテージ
print("{:.1%}".format(10.8212))  # -> 1082.1%
print("{:.2%}".format(10.8212))  # -> 1082.12%
print("{:.3%}".format(10.8212))  # -> 1082.120%
print("{:.4%}".format(10.8212))  # -> 1082.1200%
print()

# ****** 例文 ******

# === 例文1 ===

# format文無し

for x in range(1, 5):
    # ljust():左詰め ,center():中央揃え ,rjust():右詰め
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x * x * x).rjust(4))
print()

# format文有り

for x in range(1, 5):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
print()

# === 例文2 ===

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))
print()

# === 例文3 ===

contents = 'eels'
num = 1
print('My hovercraft is full of {}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))
print('My hovercraft is full of {!s}.'.format(num))
print()

# === 例文4 ===

import math

print('The value of PI is approximately {0:.3f}.'.format(math.pi))
print()

# === 例文5 ===

print(format(255, '04x'))
print(format('center', '*^16'))
