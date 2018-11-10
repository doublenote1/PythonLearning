# ****** 多重代入 ******

# 左右の変数と値が同じ個数の場合(異なる型もＯＫ)
a, b, c = 0.1, 100, 'string'
print(a, b, c, sep=', ')  # -> 0.1, 100, string

# 左辺の半数が一つの場合はタプルとして代入
a = 0.1, 100, 'string'
print(a)  # -> (0.1, 100, 'string')

# ****** 変数やリストの値の入れ替え ******

# === 変数の入れ替え(交換) ===

# 変数2つ
a, b = 1, 2
a, b = b, a
print(a, b, sep=', ')  # -> 2, 1

# 変数3つ以上
a, b, c, d = 1, 2, 3, 4
a, b, c, d = b, c, d, a
print(a, b, c, d, sep=', ')  # -> 2, 3, 4, 1

# === リスト要素を入れ替え(並べ替え) ===

l = [0, 1, 2, 3, 4]
l[0], l[3] = l[3], l[0]
print(l)
print()

# ****** アンパック代入 ******

# === '*' 変数なしの場合 ===

# 変数の数 = 右辺のコンテナの要素数(ネスト可能)の形になる

t = (0, 1, 2)
a, b, c = t
print(a, b, c, sep=', ')  # -> 0, 1, 2

l = [0, 1, 2]
a, b, c = l
print(a, b, c, sep=', ')  # -> 0, 1, 2
print()

# 変数と値の要素数が一致していないとエラーになる

try:
    a, b = t
except Exception as e:
    print(type(e), e, sep=': ')

try:
    a, b, c, d = t
except Exception as e:
    print(type(e), e, sep=': ')
print()

# ネストしたタプル、リストのアンパック

t = (0, 1, (2, 3, 4))

a, b, c = t
print(a, b, c, sep=', ')  # -> 0, 1, (2, 3, 4)

a, b, (c, d, e) = t
print(a, b, c, d, e, sep=', ')  # -> 0, 1, 2, 3, 4
print()

#  === 変数に '*' を付ける場合 ===

# --- 変数の数 < 右辺の要素数 の場合 ---

# 変数名に '*' をつけると、その変数にあまった要素がリストとしてまとめて代入される
# '*' がついていない変数に先頭と末尾から先に要素が代入される
# '*' の利用は一回のみ

t = (0, 1, 2, 3, 4)

a, b, *c = t
print(a, b, c, sep=', ')  # -> 0, 1, [2, 3, 4]

a, *b, c = t
print(a, b, c, sep=', ')  # -> 0, [1, 2, 3], 4

*a, b, c = t
print(a, b, c, sep=', ')  # -> [0, 1, 2], 3, 4

# --- 変数の数 = 右辺の要素数 の場合 ---

# '*' がついた変数に該当要素がリストとして代入される

t = (0, 1, 2)

a, b, *c = t
print(a, b, c, sep=', ')  # -> 0, 1, [2]

# --- 変数の数が '*' の付いた変数を含めて、要素数+1 の場合 ---

# '*' がついた変数に空のリストが代入される

a, b, c, *d = t
print(a, b, c, d, sep=', ')  # -> 0, 1, 2, []
print()

# === '_' を使ったアンパック ===

# 慣例的に必要ない要素は '_' 変数 に代入する

t = (0, 1, 2)

a, b, _ = t
print(a, b, _, sep=', ')  # -> 0, 1, 2
a, *_ = t
print(a, _, sep=', ')  # -> 0, [1, 2]
print()

