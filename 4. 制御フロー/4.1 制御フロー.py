# === if ===
def if_use(x):
    if x < 0:
        x = str(x) + ' -> 0'
        msg = 'Negative changed to zero'
    elif x == 0:
        msg = 'Zero'
    elif x == 1:
        msg = 'Single'
    else:
        msg = 'More'
    print(x, ': ', msg, sep='')

if_use(-5)
if_use(0)
if_use(1)
if_use(20)
print()

# === for ===

words = ['cat', 'window', 'defenestrate']
for word in words:
    print(word, len(word), sep=': ', end=' | ')
print()

# ループ内部でイテレートしているシーケンスを修正する場合、
# シーケンスのコピーをイテレートする様にする
for word in words[:]:
    if len(word) > 6:
        words.insert(0, word)
print(words)
print()

# break / else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:  # 最後まで break されなかった場合実行
        print(n, 'is a prime number')
print()

# continue
for num in range(2, 10):
    if num % 2 == 0:
        print(num, ': 偶数', sep='', end=' | ')
        continue
    print(num, ': 奇数', sep='', end=' | ')
print()
print()

# === range() ===

for i in range(5):
    print(i, end=', ')
print()

print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))
print()

# シーケンスのインデックスを取得

list = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(list)):
    print(i, ': ', list[i], sep='', end=' | ')
print()

enum_list = enumerate(list)
for i in enum_list:
    print(i[0], ': ', i[1], sep='', end=' | ')
print()
print()
