# === docstring ====

def my_func():
    """docstring-test
    line1
    """

print(my_func.__doc__)
print(type(my_func.__doc__))
print()

class MyClass():
    """docstring-test
    line1
    """

print(MyClass.__doc__)
print(type(MyClass.__doc__))
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

# --- 基本の型 ---

'''function(arg1: 型, arg2: 型 = default値 ) -> 戻り値の型'''

def str_multiply(x: str, y: int = 5) -> str:
    return x * y

print(str_multiply('Oh! '))
print()

# --- __annotations__ 属性 ---

'''
関数アノテーションは __annotations__ 属性に
辞書型として格納されている
'''

from pprint import pprint

print(type(str_multiply.__annotations__))  # -> <class 'dict'>
pprint(str_multiply.__annotations__, width=10)
print()

# --- 型ヒント(Type Hints) ---

'''
List[X]:               要素の型が X のリスト
Union[X, Y]:           X か Y いずれかの型
Any:                   任意の型
Callable[[X ...], Y]]: 引数の型のリストが[X ...]、
                       返り値の型が Y の呼び出し可能オブジェクト
Dict[X, Y]:            キーの型が X, 値の型が Y の辞書
'''

from typing import Union, List

def func_u(x: List[Union[int, float]]) -> float:
    return sum(x) ** 0.5

print(func_u([0.5, 9.5, 90]))
