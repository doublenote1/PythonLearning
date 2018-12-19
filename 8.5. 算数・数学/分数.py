# === 分数の生成: ===
# fractions.Fraction(<分子>[, <分母>])
# <分母> = 1

from fractions import Fraction

print(Fraction(1, 3))  # -> 1/3
print(Fraction(2, 6))  # -> 1/3
print(Fraction(3))  # -> 3
print()

"""小数（float型）の値を渡すと分数（Fraction型）に変換される"""
print(Fraction(0.25))  # -> 1/4
print(Fraction(0.33))  # -> 5944751508129055/18014398509481984
print()

"""文字列（str型）の値を渡すと分数（Fraction型）に変換される"""
print(Fraction('2/5'))  # -> 2/5
print(Fraction('16/48'))  # -> 1/3
print()

# === 分子、分母の値を整数で取得 ===

a = Fraction(1, 3)
print(a.numerator)  # -> 1
print(type(a.numerator))  # -> <class 'int'>
print(a.denominator)  # -> 3
print(type(a.denominator))  # -> <class 'int'>
print()

# === 分数（有理数）の計算・比較 ===

result = Fraction(1, 6) ** 2 + Fraction(1, 3) / Fraction(1, 2)
print(result)  # -> 25/36
print(type(result))  # -> <class 'fractions.Fraction'>
print()

"""比較演算子も使える"""
print(Fraction(7, 13) > Fraction(8, 15))  # -> True
print()

# === 分数から小数（float）への変換 ===

a = Fraction(1, 3)
a_f = float(a)
print(a_f)  # -> 0.3333333333333333
print(type(a_f))  # -> <class 'float'>
print()

"""小数（float）と計算するとfloat型に自動的に変換される"""
b = a + 0.1
print(b)  # -> 0.43333333333333335
print(type(b))  # -> <class 'float'>
print()

# === 分数から文字列（str）への変換 ===

a = Fraction(1, 3)
a_s = str(a)
print(a_s)  # -> 1/3
print(type(a_s))  # -> <class 'str'>
print()

# === 有理数近似を取得 ===

"""
・分母が引数 max_denominator 以下になる有理数（分数）を返す
・省略した場合は max_denominator = 1000000 となる。
"""

# --- 円周率 pi やネイピア数 e などの無理数を近似 ---

pi = Fraction(3.14159265359)
print(pi)  # -> 3537118876014453/1125899906842624
print(pi.limit_denominator(10))  # -> 22/7
print(pi.limit_denominator(100))  # -> 311/99
print(pi.limit_denominator(1000))  # -> 355/113
print()

e = Fraction(2.71828182846)
print(e)  # -> 6121026514870223/2251799813685248
print(e.limit_denominator(10))  # -> 19/7
print(e.limit_denominator(100))  # -> 193/71
print(e.limit_denominator(1000))  # -> 1457/536
print()

# --- 循環小数を分数に変換 ---

a = Fraction(0.565656565656)
print(a)  # -> 636872674577009/1125899906842624
print(a.limit_denominator())  # -> 56/99
print()

a = Fraction(0.3333)
print(a)  # -> 6004199023210345/18014398509481984
print(a.limit_denominator())  # -> 3333/10000
print(a.limit_denominator(100))  # -> 1/3
print()
