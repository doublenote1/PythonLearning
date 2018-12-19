# 1. 四則演算

dummy = 0

'`float` を含むと 結果は `float`'
print(2 + 3.0)  # -> 5.0
'`/` は常に浮動小数点を返す'
print(17 / 3)  # -> 5.666666666666667
print(9 / 3)  # -> 3.0
'商'
print(17 // 3)  # -> 5
'余り'
print(17 % 3)  # -> 2
'階乗'
print(2 ** 7)  # -> 128
'優先順位有り'
print(2 + 5 * 3)  # -> 17
'複数の型の計算'
print(4 * 3.75 - 1)  # -> 14.0
print()

# 1.2. 割り算の商と余りを同時に取得

"""(a // b, a % b)のタプルを返す"""

# アンパックし変数に代入
q, mod = divmod(10, 3)
print(q, mod)  # -> 3 1

# 商と余りを要素とするタプルを返す
answer = divmod(10, 3)
print(answer)  # -> (3, 1)
print(answer[0], answer[1])  # -> 3 1
print()

# 2. 代入演算子

a = 1
a += 1
print(a)  # -> 2

a = 3
a -= 1
print(a)  # -> 2

a = 2
a *= 2
print(a)  # -> 4

a = 10
a /= 3
print(a)  # -> 3.3333333333333335

a = 10
a //= 3
print(a)  # -> 3

a = 10
a %= 3
print(a)  # -> 1

a = 3
a **= 2
print(a)  # -> 9
