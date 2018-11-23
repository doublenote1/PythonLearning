# ****** オブジェクトの型を取得、確認 ******

print(type('string'))  # -> <class 'str'>

print(type(100))  # -> <class 'int'>
print(type(1.23))  # ->  <class 'float'>

print(type(True))  # -> <class 'bool'>

print(type([1, 2, 3]))  # -> <class 'list'>
print(type((1, 2, 3)))  # -> <class 'tuple'>
print(type({1, 2, 3}))  # -> <class 'set'>
print(type({'a': 1, 'b': 2, 'c': 3}))  # -> <class 'dict'>

print(type(print))  # -> <class 'builtin_function_or_method'>

def sample():
    pass

print(type(sample))  # -> <class 'function'>

class Sample:
    pass

print(type(Sample))  # -> <class 'type'>
print()

# ****** オブジェクトの型の判定 ******

# === type() を使う ===

# --- 特定の型に一致するかどうか ---

print(type('string') is str)  # -> True
print(type('string') is int)  # -> False
print()

# --- 複数の型のどれかに一致するかどうか ---

print(type('string') in (str, int))  # -> True
print(type(100) in (str, int))  # -> True
print(type(1.23) in (str, int))  # -> False
print()

# === isinstance() を使う===

# --- 特定の型に一致するかどうか ---

print(isinstance('string', str))  # -> True
print(isinstance('string', int))  # -> False
print()

# --- 複数の型のどれかに一致するかどうか ---

print(isinstance('string', (int, str)))  # -> True
print(isinstance(100, (int, str)))  # -> True
print(isinstance(1.23, (int, str)))  # -> False
print()

# === type() と isinstance() の違い ===

'''
isinstance()は、
第二引数に指定したクラスを継承するサブクラスのインスタンスに対しても
True を返す
'''

print(type(True))  # -> <class 'bool'>

print(type(True) is bool)  # -> True
print(type(True) is int)  # -> False

print(isinstance(True, bool))  # -> True
print(isinstance(True, int))  # -> True

