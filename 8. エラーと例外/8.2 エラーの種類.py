# === エラーと例外 ===

"""
・Pythonにおいて、エラーは構文エラー（syntax error）と例外（exception）に区別される。

・構文として誤っているものは「構文エラー」、
  構文として正しくても実行中に発生するエラーは「例外」と呼ばれる。

・ここでは想定内の例外を捕捉し対応する例外処理ではなく、
  想定外のエラー・例外の原因の確認方法について説明する。
"""


# === インポートに関するエラー ===

# --- ModuleNotFoundError ---
"""モジュールが見つからない"""

try:
    import mathmatics
except ModuleNotFoundError as e:
    print('ModuleNotFoundError:', e)
    # -> ModuleNotFoundError: No module named 'mathmatics'

# --- ImportError ---
"""
・モジュールのオブジェクトが見つからない
・大文字小文字も区別される
"""

try:
    from math import COS
except ImportError as e:
    print('ImportError:', e)
    # -> ImportError: cannot import name 'COS' from 'math' (unknown location)

# === 型や値、名前に関するエラー ===

# --- AttributeError ---
"""属性やメソッドの名前、オブジェクトの型を間違えている"""

import math

# メソッド名の間違い
try:
    print(math.PI)
except AttributeError as e:
    print('AttributeError:', e)
    # -> AttributeError: module 'math' has no attribute 'PI'

# オブジェクトの型が想定と異なっている
try:
    l = 100
    l.append(200)
except AttributeError as e:
    print('AttributeError:', e)
    # -> AttributeError: 'int' object has no attribute 'append'

# --- TypeError ---
"""不適切な型に対して演算や組み込み関数による処理が行われた"""

try:
    n = '100'
    print(n + 200)
except TypeError as e:
    print('TypeError:', e)
    # -> TypeError: can only concatenate str (not "int") to str

try:
    print(float(['1.23E-3']))
except TypeError as e:
    print('TypeError:', e)
    # -> TypeError: float() argument must be a string or a number, not 'list'

# --- ValueError ---
"""型は合っているが値が適切でない"""

try:
    print(float('float number'))
except ValueError as e:
    print('ValueError:', e)
    # -> ValueError: could not convert string to float: 'float number'

# --- ZeroDivisionError ---
"""0で割り算が行われた"""

try:
    print(100 / 0)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
    # -> ZeroDivisionError: division by zero

try:
    print(100 // 0)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
    # -> ZeroDivisionError: integer division or modulo by zero

try:
    print(100 % 0)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
    # -> ZeroDivisionError: integer division or modulo by zero

# --- NameError ---
"""名前が見つからなかった"""

try:
    my_number = 100
    print(myNumber)
except NameError as e:
    print('NameError:', e)
    # -> NameError: name 'myNumber' is not defined

# === インデックスやキーに関するエラー ===

# --- IndexError ---
"""
リストやタプルなどのシーケンスオブジェクトに格納された値を[インデックス]で取得する際に、
範囲外の位置（要素数を超えたインデックス値）を指定してしまった
"""

try:
    l = [0, 1, 2]
    print(l[100])
except IndexError as e:
    print('IndexError:', e)
    # -> IndexError: list index out of range

# --- KeyError ---
"""
辞書（dict型）の値をキーを指定して取得する際に、
存在しないキーを指定してしまった
"""

try:
    d = {'a': 1, 'b': 2, 'c': 3}
    print(d['x'])
except KeyError as e:
    print('KeyError:', e)
    # -> KeyError: 'x'

# === ファイルやディレクトリに関するエラー ===

# --- FileNotFoundError ---
"""open() でファイルを読み込む際などに指定したファイルが見つからない"""

try:
    with open('not_exist_file.txt') as f:
        print(f.read())
except FileNotFoundError as e:
    print('FileNotFoundError:', e)
    # -> FileNotFoundError: [Errno 2] No such file or directory: 'not_exist_file.txt'

# --- FileExistsError ---
"""すでに存在しているファイルやディレクトリを作成しようとした"""

import os

dir_path = 'test'
os.mkdir(dir_path)

try:
    os.mkdir(dir_path)
except FileExistsError as e:
    print('FileExistsError:', e)
    # -> FileExistsError: [WinError 183] 既に存在するファイルを作成することはできません。: 'test'

os.rmdir(dir_path)
