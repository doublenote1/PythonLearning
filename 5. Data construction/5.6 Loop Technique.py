# key と value に同時に取り出し可能
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# index と 要素 に同時に取り出し可能
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 二つまたはそれ以上のシーケンス型を同時にループして要素を取り出し可能
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# シーケンスを逆方向に渡ってループ
for i in reversed(range(1, 10, 2)):
    print(i)

# シーケンスをソートされた順序でループ
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

import math

# todo: 新しいリストを作る
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)
