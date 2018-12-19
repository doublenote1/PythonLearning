from user import print_err

# 1. `round(数値[, 桁数])`

"""
・「桁数」は1以上なら小数点以下の桁を表し、
  省略するか0なら1の位を表し、
  負数は10の位以上の整数の位を表す
・指定した「桁数」より下の丸める端数が
  その桁の5より、
  「小さい」なら「切り捨て」、
  「大きい」なら「切り上げ」、
  ちょうど「5」なら「切り捨て」と「切り上げ」の内、
  指定「桁数」の位が偶数となる方を選択する
・ただし、小数部に丸める場合は、小数に誤差が生じる為、
  上記の「ちょうど５」の場合の定義に当てはまらない
"""

# 1.1. 端数ごとの切り捨て・切り上げの挙動

# (a) 小数点1位までを丸める場合

print(round(0.4))  # -> 0
print(round(0.5))  # -> 0
print(round(0.6))  # -> 1

print(round(1.4))  # -> 1
print(round(1.5))  # -> 2
print(round(1.6))  # -> 2
print()

print(round(4, -1))  # -> 0
print(round(5, -1))  # -> 0
print(round(6, -1))  # -> 10

print(round(14, -1))  # -> 10
print(round(15, -1))  # -> 20
print(round(16, -1))  # -> 20
print()

# (b) 小数点2位以降を丸める場合

"""
小数点以下2桁以降の処理では
「偶数への丸め」の定義が当てはまらない場合がある
"""

print(round(0.05, 1))  # -> 0.1
print(round(0.15, 1))  # -> 0.1
print(round(0.25, 1))  # -> 0.2
print(round(0.35, 1))  # -> 0.3
print(round(0.45, 1))  # -> 0.5
print()

# 1.2. 「桁数」ごとの丸め方

f = 123.456
i = 123

# (a) 「桁数」が有効範囲内の場合

# 「桁数」省略
"""1の位へ丸めたint型を取得"""

print(round(f))  # -> 123

# 「桁数」が0
"""1の位へ丸めたフロート型を取得"""

print(round(f, 0))  # -> 123.0

# 「桁数」が1以上の整数
"""指定の桁へ丸める"""

print(round(f, 1))  # -> 123.5
print(round(f, 2))  # -> 123.46

# 「桁数」が負の整数
"""整数の指定の桁へ丸める(-1 = 10の位)"""

print(round(f, -1))  # -> 120.0
print(round(f, -2))  # -> 100.0
print(round(i, -1))  # -> 120
print(round(i, -2))  # -> 100
print()

# (b) 小数点側で、丸める位が無い場合
"""元の値を返す"""

print(round(f, 3))  # -> 123.456
print(round(f, 4))  # -> 123.456
print(round(i))  # -> 123
print(round(i, 0))  # -> 123
print(round(i, 1))  # -> 123
print()

# (c) 整数側で、指定「桁数」が無い場合
"""0を返す(-1 = 10の位)"""

print(round(f, -3))  # -> 0.0
print(round(f, -4))  # -> 0.0
print(round(i, -3))  # -> 0
print(round(i, -4))  # -> 0
print()

# 2. 正確な十進浮動小数点数を扱う

# 2.1. Decimalオブジェクトの生成

"""
・`Decimal()`でDecimal型のオブジェクトを生成できる
・float型ではなく文字列str型を指定すると正確にその値のDecimal型として扱われる
"""

from decimal import *

# (a) 引数に float型を指定

"""
・引数に float型を指定すると、実際は誤差が生じていることがわかる
・ただし、0.5 は 1/2 なので2進法で正確に表現できる
"""

print(Decimal(0.1))
# -> 0.1000000000000000055511151231257827021181583404541015625
print(Decimal(0.5))
# -> 0.5
print(Decimal(0.9))
# -> 0.90000000000000002220446049250313080847263336181640625
print(type(Decimal(0.1)))
# -> <class 'decimal.Decimal'>
print()

# (b) 引数に str型を指定

"""引数に str型を指定すると、正確にその値のDecimal型として扱われる"""

print(Decimal('0.1'))  # -> 0.1
print(Decimal('0.5'))  # -> 0.5
print(Decimal('0.9'))  # -> 0.9
print(type(Decimal('0.1')))  # -> <class 'decimal.Decimal'>
print()

# 2.2. Decimalオブジェクトの計算

def calc(*o):
    try:
        result = sum(o)
        print(result, type(result))
    except TypeError as e:
        print_err(e)

'float型が含まれる計算'
calc(0.1, 0.2, 0.3)
# -> 0.6000000000000001 <class 'float'>

'float型の代わりに Decimal型を使った計算'
calc(Decimal('0.1'), Decimal('0.2'), Decimal('0.3'))
# -> 0.6 <class 'decimal.Decimal'>

'float型と Decimal型同士の計算はエラーになる'
calc(Decimal('0.1'), 0.2, Decimal('0.3'))
# -> TypeError: unsupported operand type(s) for +: 'decimal.Decimal' and 'float'
print()

# 2.3. Decimalオブジェクトの端数処理

"""
・小数部を丸める場合:
  `Decimal(str(<対象数値>)).quantize(Decimal('<`0`か小数で桁を指定>'), rounding=<丸め方>)`
・整数部を丸める場合:
  `int(Decimal(<対象数値>).quantize(Decimal(<指数で桁を指定>), rounding=<丸め方>))`
  
・丸めオプション:
  ROUND_CEILING : 正の無限大に近づく様に丸める
  ROUND_FLOOR : 負の無限大に近づく様に丸める
  ROUND_UP : 0から離れる様に丸める
  ROUND_DOWN : 0に近づく様に丸める
  ROUND_HALF_UP : もっとも近い「数字」に丸める （5は切り上げ）
  ROUND_HALF_DOWN : もっとも近い「数字」に丸める （5は切り捨て）
  ROUND_HALF_EVEN :  もっとも近い「数字」に丸める （5は偶数へ丸める）
"""

import re
def custom_quantize(num, digit, rounding_type):
    # 小数の端数処理
    if re.match(r'^0(\.0*1)?$', digit):
        print(Decimal(str(num)).quantize(Decimal(digit), rounding=rounding_type))
    # 整数への丸め
    else:
        print(int(Decimal(num).quantize(Decimal(digit), rounding=rounding_type)))

# 2.3.1. 丸める桁の指定

# (a) 小数の端数処理
"""桁を指定するには浮動小数点数を使用"""

custom_quantize(123.456, '0', ROUND_HALF_UP)  # -> 123
custom_quantize(123.456, '0.1', ROUND_HALF_UP)  # -> 123.5
custom_quantize(123.456, '0.01', ROUND_HALF_UP)  # -> 123.46
custom_quantize(123.456, '0.001', ROUND_HALF_UP)  # -> 123.456
custom_quantize(123.456, '0.0001', ROUND_HALF_UP)  # -> 123.4560

# (b) 整数部の丸め
"""
桁を指定するには指数表記を使用
1E1: 10
1E2: 100
1E3: 1000
"""

custom_quantize(123.456, '1E1', ROUND_HALF_UP)  # -> 120
custom_quantize(123.456, '1E2', ROUND_HALF_UP)  # -> 100
custom_quantize(123.456, '1E3', ROUND_HALF_UP)  # -> 0
custom_quantize(123.456, '1E4', ROUND_HALF_UP)  # -> 0
print()

# 2.3.2. 丸めオプションごとの挙動

# (a) ROUND_CEILING
"""正の無限大に近づく様に丸める"""

custom_quantize(0.15, '0.1', ROUND_CEILING)  # -> 0.2
custom_quantize(-0.15, '0.1', ROUND_CEILING)  # -> -0.1
print()

# (b) ROUND_FLOOR
"""負の無限大に近づく様に丸める"""

custom_quantize(0.15, '0.1', ROUND_FLOOR)  # -> 0.1
custom_quantize(-0.15, '0.1', ROUND_FLOOR)  # -> -0.2
print()

# (c) ROUND_UP
"""0から離れる様に丸める"""

custom_quantize(0.15, '0.1', ROUND_UP)  # -> 0.2
custom_quantize(-0.15, '0.1', ROUND_UP)  # -> -0.2
print()

# (d) ROUND_DOWN
"""0に近づく様に丸める"""

custom_quantize(0.15, '0.1', ROUND_DOWN)  # -> 0.1
custom_quantize(-0.15, '0.1', ROUND_DOWN)  # -> -0.1
print()

# (e) ROUND_HALF_UP
"""もっとも近い「数字」に丸める （5は切り上げ）"""

custom_quantize(0.14, '0.1', ROUND_HALF_UP)  # -> 0.1
custom_quantize(0.15, '0.1', ROUND_HALF_UP)  # -> 0.2
custom_quantize(0.16, '0.1', ROUND_HALF_UP)  # -> 0.2
custom_quantize(-0.14, '0.1', ROUND_HALF_UP)  # -> -0.1
custom_quantize(-0.15, '0.1', ROUND_HALF_UP)  # -> -0.2
custom_quantize(-0.16, '0.1', ROUND_HALF_UP)  # -> -0.2
print()

# (f) ROUND_HALF_DOWN
"""もっとも近い「数字」に丸める （5は切り捨て）"""

custom_quantize(0.14, '0.1', ROUND_HALF_DOWN)  # -> 0.1
custom_quantize(0.15, '0.1', ROUND_HALF_DOWN)  # -> 0.1
custom_quantize(0.16, '0.1', ROUND_HALF_DOWN)  # -> 0.2
custom_quantize(-0.14, '0.1', ROUND_HALF_DOWN)  # -> -0.1
custom_quantize(-0.15, '0.1', ROUND_HALF_DOWN)  # -> -0.1
custom_quantize(-0.16, '0.1', ROUND_HALF_DOWN)  # -> -0.2
print()

# (g) ROUND_HALF_EVEN
"""もっとも近い「数字」に丸める （5は偶数へ丸める）"""

custom_quantize(0.14, '0.1', ROUND_HALF_EVEN)  # -> 0.1
custom_quantize(0.25, '0.1', ROUND_HALF_EVEN)  # -> 0.2
custom_quantize(0.35, '0.1', ROUND_HALF_EVEN)  # -> 0.4
custom_quantize(0.16, '0.1', ROUND_HALF_EVEN)  # -> 0.2
custom_quantize(-0.14, '0.1', ROUND_HALF_EVEN)  # -> 0.1
custom_quantize(-0.25, '0.1', ROUND_HALF_EVEN)  # -> 0.2
custom_quantize(-0.35, '0.1', ROUND_HALF_EVEN)  # -> 0.4
custom_quantize(-0.16, '0.1', ROUND_HALF_EVEN)  # -> 0.2
print()
