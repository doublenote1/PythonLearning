# === 関数定義基本 ===

# --- return 文無 ---

def print_fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    print(result)

x = print_fib(100)
print(x)  # return 文を持たないので None を返す
print()

# --- return 文有 ---

def return_fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
print()

x = return_fib(100)  # return した値を返す
print(x)  # -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# --- 関数の代入 ---

def sample():
    print('sample')
f = sample
f()
print()

# --- 複数の戻り値を返す ---

'''
Pythonにおいて、構文上必要な場合を除き、
カンマで区切られた値は丸括弧を省略したタプルとみなされる。
このため、上の例の関数はそれぞれの値を要素とするタプルを返すことになる。
'''

def return_two_results_as_tuple():
    return 1, 'string'

results = return_two_results_as_tuple()
print(results)
print(type(results))

def return_two_results_as_list():
    return [1, 'string']

results = return_two_results_as_list()
print(results)
print(type(results))
print()

# ****** 仮引数の種類 ******

'''
1. 位置引数
2. デフォルト引数
3. 可変長位置引数
4. 可変長キーワード引数
5. キーワード専用引数
'''

# === 位置引数・デフォルト引数 ===

'''
デフォルト引数が設定された引数は省略可能

デフォルト引数は位置引数の前に置けない
'''

def calc(price, num, tax=1.08, currency='円'):
    x = str(round(price * num * tax)) + currency
    print(x)

calc(180, 3)
calc(180, 3, 1.05)
calc(180, 3, 1.05, 'ドル')
print()
calc(180, 3, tax=1.05)
calc(180, 3, tax=1.05, currency='ドル')
calc(180, 3, currency='ドル')
print()
calc(price=180, num=3)
calc(price=180, num=3, tax=1.05)
calc(price=180, num=3, currency='ドル')
calc(price=180, num=3, tax=1.05, currency='ドル')
print()

# === デフォルト値の初期化 ===

# デフォルト値は関数が定義された時点で初期化

i = 5

def f(arg=i):
    print(arg)

i = 6
f()  # -> 5

# デフォルト値は関数定義時に一度しか初期化されない

def f(a, lst=[]):
    lst.append(a)
    return lst

print(f(1), end=' -> ')  # -> [1]
print(f(2), end=' -> ')  # -> [1, 2]
print(f(3))  # -> [1, 2, 3]

# リスト・辞書・関数などの変更可能なデフォルト値を
# 呼び出しごとに初期化したい場合

def f(a, lst=None):
    if lst is None:
        lst = []
    lst.append(a)
    return lst

print(f(1), end=' -> ')  # -> [1]
print(f(2), end=' -> ')  # -> [2]
print(f(3))  # -> [3]
print()

# === 可変長位置引数・可変長キーワード引数 ===

'''可変長引数は０個以上いくつでも設定可能'''

def man(name, *favorites, **others):
    size = 9

    str_favorites = ''
    for favorite in favorites:
        str_favorites += favorite + ', '
    str_favorites = str_favorites.rstrip(', ') + '\n'

    for key in others:
        if len(key) > size:
            size = len(key)

    if others:
        str_attributes = []
        for key in others:
            str_attributes.append(
                (key + ':').ljust(size + 2) + str(others[key]))
        other_attributes = '\n'.join(str_attributes) + '\n'
    else:
        other_attributes = ''

    orig_string = ('name:'.ljust(size + 2) + name + '\n'
                   + 'favorites:'.ljust(size + 2) + str_favorites
                   + other_attributes)
    print(orig_string)

man('近藤', 'みっちゃ', 'PC', 'anime', height=169, weight=60, job='opperator')
man('みっちゃ', height=160, weight=45, job='給食係')
man('節子')

# === キーワード専用引数 ====

'''
可変長位置引数以降に設定された仮引数へは、
キーワード引数でしか設定できない

デフォルト値を指定しなければ、設定必須
'''

# --- 可変長位置引数がある場合 ---

def concat(*elm, kind, sep='/'):
    return kind + ': ' + sep.join(elm)

print(concat('C:', 'Users', 'Kiyo', kind='path'))
print(concat('orange', 'apple', 'lemon', kind='fruits', sep=', '))

# <kind> は必須のキーワード引数
try:
    print(concat('cat', 'dog', 'bunny', sep=', '))
except TypeError as e:
    print(e)

# --- 可変長位置引数がない場合 ---

def sample(elm1, elm2, *, kind, sep='/'):
    return kind + ': ' + sep.join([elm1, elm2])

print(sample('word1', 'word2', kind='birds', sep=', '))
print()

# === 引数のアンパック ===

from datetime import datetime

print(datetime(*[1988, 5, 22, 0, 45, 30, 309309]))
print(datetime(**{'year': 1988, 'month': 5, 'day': 22,
                  'hour': 0, 'minute': 45,
                  'second': 30, 'microsecond': 309309}))
print(datetime(1988, *[5, 22], minute=45,
               **{'second': 30, 'microsecond': 309309}))
print(datetime(1988, *[5, 22], **{'second': 30, 'microsecond': 309309},
               minute=45, hour=0))
print()

