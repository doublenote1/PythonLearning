# ****** 辞書作成 ******

# === 辞書リテラル ===

a, b = 3, 4
d = {'string': '文字列', 1: '数値',
     (1,): 'タプル', frozenset([1]): 'フローズンセット',
     (lambda x: x ** 2)(a): '関数', a: '変数', a * b: '式'}
print(d)

'''
key に使えるのは immutable なオブジェクトだけ
key として使えるもの: int, str, tuple, frozenset

関数、変数、式の場合は、戻り値、値、評価が immutable かどうか
'''

# === dict 関数 ===

'''キーと値のペアのタプル(リスト・セット)を含むリストから辞書を生成'''

d = dict([('string', '文字列'), (1, '数値'), ((1,), 'タプル')])
print(d)

# --- キーが文字列の場合、キーワード引数を使って定義可能 ---

d = dict(one=1, two=2, three=3)
print(d)

# --- zip 関数を併用 ---

keys = ['zip1', 'zip2', 'zip3']
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)

# --- 辞書のコピー ---

d1 = {1: 1, 2: 2, 3: 3}
d2 = d1
d3 = dict(d1)
print(d1, id(d1))
print(d2, id(d2))
print(d3, id(d3))

print()

# === 辞書内包表現 ===

d = {x: x ** 2 for x in (2, 4, 6)}
print(d)

# zip 関数を併用
keys = ['zip1', 'zip2', 'zip3']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
print(d)

print()

# === ※ 辞書作成時挙動 ===

# 同じキーを指定した場合は上書きされる
d = {'k1': 1, 'k2': 2, 'k3': 3, 'k3': 300}
print(d)

print()

# ****** 要素へ アクセス・追加・更新・削除******

d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, '四': 4}
print(d)
print()

# === キーの値にアクセス ===

# 存在しなければエラー
print(d['three'])

# 存在しなければ、任意の値を返す(デフォルト: None)
print(d.get('three'))
print(d.get('ten'))
print(d.get('ten', '見当たらず'))
print()

# === キーの追加・変更 ===

# --- 1: dict[key] = value ---

# キーが存在しなければ追加
d['five'] = 5
print(d)

# キーが存在すれば更新
d['one'] = '①'
print(d)

print()

# --- 2: dict.setdefault(key, [value]) ---

# キーが存在しなければキーと値(省略時は None)を追加し、その値を返す
print(d.setdefault('six', 6))
print(d)
print(d.setdefault('seven'))
print(d)

# キーが存在すれば変更せず、そのキーに対する元々の値を返す
print(d.setdefault('seven', 7))
print(d)

print()

# === 要素の削除 ===

# del: 単一要素
del d['one'], d['two']
print(d)

# pop: キーを指定し、要素を一つ取り出し
print(d.pop('three'))
print(d)
print(d.pop('ten', None))
print(d)

# popitem: ランダムに要素を一つ取り出し
print(d.popitem())
print(d)

# clear: 要素全体
d.clear()
print(d)

print()

