# === set・frozenset の生成 ===

s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(s)
print(type(s))
print()

"""
・異なる型を要素として持つこともできる
・リスト型のような更新可能なオブジェクトは登録できない
"""
print({1.23, '百', (0, 1, 2), '百'})
try:
    print({[0, 1, 2]})
except TypeError as e:
    print('{[0, 1, 2]} =>', e)

"""
int や float のように異なる型でも
値が等価であれば重複していると見なされる
"""
print({100, 100.0, 0, False})
print()

"""イテラブルオブジェクトを set型へ変換"""
lst = [1, 2, 2, 3, 1, 4]
s_l = set(lst)
print(s_l)
print(type(s_l))

"""
空の波括弧 {} は辞書型 dict と見なされるため、
空の set型オブジェクト（空集合）を生成するには
set() コンストラクタを使う
"""
empty = {}
print(empty)
print(type(empty))

empty = set()
print(empty)
print(type(empty))

print()

"""イミュータブルな frozenset の生成"""
fs_l = frozenset(lst)
print(fs_l)
print(type(fs_l))
print()

"""集合内包表記"""
print({x for x in 'abracadabra' if x not in 'abc'})
print()

# === set型のメソッド ===



"""文字列を set型へ変換"""
a = set('abracadabra')
b = set('alacazam')
print(a)

print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

