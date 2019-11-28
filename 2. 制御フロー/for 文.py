# === 基本 ===

'''
for 変数名 in イテラブルオブジェクト:
    処理
'''

names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print(name, end=', ')
print()
print()

# === for 文制御(break,continue,else) ===

names = ['Alice', 'Bob', 'Charlie', 'Ellen', 'Michael']

def display_names(c=None, b=None):
    for name in names:
        if name == c:
            print('!!SKIP!!')
            continue
        if name == b:
            print('!!BREAK!!')
            break
        print(name)
    else:  # 最後まで break されなかった場合実行
        print('!!FINISH!!')
    print()

display_names('Bob', 'Ellen')
display_names('Alice')

# === インデックス ===

# --- インデックスで回す(range) ---

for i in range(5):
    print(i, end=', ')
print()

print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))
print()

# --- シーケンスのインデックスを取得: ---
# range(stop)
# range(start, stop[, step])
# enumerate(iterable, start=0)

names = ['Alice', 'Bob', 'Charlie']

for i in range(len(names)):
    print(i + 1, ': ', names[i], sep='', end=', ')
print()
for tpl in enumerate(names, 1):
    print(tpl[0], ': ', tpl[1], sep='', end=', ')
print()
for i, name in enumerate(names, 1):
    print(i, ': ', name, sep='', end=', ')
print()
print()

# === 複数リストの要素取得(zip, enumerate) ===

names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]
points = [100, 85, 90]

for i, (name, age, point) in enumerate(zip(names, ages, points), 1):
    print(i, ': ', name, ': ', 'age:', age, ', point:', point, sep='')
print()

# === シーケンスをソートされた順序でループ ===

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
print()

# === 逆順 ===

names = ['Alice', 'Bob', 'Charlie']

for name in reversed(names):
    print(name, end=', ')
print()

for i in reversed(range(3)):
    print(i, end=', ')
print()

# enumerate オブジェクトはリスト化が必要
for i, name in reversed(list(enumerate(names, 1))):
    print(i, ': ', name, sep='', end=', ')
print()

# enumerate オブジェクトのインデックスは逆転したくない場合
for i, name in enumerate(reversed(names), 1):
    print(i, ': ', name, sep='', end=', ')
print()
print()

# zip オブジェクトはリスト化が必要
nums = [2, 8, 10, 16]
strings = ['binary', 'octal', 'decimal', 'hex']
for num, string in reversed(list(zip(nums, strings))):
    print(num, ': ', string, sep='')
print()

# === 多重ループ・抜け出し方 ===

l1 = [1, 2, 3]
l2 = [10, 20, 30]
l3 = [100, 200, 300]

# --- else, continue を使って抜ける---

x = 0
for i in l1:
    for j in l2:
        for k in l3:
            x += i + j + k
            if i == 2 and j == 20 and k == 200:
                break
        else:
            continue
        break
    else:
        continue
    break
print(x)

# --- フラグ変数を使って抜ける---

x = 0
flag = False
for i in l1:
    for j in l2:
        for k in l3:
            x += i + j + k
            if i == 2 and j == 20 and k == 200:
                flag = True
                break
        if flag:
            break
    if flag:
        break
print(x)

import itertools

x = 0
for i, j, k in itertools.product(l1, l2, l3):
    x += i + j + k
    if i == 2 and j == 20 and k == 200:
        break
print(x)
print()

# === 辞書オブジェクトの for ループ ===

d = {'key1': 1, 'key2': 2, 'key3': 3}

for k in d:
    print(k, end=', ')
print()

for v in d.values():
    print(v, end=', ')
print()

for k, v in d.items():
    print(k, v, sep=' = ', end=', ')
print()

for t in d.items():
    print(t[0], t[1], sep=' = ', end=', ')
print()

