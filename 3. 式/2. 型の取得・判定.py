# === オブジェクトの型を取得、確認 ===

print(type('string'))  # -> <class 'str'>
print(type(100))  # -> <class 'int'>
print(type([1, 2, 3]))  # -> <class 'list'>
print(type((1, 2, 3)))  # -> <class 'tuple'>
print(type({'a': 1, 'b': 2, 'c': 3}))  # -> <class 'dict'>
print(type(print))  # -> <class 'builtin_function_or_method'>

def sample():
    pass

print(type(sample))  # -> <class 'function'>

class Sample:
    pass

print(type(Sample))  # -> <class 'type'>
print()

# === オブジェクトの型の判定 ===

# --- 特定の型に一致するかどうか ---

print(type('string') is str)  # -> True
print(type('string') is int)  # -> False

def is_str(v):
    return type(v) is str

print(is_str('string'))  # -> True
print(is_str(100))  # -> False
print(is_str([0, 1, 2]))  # -> False
print()

# --- 複数の型のどれかに一致するかどうか ---

def is_str_or_int(v):
    return type(v) in (str, int)

print(is_str_or_int('string'))  # -> True
print(is_str_or_int(100))  # -> True
print(is_str_or_int([0, 1, 2]))  # -> False
print()

# 引数の型によって処理を変える関数の定義

def type_condition(v):
    if type(v) is str:
        print('type is str')
    elif type(v) is int:
        print('type is int')
    else:
        print('type is not str or int')

type_condition('string')  # -> type is str
type_condition(100)  # -> type is int
type_condition([0, 1, 2])  # -> type is not str or int
print()

# === isinstance() ===

print(isinstance('string', str))  # -> True
print(isinstance(100, str))  # -> False
print(isinstance(100, (int, str)))  # -> True
print()

# isinstance() は type() と違い、
# 第二引数に指定したクラスを継承するサブクラスのインスタンスに対しても
# True を返す

print(type(True))  # -> <class 'bool'>
print(type(True) is bool)  # -> True
print(type(True) is int)  # -> False
print(isinstance(True, bool))  # -> True
print(isinstance(True, int))  # -> True

