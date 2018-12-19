# ****** 重複した要素を削除し、新たなリストを生成 ******

lst = [3, 3, 2, 1, 5, 1, 4, 2, 3]
print(lst)
print()

# === 元のリストの順序を保持しない ===

print(list(set(lst)))
print()

# === 元のリストの順序を保持する ===

# dict.fromkeys(seq[, value])
# value=None
"""辞書のキーは重複した要素をもたない"""
print(dict.fromkeys(lst))
print(dict.fromkeys(lst, 'test'))
print(list(dict.fromkeys(lst)))
print()

# sorted(set(list), key=list.index)
print(sorted(set(lst), key=lst.index))
print()

# === 二次元配列（リストのリスト）の場合 ===

l_2d = [[0], [2], [2], [1], [0], [0]]
print(l_2d)
print()

"""
二次元配列（リストのリスト）の場合、set() やdict.fromkey() を使う方法はエラー TypeError になる
これは、リストなどのミュータブル（更新可能）なオブジェクトは set型の要素や dict型のキーにできないから。
"""

try:
    l_2d_unique = list(set(l_2d))
except TypeError as e:
    print(e)

try:
    l_2d_unique_order = dict.fromkeys(l_2d)
except TypeError as e:
    print(e)
print()

# 関数で解決

"""
元のリストの順番は保持され、
一次元のリストやタプルに対しても動作する
"""

def get_unique_list(seq):
    seen = []
    """
    ・ and 演算子のショートサーキット（短絡評価）で
       X and Y の X が False であれば Y は評価されない（実行されない）
    ・ append() メソッドが None を返す
    """
    return [x for x in seq if x not in seen and not seen.append(x)]

print(get_unique_list(l_2d))
print(get_unique_list(lst))
print()

# ****** 重複した要素を抽出し、新たなリストを生成 ******

lst = [3, 3, 2, 1, 5, 1, 4, 2, 3]
print(lst)
print()

# === 元のリストの順序を保持しない ===

print([x for x in set(lst) if lst.count(x) > 1])
print()

# === 元のリストの順序を保持する ===

print([x for x in dict.fromkeys(lst) if lst.count(x) > 1])
print(sorted([x for x in set(lst) if lst.count(x) > 1], key=lst.index))
print()

# === 二次元配列（リストのリスト）の場合 ===

l_2d = [[0], [2], [2], [1], [0], [0]]
print(l_2d)
print()

# --- 順番を保持しない ---

def get_duplicate_list(seq):
    seen = []
    return [x for x in seq if not seen.append(x) and seen.count(x) == 2]

print(get_duplicate_list(l_2d))
print(get_duplicate_list(lst))
print()

# --- 順番を保持する ---

def get_duplicate_list_order(seq):
    seen = []
    return [x for x in seq if seq.count(x) > 1 and not seen.append(x) and seen.count(x) == 1]

print(get_duplicate_list_order(l_2d))
print(get_duplicate_list_order(lst))
