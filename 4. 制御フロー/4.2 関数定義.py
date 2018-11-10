# === 関数定義基本 ===

# return 文無

def print_fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b

print_fib(500)  # -> 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
print()

print(print_fib(0))  # return 文を持たないので None を返す

# return 文有

def return_fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

f100 = return_fib(100)  # return した値を返す
print(f100)  # -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# 関数は代入できる

f = print_fib
f(100)
print()  # -> 0 1 1 2 3 5 8 13 21 34 55 89
print()

# ===デフォルト値===

# デフォルト引数が設定された引数は省略可能

def ask_ok(prompt, answer, retries=4, reminder='Please try again!'):
    while True:
        print(prompt)
        if answer in ('y', 'ye', 'yes'):
            return True
        if answer in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries <= 0:
            return 'Unresolved !'
        print(reminder)

print(ask_ok('Do you really want to quit ?', 'y'))
print()
print(ask_ok('OK to overwrite the file ?', 'nope'))
print()
print(ask_ok('Will you continue ?', '??', 2, 'Come on, only yes or no!'))
print()

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

# キーワードで引数の値を指定して設定

def man(name, male=True, married=True):
    if male:
        pronoun, title = "He's", "Mr."
    elif not male and married:
        pronoun, title = "She's", "Mrs."
    else:
        pronoun, title = "She's", "Miss"
    if married:
        m = 'is married.'
    else:
        m = 'is not married.'
    print(pronoun, title, name, '.')

man('Seiichi')  # -> He's Mr. Seiichi .
man('Setsuko', False)  # -> She's Mrs. Setsuko .
man('Misato', False, False)  # -> She's Miss Misato .
man('Kiyofumi', married=False)  # -> He's Mr. Kiyofumi .
man(married=False, male=False, name='Cookie')  # -> She's Miss Cookie .

# 引数のアンパック
args = ('Hiromi', False)
kwargs = {'married': False}
man(*args, **kwargs)  # -> She's Miss Hiromi .
print()

# === 可変長引数(*args, **kwargs) ===

def zoo(kind, *arguments, **keywords):
    print("-- 世界の", kind, " --", sep='')
    print("-- 世の中には様々な", kind, "が存在する --", sep='')
    str_ex = ""
    for arg in arguments:
        str_ex += arg + "、"
    str_ex.rstrip("、")
    print("例えば、", str_ex, "などが挙げられる", sep='')
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

examples = ["パンダ", "チンパンジー", "ゴリラ", "ペリカン"]
signature = {"監督": "井筒", "脚本": "野島信二"}
zoo("動物", "猿", "豚", *examples, 社長="近藤清史", 秘書="みっちゃ", **signature)
print()

# Keyword 引数は可変長引数のあとに指定する

def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))  # -> earth/mars/venus
print(concat("earth", "mars", "venus", sep="."))  # -> earth.mars.venus
print()

# === ドキュメンテーション文字列 ====

def my_func():
    """\
    docstring-test
    line1"""

print(my_func.__doc__)
print(type(my_func.__doc__))
print()

# reStructuredText(reST)スタイル

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
print(type(str_multiply.__annotations__))  # -> <class 'dict'>
dic_a = str_multiply.__annotations__
print(dic_a)  # -> {'x': <class 'str'>, 'y': <class 'int'>, 'return': <class 'str'>}
print(str_multiply.__annotations__['x'])  # -> <class 'str'>
print()
