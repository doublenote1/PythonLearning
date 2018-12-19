"""
■ `random.random()` 0.0以上1.0未満の浮動小数点数
■ `random.uniform()` 任意の範囲の浮動小数点数
■ 正規分布やガウス分布などに従う乱数の生成
■ `random.randrange()` 任意の範囲・ステップの整数
■ `random.randint()` 任意の範囲の整数
■ ランダムな数値を要素とするリストの生成
    ・浮動小数点数floatの乱数のリスト
    ・整数intの乱数のリスト
■ 乱数シードを固定
"""

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
