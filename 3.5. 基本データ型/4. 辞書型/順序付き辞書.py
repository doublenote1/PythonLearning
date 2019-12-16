# === 順序付き辞書 ===

from collections import OrderedDict

# --- 作成 ---

od = OrderedDict()
od['k1'] = 1
od['k2'] = 2
od['k3'] = 3
print(od)

print(OrderedDict(k1=1, k2=2, k3=3))
print(OrderedDict([('k1', 1), ('k2', 2), ('k3', 3)]))
print(OrderedDict((['k1', 1], ['k2', 2], ['k3', 3])))
print()

# --- 辞書に対するものと同じ操作が可能 ---

print(od['k1'])

od['k2'] = 200
print(od)

od.update(k4=4, k5=5)
print(od)

del od['k4'], od['k5']
print(od)

print()

# --- 要素を先頭・末尾に移動 ---

# 先頭へ
od.move_to_end('k1')
print(od)

# 末尾へ
od.move_to_end('k1', False)
print(od)

print()

# --- 任意の位置に新たな要素を追加 ---

lst = list(od.items())
lst.insert(1, ('kx', -1))
od = OrderedDict(lst)
print(od)
print()

# --- 要素を交換 ---

# インデックス指定

lst = list(od.items())
lst[0], lst[2] = lst[2], lst[0]
od = OrderedDict(lst)
print(od)
print()

# キー指定

lst = list(od.items())
k = list(od.keys())
lst[k.index('kx')], lst[k.index('k3')] = lst[k.index('k3')], lst[k.index('kx')]
od = OrderedDict(lst)
print(od)
print()

# --- 要素をキーまたは値でソート ---

od_sorted_key = OrderedDict(
    sorted(od.items(), key=lambda x: x[0])
)
print(od_sorted_key)

od_sorted_value = OrderedDict(
    sorted(od.items(), key=lambda x: x[1], reverse=True)
)
print(od_sorted_value)
