# === キーに要素、値に出現回数の形のデータを持った辞書型のオブジェクトを返す: ===
# collections.Counter()

import collections

lst = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
c = collections.Counter(lst)
print(c)  # -> Counter({'a': 4, 'c': 2, 'b': 1})
print(type(c))  # -> <class 'collections.Counter'>
print(issubclass(type(c), dict))  # -> True
print()

print(c['a'])  # -> 4
print(c['b'])  # -> 1
print(c['c'])  # -> 2
print(c['d'])  # -> 0
print()

print(c.keys())  # -> dict_keys(['a', 'b', 'c'])
print(c.values())  # -> dict_values([4, 1, 2])
print(c.items())  # -> dict_items([('a', 4), ('b', 1), ('c', 2)])
print()

# === 出現回数順に要素を取得: ===
# collections.Counter(lst).most_common([n])
# n=出現回数の多いn要素のみ返す

"""
・(要素, 出現回数)という形のタプルを出現回数順に並べたリストを返す
・出現回数が最も多いものは[0]、最も少ないものは[-1]のように
  インデックスを指定して取得できる
・要素だけ、出現回数だけを取得したい場合はさらにインデックスを指定する

"""

import collections

lst = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
c = collections.Counter(lst)

print(c.most_common())  # -> [('a', 4), ('c', 2), ('b', 1)]
print(c.most_common()[0])  # -> ('a', 4)
print(c.most_common()[-1])  # -> ('b', 1)
print(c.most_common()[0][0])  # -> a
print(c.most_common()[0][1])  # -> 4
print()

"""出現回数の少ない順に並べ替えたい場合は増分を-1としたスライスを使う"""
print(c.most_common()[::-1])  # -> [('b', 1), ('c', 2), ('a', 4)]
print()

"""
・引数 n を指定すると、出現回数の多い n 要素のみを返す
・省略するとすべての要素
"""
print(c.most_common(2))  # -> [('a', 4), ('c', 2)]
print()

"""
(要素, 出現回数)のタプルではなく、
出現回数順に並べた要素・出現回数のリストが個別に欲しい場合は、
以下のようにして分解できる。
"""
values, counts = zip(*c.most_common())
print(values)  # -> ('a', 'c', 'b')
print(counts)  # -> (4, 2, 1)
print()

# === 重複しない要素（一意な要素）の個数（種類）をカウント ===

lst = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
print(len(collections.Counter(lst)))  # -> 3
print(len(set(lst)))  # -> 3
print()

# === 条件を満たす要素の個数をカウント ===

# --- 数値のリストに対して ---

lst = list(range(-5, 6))
print(lst)  # -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# 0 以下
print([i for i in lst if i < 0])  # -> [-5, -4, -3, -2, -1]
print(len([i for i in lst if i < 0]))  # -> 5

# 奇数
print([i for i in lst if i % 2 == 1])  # -> [-5, -3, -1, 1, 3, 5]
print(len([i for i in lst if i % 2 == 1]))  # -> 6
print()

# --- 文字列のリストに対して ---

lst = ['apple', 'orange', 'banana']
print(lst)  # -> ['apple', 'orange', 'banana']

print([s for s in lst if s.endswith('e')])  # -> ['apple', 'orange']
print(len([s for s in lst if s.endswith('e')]))  # -> 2
print()

# --- 出現回数を条件にして ---

lst = ['a', 'a', 'a', 'a', 'b', 'c', 'c']
print(lst)  # -> ['a', 'a', 'a', 'a', 'b', 'c', 'c']

# 出現回数が 2 以上の要素の総数
print([i for i in lst if lst.count(i) >= 2])
# -> ['a', 'a', 'a', 'a', 'c', 'c']
print(len([i for i in lst if lst.count(i) >= 2]))  # -> 6

# 出現回数が 2 以上の要素の種類の数
c = collections.Counter(lst)
print([i[0] for i in c.items() if i[1] >= 2])  # -> ['a', 'c']
print(len([i[0] for i in c.items() if i[1] >= 2]))  # -> 2
print()

# --- 文字列の単語の出現個数をカウント ---

"""
・不必要な ',' や '.' をreplace() メソッドで空文字列と置換し、削除する
・さらに split() メソッドで空白で区切ってリスト化する

・リスト化できれば、各単語の出現回数や出現する単語の種類を取得したり、
  collections.Counter の most_common() で最も出現回数の多い単語を取得したりできる
"""

text = 'government of the people, by the people, for the people.'

text_remove = text.replace(',', '').replace('.', '')
print(text_remove)
# -> government of the people by the people for the people

word_list = text_remove.split()
print(word_list)
# -> ['government', 'of', 'the', 'people', 'by', 'the', 'people', 'for', 'the', 'people']

print(word_list.count('people'))  # -> 3
print(len(set(word_list)))  # -> 6

c = collections.Counter(word_list)
print(c)
# -> Counter({'the': 3, 'people': 3, 'government': 1, 'of': 1, 'by': 1, 'for': 1})
print(c.most_common()[0][0])  # -> the
print()

"""
・日本語のテキストの場合は単語の区切りがはっきりしていないので spilit() では分割できない
・Janome というライブラリを使うと実現可能
"""

# --- 文字列の文字の出現個数をカウント ---

text = 'supercalifragilisticexpialidocious'
c = collections.Counter(text)
print(c.most_common(5))
# -> [('i', 7), ('s', 3), ('c', 3), ('a', 3), ('l', 3)]
values, counts = zip(*c.most_common(5))
print(values)  # -> ('i', 's', 'c', 'a', 'l')
