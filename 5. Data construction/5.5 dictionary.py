tel = {'jack': 4098, 'sape': 4139}

# key が存在しなければ追加
tel['guido'] = 4127
print(tel)  # -> {'jack': 4098, 'sape': 4139, 'guido': 4127}

# key が存在すれば更新
tel['jack'] = 1111
print(tel)  # -> {'jack': 1111, 'sape': 4139, 'guido': 4127}

# key の値にアクセス
print(tel['jack'])  # -> 1111

del tel['sape']
tel['irv'] = 4127
print(tel)  # -> {'jack': 1111, 'guido': 4127, 'irv': 4127}

print(tel.keys())  # -> dict_keys(['jack', 'guido', 'irv'])
print(list(tel.keys()))  # -> ['jack', 'guido', 'irv']
print(sorted(tel.keys()))  # -> ['guido', 'irv', 'jack']

# キーの存在確認
print('guido' in tel)  # -> True
print('jack' not in tel)  # -> False

# キーと値のペアのタプルを含むリストから辞書を生成
print(dict([('a', 1), ('b', 2), ('c', 3)]))  # -> {'a': 1, 'b': 2, 'c': 3}
# キーが文字列の場合、キーワード引数を使って定義可能
print(dict(a=1, b=2, c=3))  # -> # -> {'a': 1, 'b': 2, 'c': 3}

# 辞書内包表現
print({x: x ** 2 for x in (2, 4, 6)})  # -> {2: 4, 4: 16, 6: 36}
