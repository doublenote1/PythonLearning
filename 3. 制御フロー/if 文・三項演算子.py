# === if 文 ===

def if_use(x):
    if x < 0:
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

# === 三項演算子 ===

'''
<条件式が真の時に返す値> if <条件式> else <条件式が偽の時に返す値>
<条件式が真の時に評価される式> if <条件式> else <条件式が偽の時に評価される式>
'''

# --- if... else 文 ---

def even_or_odd(num):
    if num % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    print(num, '=', result)

even_or_odd(1)
even_or_odd(2)

# --- 三項演算子(値を返す) ---

def even_or_odd_with_ternary(num):
    result = 'even' if num % 2 == 0 else 'odd'
    print(num, '=', result)

even_or_odd_with_ternary(1)
even_or_odd_with_ternary(2)

# --- 三項演算子(式を評価) ---

def print_even_or_odd_with_ternary(num):
    print(num, ' = ', sep='', end='')
    print('even') if num % 2 == 0 else print('odd')

print_even_or_odd_with_ternary(1)
print_even_or_odd_with_ternary(2)
print()

# --- if... elif... else 文を一行で記述 ---

def nega_posi_zero(num):
    return 'negative' if num < 0 else 'positive' if num > 0 else 'zero'

print(nega_posi_zero(2))
print(nega_posi_zero(-2))
print(nega_posi_zero(0.0))
print()

# === リスト内包表記と三項演算子の組み合わせ ===

l = ['even' if i % 2 == 0 else i for i in range(10)]
print(l)
l = [i * 10 if i % 2 == 0 else i for i in range(10)]
print(l)
