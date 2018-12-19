# ****** 2つの整数の最大公約数・最小公倍数 ******

# === 最大公約数 ===

"""gcdは「greatest common divisor」の頭文字"""

import math

a, b = 6, 4
print(math.gcd(a, b))  # -> 2
print()

# === 最小公倍数 ===

"""
最小公倍数lcm（ least common multiple）を返す関数は用意されていないが、
lcm(a, b) = a * b / gcd(a, b)
なので、gcd()関数を使って簡単に算出できる。
"""

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

print(lcm(a, b))  # -> 12
print()

# ****** 3つ以上の整数の最大公約数、最小公倍数 ******

"""
・3つ以上の複数の整数の最大公約数・最小公倍数を求める場合、
  特に複雑なアルゴリズムは必要なく、
  2つずつ再帰的に演算していけばOK。

・高階関数 reduce() を使って複数の値に対して
  順番に最大公約数・最小公倍数を計算する。
    ・可変長引数で任意の個数の値を受け取る関数
    ・リスト（配列）で値を受け取る関数
  が考えられる。

・可変長引数を使う場合は*をつけることでリスト（配列）を渡すこともできる。
"""

# === 最大公約数 ===

import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

print(gcd(27, 18, 9))  # -> 9
print(gcd(27, 18, 9, 3))  # -> 3
print(gcd([27, 18, 9, 3]))  # -> [27, 18, 9, 3]
print(gcd(*[27, 18, 9, 3]))  # -> 3
print(gcd_list([27, 18, 9, 3]))  # -> 3
try:
    print(gcd_list(27, 18, 9, 3))
except TypeError as e:
    print(e)
print()

# === 最小公倍数 ===

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

print(lcm(27, 18, 9, 3))  # -> 54
print(lcm(27, 9, 3))  # -> 27
print(lcm(*[27, 9, 3]))  # -> 27
print(lcm_list([27, 9, 3]))  # -> 27
