# ****** 「キー」、「値」 のリストを取得 ******

d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, '四': 4}

# キーの一覧

print(d.keys())
print(list(d.keys()))
print()

# 値の一覧

print(d.values())
print(list(d.values()))
print()

# キーと値の組み合わせの一覧

print(d.items())
print(list(d.items()))
print()

# ****** 複数辞書の結合・集合演算 ******

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4, 'd': 5}

# === 結合 ===

'''引数は dict が使うものを使える'''

d1.update(d2)
print(d1)
print()

# === 集合演算 ===

# --- 共通部分 ---

# 共通のキー

keys = d1.keys() & d2.keys()
print(keys)
print(type(keys))

# 共通のキーと値の組み合わせ

items = d1.items() & d2.items()
print(items)
print(type(items))
print(dict(items))
print(type(dict(items)))
print()

# --- 和集合 ---

# すべてのキー

keys = d1.keys() | d2.keys()
print(keys)

# すべてのキーと値の組み合わせ

items = d1.items() | d2.items()
print(items)
'''辞書にすると、値が別でキーが共通の要素はどちらかが上書きされる'''
print(dict(items))
print()

# --- 対象差集合 ---

# 共通でないキー

keys = d1.keys() ^ d2.keys()
print(keys)

# 共通でないキーと値の組み合わせ

items = d1.items() ^ d2.items()
print(items)
'''辞書にすると、値が別でキーが共通の要素はどちらかが上書きされる'''
print(dict(items))
print()

# --- 差集合 ---

# 一方にのみ含まれるキー

keys = d1.keys() - d2.keys()
print(keys)

# 一方にのみ含まれるキーと値の組み合わせ

items = d1.items() - d2.items()
print(items)
print(dict(items))
print()

# === 存在確認 ===

d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, '四': 4}

# キーの存在確認

print('one' in d)
print('one' not in d)

# 値の存在確認

print(1 in d.values())
print(1 not in d.values())

# キーと値の組み合わせの存在確認

print(('three', 3) in d.items())
print(('five', 5) in d.items())

print()

# === 最大値・最小値 ===

d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, '四': 4}

# --- キー ---

print(max(d))
print(min(d))

# --- 値 ---

print(max(d.values()))
print(min(d.values()))

# --- 値の 最大値・最小値に対応するキー ---

print(max(d, key=d.get))
print(min(d, key=d.get))

# --- キーの 最大値・最小値に対応する値 ---

print(d[max(d)])
print(d[min(d)])

# --- キーと値を同時取得 ---

# キーを基準にして
print(max(d.items(), key=lambda x: x[0]))
print(min(d.items(), key=lambda x: x[0]))

# 値を基準にして
print(max(d.items(), key=lambda x: x[1]))
print(min(d.items(), key=lambda x: x[1]))

# --- 最大・最小となる値が複数存在する場合、リストで取得 ---

# キーのリスト取得
print([kv[0] for kv in d.items() if kv[1] == max(d.values())])

# キーと値を同時取得
print([kv for kv in d.items() if kv[1] == max(d.values())])

# === 値からキーを抽出 ===

print([k for k, v in d.items() if v == 4])
print([k for k, v in d.items() if v == 1])
print([k for k, v in d.items() if v == 5])
print()

# === キーと値を入れ替え ===

d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, '四': 4}

'''
値がキーになった時、そのキーが複数存在すれば、
最も後発の要素により、その他の同一キーの要素は上書きされる
'''

print({v: k for k, v in d.items()})
print()

# === 共通のキーを持つ辞書を要素とするリストに対する操作 ===

dict_list = [{'Name': 'Alice', 'Age': 40, 'Point': 70},
             {'Name': 'Bob', 'Age': 20},
             {'Name': 'Charlie', 'Age': 30, 'Point': 80}]

# --- 特定のキーの値のリストを取得 ---

l_name = [d.get('Name') for d in dict_list]
print(l_name)

l_age = [d.get('Age') for d in dict_list]
print(l_age)

l_point = [d.get('Point') for d in dict_list]
print(l_point)
print()

# --- 特定のキーの値に従ってソート ---

'''sort()メソッドも利用可能'''

from pprint import pprint

s_age = sorted(dict_list, key=lambda x: x.get('Age'))
pprint(s_age)
print()

s_name = sorted(dict_list, key=lambda x: x.get('Name'))
pprint(s_name)
print()

'''
指定キーが存在しない要素は
第二引数に指定した値に置き換えられてソートされる
'''

s_point = sorted(dict_list, key=lambda x: x.get('Point', 0))
pprint(s_point)
print()

s_point = sorted(dict_list, key=lambda x: x.get('Point', 100))
pprint(s_point)
print()
