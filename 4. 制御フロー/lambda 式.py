# === lambda 式の基本 ====

# --- lambda 式 = (lambda <仮引数>: <仮引数を含む式>)(<実引数>) ---

print((lambda a, b=1: a + b)(2, 3))  # -> 5

# --- 上記を関数定義すると ---

def func_add(a, b=1):
    return a + b
print(func_add(2, 3))  # -> 5

# --- 三項演算子を使用可能 ---

print((lambda x: 'even' if x % 2 == 0 else 'odd')(9))  # -> odd

# --- lambda を使って関数を返す ---

def make_incrementor(n):
    return lambda x: x + n

func_add_one = make_incrementor(1)
func_add_two = make_incrementor(2)
print(func_add_one(10), func_add_one(100))  # -> 11 101
print(func_add_two(10), func_add_two(100))  # -> 12 102
print()

# === 他の関数の式オブジェクトが入る所で利用 ===

# --- sorted(), max(), min() と lambda ---

# sorted(iterable, key=None, reverse=False)
# key 関数に、iterable の値を引数とする関数を設定し、
# その戻り値を元に最終的にソートする

lst = ['Carl', 'Bob', 'Alice']

print(sorted(lst))  # -> ['Alice', 'Bob', 'Carl']
print(sorted(lst, key=len))  # -> ['Bob', 'Carl', 'Alice']
print(sorted(lst, key=lambda x: x[1]))  # -> ['Carl', 'Alice', 'Bob']
print()

print(max(lst))  # -> Carl
print(max(lst, key=len))  # -> Alice
print(max(lst, key=lambda x: x[1]))  # -> Bob
print()

print(min(lst))  # -> Alice
print(min(lst, key=len))  # -> Bob
print(min(lst, key=lambda x: x[1]))  # -> Carl
print()

# --- map() と lambda ---

# map(function, iterable)
# function に iterable の値を引数とする関数を設定し、
# その戻り値で 各 iterable 要素を書き換える

mapped_lst = list(map(lambda x: x ** 2, range(5)))
print(mapped_lst)  # -> [0, 1, 4, 9, 16]
print()

# --- filter() と lambda ---

# filter(function, iterable)
# function に iterable の値を引数とする式か関数を設定し、
# その戻り値が True の要素だけの iterable を生成する

filtered_list = list(filter(lambda x: x % 2 == 0, range(10)))
print(filtered_list)  # -> [0, 2, 4, 6, 8]
print()

