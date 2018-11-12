# ****** 破壊的メソッド ******

lst = [1, 2, 3, 4]

# === 追加・挿入・結合 ===

# 追加
lst.append('appended')
print(lst)

# 挿入
lst.insert(2, 'inserted')
print(lst)

# 結合
lst.extend(['1', '2'])
print(lst)
lst += ['1', '2']
print(lst)
print()

# === 削除 ===

# 指定した値と同じの、最初の要素を削除
lst.remove('inserted')
lst.remove('appended')
print(lst)

# 一文字取出し
print(lst.pop())
print(lst)
print(lst.pop(2))
print(lst)
print(lst.pop(-2))
print(lst)

# 全ての要素を削除
lst.clear()
print(lst)
print()

# === 並び替え ===

# sort
lst = [5, 1, 9, 2, 4]
lst.sort()
print(lst)

# reverse
lst.reverse()
print(lst)
print()

# ****** 非破壊的メソッド・関数 ******

lst = [3, 4, 1, 2, 3, 6, 3, 3]

# === 結合 ===

print(lst + ['test', 'sample'])

# === 情報取得 ===

# index
print(lst.index(1))

# count
print(lst.count(3))
print()

# max
print(max(lst))

# min
print(min(lst))

# sum
print(sum(lst))

# len
print(len(lst))

# 平均値
print(sum(lst) / len(lst))

# === 並べ替え ===

# sorted
print(sorted(lst))

# reversed
print(list(reversed(lst)))
