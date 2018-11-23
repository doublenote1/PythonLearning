# ****** 数値の整数部と小数部を同時に取得 ******

# --- math モジュールを使わず ---

a = 1.5
i = int(a)
f = a - int(a)
print(i)
print(f)
print()

# --- math.modf() を使う: ---
# math.modf()

import math

print(math.modf(1.5))
print(type(math.modf(1.5)))

f, i = math.modf(1.5)
print(i)
print(f)

f, i = math.modf(-1.5)
print(i)
print(f)

f, i = math.modf(100)
print(i)
print(f)

print()

# ****** 2・8・16進数の数値・文字列相互変換 ******

# === 2・8・16進数で記述 ===

# 2進数
print(0b10, 0B10)
# 8進数
print(0o10, 0O10)
# 16進数
print(0x10, 0X10)
# 四則演算
print(0b10 * 0o10 + 0x10)
# 数値中にどこにでも '_' を挿入可能
print(0b1111_1111_1111)
print()

# === 数値を2・8・16進数表記の文字列に変換 ===

i = 255
print(bin(i), type(bin(i)))
print(oct(i), type(oct(i)))
print(hex(i), type(hex(i)))
print()

# === 2・8・16進数表記の文字列を数値(10進数)に変換: ===
# int(<数値文字列>, base(基数)=10)

dec_num = int('10')
bin_num = int('10', 2)
oct_num = int('10', 8)
hex_num = int('10', 16)

print(dec_num, type(dec_num))
print(bin_num, type(bin_num))
print(oct_num, type(oct_num))
print(hex_num, type(hex_num))
print()

# 基数を0にすると、文字列のプレフィックス（0b, 0o, 0xまたは0B, 0O, 0X）
# をもとに変換される

print(int('10', 0))
print(int('0b10', 0))
print(int('0o10', 0))
print(int('0x10', 0))
print(int('0B10', 0))
print(int('0O10', 0))
print(int('0X10', 0))
print()

# === 活用例 ===

a = '0b1001'
b = '0b0011'
c = int(a, 0) + int(b, 0)
print(c)
print(bin(c))
print()

# ****** 漢数字の文字列を数値に変換 ******

'''
unicodedataモジュールのunicodedata.numeric()関数を使うと
Unicodeの漢数字一文字を浮動小数点float型の数値に変換できる

一文字じゃないとエラーTypeError、数字ではない文字もエラーValueErrorになる
'''

import unicodedata

print(unicodedata.numeric('五'))
print(type(unicodedata.numeric('五')))
print(unicodedata.numeric('十'))
print(unicodedata.numeric('参'))
print(unicodedata.numeric('億'))
print()

# ****** 端数処理 ******

# === round(number[,ndigits(桁)]) ===

'''
偶数への丸めは、端数が0.5より小さいなら切り捨て、
端数が0.5より大きいならは切り上げ、
端数がちょうど0.5なら切り捨てと切り上げのうち結果が偶数となる方へ丸める
'''

# --- 小数の場合 ---

'''
ndigits:
    省略:     1の位へ丸めたint 型を取得
    0:        1の位へ丸めたフロート型を取得
    正の整数(有効桁数範囲内): 小数点以下の指定の桁へ丸める
    正の整数(有効桁数範囲外): 元の値をかえす
    負の整数(有効桁数範囲内): 整数の指定の桁へ丸める(-1 = 10の位)
    負の整数(有効桁数範囲外): 0 をかえす(-1 = 10の位)

'''

f = 123.456
print(round(f))  # -> 123
print(round(f, 0))  # -> 123.0
print(round(f, 1))  # -> 123.5
print(round(f, 2))  # -> 123.46
print(round(f, 3))  # -> 123.456
print(round(f, 4))  # -> 123.456
print(round(f, -1))  # -> 120.0
print(round(f, -2))  # -> 100.0
print(round(f, -3))  # -> 0.0
print(round(i, -4))  # -> 0
print()

# --- 整数の場合 ---

'''
ndigits:
    省略:     元の値をかえす
    0:        元の値をかえす
    正の整数: 元の値をかえす
    負の整数(有効桁数範囲内): 整数の指定の桁へ丸める(-1 = 10の位)
    負の整数(有効桁数範囲外): 0 をかえす
'''

i = 99518
print(round(i))  # -> 99518
print(round(i, 0))  # -> 99518
print(round(i, 1))  # -> 99518
print(round(i, -1))  # -> 99520
print(round(i, -2))  # -> 99500
print(round(i, -3))  # -> 100000
print(round(i, -4))  # -> 100000
print(round(i, -5))  # -> 100000
print(round(i, -6))  # -> 0
print()

# --- 偶数への丸めの挙動 ---

print(round(0.4))  # -> 0
print(round(0.5))  # -> 0
print(round(0.6))  # -> 1

print(round(4, -1))  # -> 0
print(round(5, -1))  # -> 0
print(round(6, -1))  # -> 10

print(round(0.5))  # -> 0
print(round(1.5))  # -> 2
print(round(2.5))  # -> 2
print(round(3.5))  # -> 4
print(round(4.5))  # -> 4
print()

'''
小数点以下2桁以降の処理では
偶数への丸めの定義にも当てはまらない場合もある
'''
print(round(0.05, 1))  # -> 0.1
print(round(0.15, 1))  # -> 0.1
print(round(0.25, 1))  # -> 0.2
print(round(0.35, 1))  # -> 0.3
print(round(0.45, 1))  # -> 0.5
print()

# === 正確な十進浮動小数点数を扱う ===

# --- Decimalオブジェクトの生成 ---

'''
Decimal()でDecimal型のオブジェクトを生成できる。
float型ではなく文字列str型を指定すると正確にその値のDecimal型として扱われる
'''

from decimal import *

# 引数に float型を指定すると、実際は誤差が生じていることがわかる
# ただし、0.5 は 1/2 なので2進法で正確に表現できる

print(Decimal(0.1))
# -> 0.1000000000000000055511151231257827021181583404541015625
print(Decimal(0.5))
# -> 0.5
print(Decimal(0.9))
# -> 0.90000000000000002220446049250313080847263336181640625
print(type(Decimal(0.1)))
# -> <class 'decimal.Decimal'>
print()

# 引数に str型を指定すると、正確にその値のDecimal型として扱われる

print(Decimal('0.1'))  # -> 0.1
print(Decimal('0.5'))  # -> 0.5
print(Decimal('0.9'))  # -> 0.9
print(type(Decimal('0.1')))  # -> <class 'decimal.Decimal'>
print()

# --- Decimalオブジェクトの計算 ---

def calc(*o):
    try:
        result = sum(o)
        print(result, type(result))
    except TypeError as e:
        print(e)

# float型が含まれる計算
calc(0.1, 0.2, 0.3, 100)
# -> 0.6000000000000001 <class 'float'>

# float型の代わりに Decimal型を使った計算
calc(Decimal('0.1'), Decimal('0.2'), Decimal('0.3'), 100)
# -> 0.6 <class 'decimal.Decimal'>

# float型と Decimal型同士の計算はエラーになる
calc(Decimal('0.1'), 0.2, Decimal('0.3'), 100)
# -> unsupported operand type(s) for +: 'decimal.Decimal' and 'float'

print()

# --- 小数を任意の桁数で四捨五入・偶数への丸め: ---

'''
桁を指定するには浮動小数点数を使用
'''

# 四捨五入

f = 123.456
print(Decimal(str(f)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
print(Decimal(str(f)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
print(Decimal(str(f)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
print(Decimal(str(f)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
print(Decimal(str(f)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))
print(Decimal(str(0.4)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
print(Decimal(str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
print(Decimal(str(0.6)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
print()

# 偶数への丸め

print(Decimal(str(0.05)).quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))
print(Decimal(str(0.15)).quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))
print(Decimal(str(0.25)).quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))
print(Decimal(str(0.35)).quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))
print(Decimal(str(0.45)).quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))
print()

# --- 整数を任意の桁数で四捨五入・偶数への丸め ---

'''
桁を指定するには指数表記を使用
1E1: 10
1E2: 100
1E3: 1000
'''

i = 99518
print(Decimal(i).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP))
print(int(Decimal(i).quantize(Decimal('1E0'), rounding=ROUND_HALF_UP)))
print(int(Decimal(i).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)))
print(int(Decimal(i).quantize(Decimal('1E2'), rounding=ROUND_HALF_UP)))
print(int(Decimal(i).quantize(Decimal('1E3'), rounding=ROUND_HALF_UP)))
print(int(Decimal(i).quantize(Decimal('1E4'), rounding=ROUND_HALF_UP)))
print(int(Decimal(i).quantize(Decimal('1E5'), rounding=ROUND_HALF_UP)))
print(int(Decimal(i).quantize(Decimal('1E6'), rounding=ROUND_HALF_UP)))
print()
print(int(Decimal(4).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)))
print(int(Decimal(5).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)))
print(int(Decimal(6).quantize(Decimal('1E1'), rounding=ROUND_HALF_UP)))
print()

# ****** ランダムな小数・整数を生成する ******

'''
■ random.random()（0.0以上1.0未満の浮動小数点数）
■ random.uniform()（任意の範囲の浮動小数点数）
■ 正規分布やガウス分布などに従う乱数の生成
■ random.randrange()（任意の範囲・ステップの整数）
■ random.randint()（任意の範囲の整数）
■ ランダムな数値を要素とするリストの生成
    ・浮動小数点数floatの乱数のリスト
    ・整数intの乱数のリスト
■ 乱数シードを固定
'''

import random

# === 0.0以上 1.0未満の浮動小数点数: ===
# random.random()

print(random.random())

# === 任意の範囲(a <= n <= b or b <= n <= a)の浮動小数点数: ===
# random.uniform(a, b)

print(random.uniform(100, 200))
print(random.uniform(100, -100))
print(random.uniform(100, 100))
print(random.uniform(1.234, 5.637))

# === 正規分布やガウス分布などに従う乱数の生成 ===

'''
・ベータ分布:           random.betavariate()
・指数分布:             random.expovariate()
・ガンマ分布:           random.gammavariate()
・ガウス分布:           random.gauss()
・対数正規分布:         random.lognormvariate()
・正規分布:             random.normalvariate()
・フォン・ミーゼス分布: random.vonmisesvariate()
・パレート分布:         random.paretovariate()
・ワイブル分布:         random.weibullvariate()
'''

# === range() の要素からランダムに選ばれた整数 ===
# random.randrange(stop)
# random.randrange(start,stop[,step])

print(random.randrange(10))
print(random.randrange(10, 20, 2))

# === 任意の範囲(a <= n <= b)の整数: ===
# random.randint(a, b)

print(random.randint(50, 100))

# === ランダムな数値を要素とするリストの生成 ===

# --- 浮動小数点数の乱数のリスト ---

print([random.random() for i in range(5)])
print([random.uniform(100, 200) for i in range(5)])

# --- 整数の乱数のリスト ---

'''値が重複する可能性有り'''
print([random.randrange(0, 10, 2) for i in range(5)])
print([random.randint(0, 10) for i in range(5)])

'''値が重複する可能性無し'''
print(random.sample(range(10), k=5))
print(random.sample(range(100, 200, 10), k=5))

# === 乱数シードを固定 ===

'''
random.seed()に任意の整数を与えることで、乱数シードを固定することができる
常に同じ要素が返る
'''

random.seed(0)
print(random.random())

# ****** 数値が整数か小数かを判定 ******

# === float型の数値が整数（小数点以下が0）か判定: ===
# float.is_integer()

print(1.23.is_integer())
print(100.0.is_integer())
print()

# 整数の数値(int型および整数のfloat型)に対して True を返す関数

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

print(is_integer_num(100))
print(is_integer_num(1.23))
print(is_integer_num(100.0))
print(is_integer_num('100'))
print()

# 整数の数値、整数の数値を表す文字列(int型、整数の float型および str型)
# に対して True をかえす関数

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

print(is_integer(100))
print(is_integer(100.0))
print(is_integer(1.23))
print(is_integer('100'))
print(is_integer('100.0'))
print(is_integer('1.23'))
print(is_integer('string'))
print()
