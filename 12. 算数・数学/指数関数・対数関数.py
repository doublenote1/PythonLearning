import math

# === 自然対数の底（ネイピア数）: ===
# math.e

print(math.e)
print()

# === べき乗: ===
# **演算子, pow(), math.pow()

"""
・べき乗を計算するには
  ** 演算子, 組み込み関数 pow(), math.pow() のいずれかを使う
・x の y乗は、それぞれ、x**y, pow(x, y), math.pow(x, y) で得られる
"""
print(2**4)
print(pow(2, 4))
print(math.pow(2, 4))

"""
・math.pow() は引数を浮動小数点 float型に変換するのに対して、
  組み込み関数 pow() では各型それぞれで定義された __pow()__ を使って処理する
・例えば、pow() では引数に複素数 complex型を指定できるが、
  math.pow() では complex型から float型に変換できないため、エラーとなる
"""
print(pow(1 + 1j, 2))
try:
    print(math.pow(1 + 1j, 2))
except TypeError as e:
    print(e)

"""
・組み込み関数 pow() では第三引数を指定することができ、
  pow(x, y, z) は x の y乗に対する z の剰余（あまり）を返す
・pow(x, y) % z と同じ計算だが、pow(x, y, z) のほうが効率よく計算される
"""
print(pow(2, 4, 5))
print()

# === 平方根（ルート）: ===
# math.sqrt()

"""
平方根（ルート）は、べき乗演算子 ** を使って **0.5 とするか、
math.sqrt()を使う
"""
print(2**0.5)
print(math.sqrt(2))
print(2**0.5 == math.sqrt(2))

"""
math.pow() と同じく math.sqrt() では引数を浮動小数点 float型に変換して処理するため、
float型に変換できない型を指定するとエラー TypeError になる
"""
print((-3 + 4j)**0.5)

try:
    print(math.sqrt(-3 + 4j))
except TypeError as e:
    print(e)

"""また、math.sqrt() は負の値も処理できずエラー ValueError となる"""

print((-1)**0.5)

try:
    print(math.sqrt(-1))
except ValueError as e:
    print(e)

"""
なお、複素数を扱う場合、** 演算子を使った例では誤差が生じているが、
cmath モジュールを使うとより正確な値が得られる
"""
import cmath

print(cmath.sqrt(-3 + 4j))
print(cmath.sqrt(-1))
print()

# === 指数関数（自然指数関数）: ===
# math.exp()

"""
・自然対数の底（ネイピア数） e のべき乗を計算するには、math.exp()を使う
・math.exp(x) は e の x乗を返す
・math.exp(x) はmath.e ** x と等価でなく、math.exp(x) のほうがより正確な値となる
"""
print(math.exp(2))
print(math.exp(2) == math.e**2)
print()

# === 対数関数: ===
# math.log(), math.log10(), math.log2()

"""
・対数関数を計算するには、math.log(), math.log10(), math.log2() を使う
・math.log(x, y) は y を底とした x の対数を返す
・第二引数を省略すると次に示す自然対数となる
"""
print(math.log(25, 5))

# --- 自然対数 ---

"""
数学では log とか ln で表される自然対数（ネイピア数 e を底とする対数）は、
math.log(x) で計算できる
"""
print(math.log(math.e))

# --- 常用対数 ---

"""
常用対数（10 を底とする対数）は、math.log10(x) で計算できる
math.log(x, 10) よりも正確な値となる
"""
print(math.log10(100000))

# --- 二進対数 ---

"""
二進対数（2 を底とする対数）は、math.log2(x) で計算できる
math.log(x, 2) よりも正確な値となる
"""
print(math.log2(1024))
