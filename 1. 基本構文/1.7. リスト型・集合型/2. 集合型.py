# ****** set・frozenset の生成 ******

# === 直接要素を代入して生成 ===

s = {0, 0, 1, 1, 2, 2, 3, 3}
print(s)  # -> {0, 1, 2, 3}
print(type(s))  # -> <class 'set'>
print()

fs = frozenset([0, 0, 1, 1, 2, 2, 3, 3])
print(fs)  # -> frozenset({0, 1, 2, 3})
print(type(fs))  # -> <class 'frozenset'>
print()

"""
空の波括弧 {} は辞書型 dict と見なされるため、
空の set型オブジェクト（空集合）を生成するには
set() コンストラクタを使う
"""
empty = {}
print(empty)  # -> {}
print(type(empty))  # -> <class 'dict'>

empty = set()
print(empty)  # -> set()
print(type(empty))  # -> <class 'set'>

print()

# === イテラブルオブジェクトを set型へ変換 ===

# --- リスト ---

lst = [1, 2, 2, 3, 1, 4]
s_l = set(lst)
print(s_l)  # -> {1, 2, 3, 4}
print(type(s_l))  # -> <class 'set'>
print()

# --- 辞書 ---

dict = {1: 'a', 2: 'b', 3: 'c', }
s_d = set(dict)
print(s_d)  # -> {1, 2, 3}
print(type(s_d))  # -> <class 'set'>
print()

# --- 文字列 ---

s_s = set('abracadabra')
print(s_s)  # -> {'a', 'r', 'd', 'b', 'c'}
print(type(s_s))  # -> <class 'set'>
print()

# === 集合内包表記 ===

print({x for x in range(10) if x % 2 == 0})  # -> {0, 2, 4, 6, 8}
print()

# === 集合生成時注意点 ===

"""
・異なる型を要素として持つこともできる
・リスト型のような更新可能なオブジェクトは登録できない
"""
s = {1.23, '百', (0, 1, 2), '百'}
print(s)  # -> {(0, 1, 2), 1.23, '百'}
try:
    print({[0, 1, 2]})
except TypeError as e:
    print(e)  # -> unhashable type: 'list'
print()

"""
int や float のように異なる型でも
値が等価であれば重複していると見なされる
"""
s = {100, 100.0, 0, 0.0, False}
print(s)  # -> {0, 100}
print()

# ****** 集合演算 ******

"""
・メソッドには複数の引数を指定可能
・set型だけでなく、set() でset型に変換できるリストやタプルなども引数に指定可能
"""

# === 演算結果を取得 ===

# --- 和集合（合併、ユニオン）: ---
# '|'演算子, set.union(*args)
# args=set|seq

s1 = {0, 1, 2}
s2 = {1, 2, 3}
s3 = {2, 3, 4}

print(s1 | s2)  # -> {0, 1, 2, 3}
print(s1.union(s2))  # -> {0, 1, 2, 3}
print(s1.union(s2, s3))  # -> {0, 1, 2, 3, 4}
print(s1.union(s2, [5, 6, 5, 7, 5]))  # -> {0, 1, 2, 3, 5, 6, 7}
print(s1.union(s2, 'abc'))  # -> {0, 1, 2, 3, 'b', 'c', 'a'}
print()

# --- 積集合（共通部分、交差、インターセクション）: ---
# '&'演算子, intersection()

s1 = {0, 1, 2, 'a', 'b', 'c'}
s2 = {1, 2, 3, 'b', 'c', 'd'}
s3 = {2, 3, 4, 'c', 'd', 'e'}

print(s1 & s2)  # -> {'c', 1, 2, 'b'}
print(s1.intersection(s2))  # -> {'c', 1, 2, 'b'}
print(s1.intersection(s2, s3))  # -> {'c', 2}
print(s1.intersection(s2, [1, 2, 3, 4]))  # -> {1, 2}
print(s1.intersection(s2, 'abc'))  # -> {'c', 'b'}
print()

# --- 差集合: ---
# '-'演算子, difference()

s1 = {0, 1, 2}
s2 = {2, 3, 4}
s3 = {0, 5, 6}

print(s1 - s2)  # -> {0, 1}
print(s1.difference(s2))  # -> {0, 1}
print(s1.difference(s2, s3))  # -> {1}
print()

# --- 対称差集合（どちらか一方にだけ含まれる要素の集合）: ---
# '^'演算子, symmetric_difference()

s1 = {0, 1, 2}
s2 = {1, 2, 3}

print(s1 ^ s2)  # -> {0, 3}
print(s1.symmetric_difference(s2))  # -> {0, 3}
print()

# === 集合比較 ===

# --- 部分集合か判定 ---

s1 = {0, 1}
s2 = {0, 1, 2, 3}
s3 = {1, 2, 3, 4}

# 等価な集合に対してもTrueを返す:
# '<='演算子, set.issubset(set)

print(s1 <= s2)  # -> True
print(s1 <= s3)  # -> False
print(s1 <= s1)  # -> True

print(s1.issubset(s2))  # -> True
print()

# 等価な集合に対してはFalseを返す（新部分集合）:
# '<'演算子

print(s1 < s2)  # -> True
print(s1 < s3)  # -> False
print(s1 < s1)  # -> False
print()

# --- 上位集合か判定 ---

s1 = {0, 1, 2, 3}
s2 = {0, 1}
s3 = {1, 2, 3, 4}

# 等価な集合に対してもTrueを返す:
# '>='演算子, set.issuperset(set)

print(s1 >= s2)  # -> True
print(s1 >= s3)  # -> False
print(s1 >= s1)  # -> True
print(s1 >= s1)  # -> True

print(s1.issubset(s2))  # -> False
print()

# 等価な集合に対してはFalseを返す（新上位集合）:
# '>'演算子

print(s1 > s2)  # -> True
print(s1 > s3)  # -> False
print(s1 > s1)  # -> False
print()

# --- 互いに素か判定: ---
# set.isdisjoint(set)

s1 = {0, 1}
s2 = {1, 2}
s3 = {2, 3}

print(s1.isdisjoint(s2))  # -> False
print(s1.isdisjoint(s3))  # -> True
