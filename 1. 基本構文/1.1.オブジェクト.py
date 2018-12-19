from user import print_err

# 1. オブジェクトとは

"""
・Python プログラムのすべてのデータは「オブジェクト」で表現される
・全てのオブジェクトは、識別可能（`id()`関数で調査、`is`演算子で比較可能）
・全てのオブジェクトは、不変的な型情報を持つ(`type()`関数で調査可能)

・python は動的型付け言語
  静的型付け: プログラムを実行前(コンパイル時)に変数の型検査を行う
  動的型付け: プログラムを実行しながら変数の型検査を行う

                  ┌──────────────┐
                  │組込データ（オブジェクト）型│
                  └───────┬──────┘
            ┌──────────┴─────────────┐
      ┌──┴───┐                            ┌─────┴──────┐
      │数値型(不可)│                            │コンテナ型（イテラブル）│
      └──┬───┘                            └─────┬──────┘
  ┌────┼─────┐              ┌──────────┼─────────────┐
┌┴─┐┌─┴──┐┌─┴─┐    ┌──┴───┐        ┌─┴─┐                  ┌─┴──┐
│整数││浮動小数││複素数│    │シーケンス型│        │集合型│                  │マップ型│
└──┘└────┘└───┘    └──┬───┘        └─┬─┘                  └─┬──┘
      ┌──────┬─────────┤            ┌───┴─┐                      │
┌──┴──┐┌──┴───┐┌────┴─┐┌───┴─┐┌──┴────────┐┌─┴──┐
│リスト(可)││タプル(不可)││文字列(不可)││セット(可)││フローズンセット(不可)││辞書(可)│
└─────┘└──────┘└──────┘└─────┘└───────────┘└────┘

※ 他に bool型、range型、bytes型、bytearray型、file object型 がある

"""

# 2. オブジェクトの属性（変数とメソッド）

# 2.1. オブジェクトの変数

"""`オブジェクト名`.`変数名`でオブジェクト固有の変数にアクセス可能"""

'全てのオブジェクトは`__class__`変数に型情報を保持している'
print('abc'.__class__)  # -> <class 'str'>
print()

# 2.2. オブジェクトのメソッド

"""`オブジェクト名`.`メソッド名`でオブジェクトメソッド呼び出し可能"""

print('abc'.upper)  # -> <built-in method upper of str object at 0x0000000000630810>
print('abc'.upper())  # -> ABC
print()

# 3. オブジェクトの「型情報」を取得・判定

# 3.1. オブジェクトの型情報を取得

# (a) `type`関数を使う

print(type('string'))  # -> <class 'str'>
print(type(100))  # -> <class 'int'>
print(type(1.23))  # ->  <class 'float'>
print(type(True))  # -> <class 'bool'>
print(type([1, 2, 3]))  # -> <class 'list'>
print(type((1, 2, 3)))  # -> <class 'tuple'>
print(type({1, 2, 3}))  # -> <class 'set'>
print(type({'a': 1, 'b': 2, 'c': 3}))  # -> <class 'dict'>
print(type(print))  # -> <class 'builtin_function_or_method'>

def func():
    pass
print(type(func))  # -> <class 'function'>

class Clas:
    pass
print(type(Clas))  # -> <class 'type'>
print()

# (b) `__class__`変数を使う

print('abc'.__class__)  # -> <class 'str'>

# (c) `__name__`変数を使う

"""
`type`関数も`__class__`変数も、
型情報文字列だけを保持する`__name__`変数を持つ
"""

print(type('string').__name__)  # -> str
print('abc'.__class__.__name__)  # -> str

# 3.2. オブジェクトの型の判定

# (a) `type()`関数を使う

# 特定の型に一致するかどうか
print(type('string') is str)  # -> True
print(type('string') is int)  # -> False
print()

# 複数の型のどれかに一致するかどうか
print(type('string') in (str, int))  # -> True
print(type(100) in (str, int))  # -> True
print(type(1.23) in (str, int))  # -> False
print()

# (b) `isinstance()`関数を使う

# 特定の型に一致するかどうか
print(isinstance('string', str))  # -> True
print(isinstance('string', int))  # -> False
print()

# 複数の型のどれかに一致するかどうか
print(isinstance('string', (int, str)))  # -> True
print(isinstance(100, (int, str)))  # -> True
print(isinstance(1.23, (int, str)))  # -> False
print()

# 3.2.1. `type()` と `isinstance()` の違い

"""
isinstance()は、
第二引数に指定したクラスを継承するサブクラスのインスタンスに対しても
True を返す
"""

print(type(True))  # -> <class 'bool'>
print(type(True) is bool)  # -> True
print(type(True) is int)  # -> False
print(isinstance(True, bool))  # -> True
print(isinstance(True, int))  # -> True

# 4. ミュータブルとイミュータブル

"""
・ミュータブル:
    自身を収容する変数に対して破壊的メソッドや演算代入が行なわれたり、
    自身が持つ要素への代入が行われたりした時、
    変数と自身が持つ参照値（id）を変えずに、自身が変更されるオブジェクトの事

・イミュータブル:
    ミュータブルが持つ様な、
    破壊的メソッド、自身の要素への代入手段もしくは要素そのものを持たず、
    自身を収容する変数に対し演算代入が行われた時は
    その変数に自身の参照値を破棄されるオブジェクトの事

    ※ 自身の参照値の破棄を行った変数はその後、破棄する前に行なわれた変更の結果として新たなオブジェクトが作られると、そのオブジェクトの参照値を収納する

・ミュータブル・イミュータブル共に、
  自身を収納する変数に対し再代入が行われると、
  その変数には、新たに作られるオブジェクトへの参照値が収納される
"""

# 4.1. ミュータブル

"""リスト型の例"""

# (a) 破壊的メソッド

a = [1, 2, 3]
id_before_change = id(a)
a.append(4)
print(a)  # -> [1, 2, 3, 4]
print(id_before_change == id(a))  # -> True

# (b) 演算代入

a = [1, 2, 3]
id_before_change = id(a)
a += [4]
print(a)  # -> [1, 2, 3, 4]
print(id_before_change == id(a))  # -> True

# (c) 要素の変更

a = [1, 2, 3]
id_before_change = id(a)
a[0] = 100
print(a)  # -> [100, 2, 3]
print(id_before_change == id(a))  # -> True

# (d) 再代入

a = [1, 2, 3]
id_before_change = id(a)
a = [4, 5, 6]
print(a)  # -> [4, 5, 6]
'別のオブジェクトを参照する様になる'
print(id_before_change == id(a))  # -> False
print()

# 4.2. イミュータブル

"""文字列型の例"""

# (a) メソッド

a = 'test'
id_before_change = id(a)
'''
自身が収納された変数に対しメソッドが実行されても、
その結果、返り値として新たに作られたオブジェクトの参照値が
その変数に収納される事はない（破壊的メソッドを持たない）
'''
a.upper()
print(a)  # -> test
print(id_before_change == id(a))  # -> True

# (b) 演算代入

a = 'test'
id_before_change = id(a)
a += 'test'
print(a)  # -> testtest
'別のオブジェクトを参照する様になる'
print(id_before_change == id(a))  # -> False

# (c) 要素の変更はできない

a = 'test'
id_before_change = id(a)
try:
    a[0] = 'a'
except Exception as e:
    print_err(e)  # -> TypeError: 'str' object does not support item assignment

# (d) 再代入

a = 'test'
id_before_change = id(a)
'再代入'
a = 'sub'
print(a)  # -> sub
'別のオブジェクトを参照する様になる'
print(id_before_change == id(a))  # -> False
print()
