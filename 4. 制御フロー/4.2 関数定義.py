# === def / while ===

# return 文無

def print_fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

print_fib(2000)
print(print_fib(0))  # return 文を持たないので None を返す

# return 文有

def return_fib(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = return_fib(100)  # return した値を返す
print(f100)

# 関数は代入できる

f = print_fib
f(100)
print()

# ===デフォルト値===

# デフォルト引数が設定された引数は省略可能

def ask_ok(prompt, answer, retries=4, reminder='Please try again!'):
    while True:
        print(prompt)
        ok = answer
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
ask_ok('Do you really want to quit?', 'y')
ask_ok('OK to overwrite the file?', 'ye', 2)
ask_ok('OK to overwrite the file?', 'yes', 2, 'Come on, only yes or no!')
print()

# デフォルト値は関数が定義された時点で初期化

i = 5
def f(arg=i):
    print(arg)
i = 6
f()  # -> 5
print()

# デフォルト値は関数定義時に一度しか初期化されない

def f(a, lst=[]):
    lst.append(a)
    return lst

print(f(1), end=', ')  # -> [1]
print(f(2), end=', ')  # -> [1, 2]
print(f(3))  # -> [1, 2, 3]

# リスト・辞書・関数などの変更可能なデフォルト値を呼び出しごとに初期化したい場合

def f(a, lst=None):
    if lst is None:
        lst = []
    lst.append(a)
    return lst

print(f(1), end=', ')  # -> [1]
print(f(2), end=', ')  # -> [2]
print(f(3))  # -> [3]
print()

# キーワードで引数の値を指定して設定

def man(name, male=True, married=True, height=170):
    if male:
        i, p = 'He', 'His'
    else:
        i, p = 'She', 'Her'
    if married:
        m = 'is married'
    else:
        m = 'is not married'
    print(p, 'name is', name + '.')
    print(i, m, 'and', p, 'height is', height, 'cm.')

man('Kiyofumi')
man(name='Taro')
man(name='Yoshio',married=False)
man(married=False, name='Hanako')
man('Akemi', False, False)
man('Setsuko', height=190)
args = ('Hiromi', 'femail')
kwargs = {'married': True, 'height': 160}
# 引数のアンパック
man(*args, **kwargs)
print()

# === 可変長引数（*args, **kwargs） ===

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

sentences = ["It's very runny, sir.", "It's really very, VERY runny, sir.", 'Yes, so much.']
signature = {'shopkeeper': "Michael Palin", 'client': "John Cleese", 'sketch': "Cheese Shop Sketch"}
cheeseshop("Limburger", *sentences, Kiyofumi='President', **signature)
print()

# Keyword 引数は可変長引数のあとに指定する

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))
print()

# === ラムダ式 ===

# 無名関数 = lambda 仮引数: <*argsを含む式>
print(type(lambda x: x + 1))
# 戻り値 = (<lambda式>)(実引数)
print(type((lambda x: x + 1)(1)))
print()

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0), end=', ')
print(f(1))

value = (lambda a, b: a + b)(1, 2)
print(value)
print()

# --- sorted() と lambda ---

# sorted(iterable, key=None, reverse=False)
# key 関数に、iterable の値を引数とする関数を設定し、
# その戻り値を元に最終的にソートする

lst = ['Charle', 'Bob', 'Alice']
print(sorted(lst))
print(sorted(lst, key=len))
print(sorted(lst, key=lambda x: x[1]))
print()

# --- map() と lambda ---

# map(function, iterable)
# function に iterable の値を引数とする関数を設定し、
# その戻り値で 各 iterable 要素を書き換える

print(list(map(lambda x: x**2, range(5))))
print()

# --- filter() と lambda ---

# filter(function, iterable)
# function に iterable の値を引数とする式か関数を設定し、
# その戻り値が True の要素だけの iterable を生成する

print(list(filter(lambda x: x % 2 == 0, range(10))))
print()

# === ドキュメンテーション文字列 ====

def my_func():
    """\
    docstring-test
    line1"""
print(my_func.__doc__)
print(type(my_func.__doc__))
print()

# reStructuredText（reST）スタイル

def func_rest(arg1, arg2):
    """Summary line.

    :param arg1: Description of arg1
    :type arg1: int
    :param arg2: Description of arg2
    :type arg2: str
    :returns: Description of return value
    :rtype: bool
    """
    return True

# NumPyスタイル

def func_numpy(arg1, arg2):
    """Summary line.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value
    """
    return True

# Googleスタイル

def func_google(arg1, arg2):
    """Summary line.

    Extended description of function.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value

    """
    return True

# === 関数アノテーション ===

# function(arg1:型 , arg2:型 = default値 ) -> 戻り値の型

def str_multiply(x: str, y: int = 5) -> str:
    return x * y

print(str_multiply('Oh! '))

# 関数アノテーションは __annotations__ 属性に辞書型として格納されている
print(type(str_multiply.__annotations__))
print(str_multiply.__annotations__)
print(str_multiply.__annotations__['x'])
print()
