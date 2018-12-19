"""
・Python のプログラムの中で環境変数を取得して確認したり、
  設定（追加・上書き）、削除したりするには os.environ を使う。
・なお、環境変数の設定や削除による変更はその Python プログラムの中でのみ有効。
・システムの環境変数が書き換わるわけではない。
"""

import os

print(type(os.environ))  # -> <class 'os._Environ'>
print()
"""
・os.environ の型は os._Environ。
・os._Environ はキー key と値 value が対になったマップ型オブジェクトで、
  辞書（dict型）などと同様のメソッドを持つ。
・環境変数名が key、その値が value になっている。
"""

# === 環境変数を取得 ===

# --- 1: os.environ[環境変数名] ---

"""存在しない環境変数名を指定するとエラー KeyError になる"""

print(os.environ['APPDATA'])  # -> C:\Users\KIYO\AppData\Roaming
try:
    print(os.environ['NEW_KEY'])
except KeyError as e:
    print(type(e))  # -> <class 'KeyError'>
print()

# --- 2: os.environ.get(環境変数名, デフォルト値=None) ---

"""
・os.environ の get() メソッドを使うと、
  存在しない場合にはデフォルト値を取得できる
"""

print(os.environ.get('COMSPEC'))  # -> C:\windows\system32\cmd.exe
print(os.environ.get('NEW_KEY'))  # -> None
print(os.environ.get('NEW_KEY', 'default'))  # -> default
print()

# --- 3: os.getenv(環境変数名, デフォルト値=None) ---

"""辞書の get() メソッドと同様、キーが存在しない場合はデフォルト値を返す"""
print(os.getenv('COMSPEC'))  # -> C:\windows\system32\cmd.exe
print(os.getenv('NEW_KEY'))  # -> None
print(os.getenv('NEW_KEY', 'default'))  # -> default
print()

# === 環境変数を設定(追加・上書き) ===

"""文字列以外を代入するとエラーTypeErrorになる"""

os.environ['NEW_KEY'] = 'test'
print(os.environ['NEW_KEY'])  # -> test

os.environ['NEW_KEY'] = 'test2'
print(os.environ['NEW_KEY'])  # -> test2

try:
    os.environ['NEW_KEY'] = 1
except TypeError as e:
    print('TypeError:', e)  # -> TypeError: str expected, not int
print()

# === 環境変数を削除 ===

"""
・環境変数を削除するには os.environ の pop() メソッドや del文 を使う
・辞書と同じ
"""

# --- pop() ---

print(os.environ.pop('NEW_KEY'))  # -> test2
print(os.environ.pop('NEW_KEY', 'None'))  # -> None
print()

# --- del文 ---

os.environ['NEW_KEY'] = '100'
print(os.getenv('NEW_KEY'))  # -> 100
del os.environ['NEW_KEY']
print(os.getenv('NEW_KEY'))  # -> None
try:
    del os.environ['NEW_KEY']
except KeyError as e:
    print('KeyError:', e)  # -> KeyError: 'NEW_KEY'
