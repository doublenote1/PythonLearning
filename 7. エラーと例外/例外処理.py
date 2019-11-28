# ****** 例外処理の基本: try, except ******

"""
・例えばゼロによる除算が行われると、
  ZeroDivisionError という例外が発生して処理が終了する。

・この例外をキャッチ（捕捉）するには以下のように記述する。
"""

try:
    print(1 / 0)
except ZeroDivisionError as e:
    print('Error')  # -> Error
print()

"""
・さらに、「except <例外型> as <変数名>:」 とすることで、
  変数に例外オブジェクトを格納して使用することができる。
・この変数名には 'e' や 'err' などの名前が使われることが多い。

・例外オブジェクトには例外発生時に出力されるエラーメッセージなどが格納されているので、
  それを出力することでエラーの内容を確認できる。
"""

try:
    print(1 / 0)
except ZeroDivisionError as e:
    print(e)  # -> division by zero
    print(type(e))  # -> <class 'ZeroDivisionError'>
print()

"""
・try節 で例外が発生した時点で try節 の中のそれ以降の処理はスキップされる。
・以下の例のように forループ の途中で例外が発生すると、
  その時点で forループ は終了して except節 の処理に移行する。
"""

try:
    for i in [-2, -1, 0, 1, 2]:
        print(1 / i)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
# -> -0.5
# -> -1.0
# -> ZeroDivisionError: division by zero
print()

# ****** 複数の例外をキャッチ ******

"""
除算を行い ZeroDivisionError をキャッチする以下の関数を定義する。
"""

def divide(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print('catch ZeroDivisionError:', e)

"""
ZeroDivisionError はキャッチできるが、
それ以外の例外はキャッチできず処理が途中終了する。
"""

divide(1, 0)
# -> catch ZeroDivisionError: division by zero
print()

# === 複数の例外に異なる処理を実行 ===

"""
・except節 は複数指定することができる。
・複数の例外に対してそれぞれ異なる処理を記述可能。
"""

def divide_each(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print('catch ZeroDivisionError:', e)
    except TypeError as e:
        print('catch TypeError:', e)

divide_each(1, 0)
# -> catch ZeroDivisionError: division by zero
divide_each('a', 'b')
# -> catch TypeError: unsupported operand type(s) for /: 'str' and 'str'
print()

# === 複数の例外に同じ処理を実行 ===

"""
・一つの except節 に複数の例外型をタプルで指定することもできる。

・変数に格納される例外オブジェクトの中身はそれぞれ異なるので、
  エラーメッセージを出力してエラーの内容を確認するだけであればこれで問題ない。
"""

def divide_same(a, b):
    try:
        print(a / b)
    except (ZeroDivisionError, TypeError) as e:
        print(e)

divide_same(1, 0)  # -> division by zero
divide_same('a', 'b')  # -> unsupported operand type(s) for /: 'str' and 'str'
print()

# ****** すべての例外をキャッチ ******

"""
基本的には想定される例外型を except節 に指定すべきだが、
特定の例外を指定せずにすべての例外をキャッチすることも可能。
"""

# === ワイルドカードの except節（bare except） ===

"""
・except節 から例外型を省略するとすべての例外をキャッチできる。
・複数の except節 がある場合は例外型を省略できるのは最後の except節 のみ。

・例外型を省略した書き方は「ワイルドカードの except節」 や 「bare except」 などと呼ばれるが、
  公式ドキュメントにあるように使用には注意が必要。
"""

"""
・最後の except節 では例外名を省いて、ワイルドカードにすることができます。
・ワイルドカードの except節 は非常に注意して使ってください。
・というのは、ワイルドカードは通常のプログラムエラーをたやすく隠してしまうからです！
"""

"""この方法では例外オブジェクトを取得できない。"""
def divide_wildcard(a, b):
    try:
        print(a / b)
    except:
        print('Error')

divide_wildcard(1, 0)  # -> Error
divide_wildcard('a', 'b')  # -> Error
print()

# === 基底クラスException ===

"""
・システム終了以外のすべての組み込み例外の基底クラスである Exception を使う方法もある。
・この方法では例外オブジェクトを取得できる。
"""

def divide_exception(a, b):
    try:
        print(a / b)
    except Exception as e:
        print(e)

divide_exception(1, 0)  # -> division by zero
divide_exception('a', 'b')  # -> unsupported operand type(s) for /: 'str' and 'str'
print()

"""
なお、想定していない例外までキャッチしてしまうのはバグの温床になるので、
繰り返しになるが、except節 には可能な限り想定される例外型を指定したほうがいい。
"""

# ****** 正常終了時の処理: else ******

"""
・try節 で例外が発生せず正常終了したあとに行う処理を else節 に指定できる。
・例外が発生して except でキャッチした場合は else節 の処理は実行されない。
"""

def divide_else(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print('catch ZeroDivisionError:', e)
    else:
        print('finish (no error)')

divide_else(1, 2)
# -> 0.5
# -> finish (no error)
divide_else(1, 0)  # -> catch ZeroDivisionError: division by zero
print()

# ****** 終了時に常に行う処理: finally ******

"""
例外が発生した場合もしなかった場合も、
常に最後に行う処理を finally節 に指定できる。
"""

def divide_finally(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print('catch ZeroDivisionError:', e)
    finally:
        print('all finish')

divide_finally(1, 2)
# -> 0.5
# -> all finish
divide_finally(1, 0)
# -> catch ZeroDivisionError: division by zero
# -> all finish
print()

"""
・else節 と finally節 を同時に使うことも可能。
・正常終了時は else節 の処理が実行されたあとに finally節 の処理が実行される。
"""

def divide_else_finally(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        print('catch ZeroDivisionError:', e)
    else:
        print('finish (no error)')
    finally:
        print('all finish')

divide_else_finally(1, 2)
# -> 0.5
# -> finish (no error)
# -> all finish
divide_else_finally(1, 0)
# -> catch ZeroDivisionError: division by zero
# -> all finish
print()

# ****** 例外を無視: pass ******

"""
例外をキャッチしても特に何も処理を行わずにスルーしたい場合は pass文 を使う。
"""

def divide_pass(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        pass

divide_pass(1, 0)
