"""
■ モジュール = パイソン スクリプト ファイル

■ オブジェクト = このファイルのコメント内では、
アクセス可能なモジュール内の関数や変数を示す

■ ローカル = カレントディレクトリ内かパスの通ったディレクトリ、もしくはその中のという意味
"""

# ****** インポート(カレントフォルダ内) ******

# === モジュール ===

import math

import module1
import module2

# 呼び出し
module1.func1()
module1.func2()
module2.func1()
del math, module1, module2
print()

# === モジュール内のオブジェクト(複数選択可能) ===

from module1 import func1, func2

# 呼び出し
func1()
func2()
del func1, func2
print()

# === モジュルー内のオブジェクトを全て ===

from module1 import *

# 呼び出し
func1()
func2()
del func1, func2
print()

# ****** インポート(カレントフォルダ以下の所から) ******

# === モジュール ===

# ① import <dir>.<dir>….<module>

import package.inner.package_module1

# 呼び出し
package.inner.package_module1.func1()
package.inner.package_module1.func1()
del package.inner.package_module1

# ② from <dir>.<dir>… import <module> (複数選択可能)

from package.inner import package_module1, package_module2

# 呼び出し
package_module1.func1()
package_module2.func1()
del package_module1, package_module2
print()

# === パッケージ内の指定モジュールを全て ===

'''フォルダ内に __init__.py があり、
その中に書いた __all__ 変数に
読み込むモジュールの指定がされている場合のみ
'''

# from <dir>.<dir>….<module> import *

from package.multiple_import import *

# 呼び出し
included_module.func()
# --all-- で指定しないものはエラーになる
try:
    excluded_module.excluded()
except Exception as e:
    print('ERROR:', e)
del included_module
print()

# === モジュール内のオブジェクト ===

# from <dir>.<dir>….<module> import <object> (複数選択可能)

from package.inner.package_module1 import func1, func2

# 呼び出し
func1()
func2()
del func1, func2
print()

# === モジュール内のオブジェクトを全て ===

# from <dir>.<dir>….<module> import *

from package.inner.package_module1 import *

# 呼び出し
func1()
func2()
del func1, func2
print()

# ****** 別名を付けてインポート ******

# === モジュール ===

import module1 as mod
import package.inner.package_module1 as pk
from package.inner import package_module2 as pk2

# 呼び出し
mod.func1()
pk.func1()
pk2.func1()
del mod, pk, pk2
print()

# === モジュール内のオブジェクト ===

from module1 import func1 as f
from package.inner.package_module1 import func1 as pk_f

# 呼び出し
f()
pk_f()
del f, pk_f
print()

# ****** その他 ******

# === モジュール検索パス (sys.path) ===

# --- モジュール検索パスのリストの取得 ---

'''
含まれるパス：
    1. スクリプトファイルがあるディレクトリ (sys.path[0])
    2. 環境変数PYTHONPATHで指定したディレクトリ
    3. カレントディレクトリ
    4. 標準ライブラリのためのディレクトリ
    5. pip でインストールしたサードパーティライブラリのための
       site-packages ディレクトリ
       
先頭から優先してモジュールを検索する
'''

import sys
from pprint import pprint

pprint(sys.path)
print()

# --- モジュール検索パスのリストへパス追加 ---

'''
sys.pathはただのリストオブジェクトなので、
append()メソッドなどで新たなパスを追加することが可能
'''

# === あるモジュールがどんな名前を定義しているか ===

import module1

print(dir(module1))

del module1
print()

# === モジュールの名前を取得 ===

'''as を使って呼び出している時は元々の名前を出力'''

import module1
import module2 as mod2

print(module1.__name__)
print(mod2.__name__)

del module1, mod2
print()

# === モジュール関数を変数に代入して使う ===

import module1

func_m1 = module1.func1
func_m1()

del module1
print()
