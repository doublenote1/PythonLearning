# ****** モジュール検索パス (sys.path) ******

# === モジュール検索パスのリストの取得 ===

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

# === モジュール検索パスのリストへパス追加 ===

'''
sys.pathはただのリストオブジェクトなので、
append()メソッドなどで新たなパスを追加することが可能
'''

# ****** あるモジュールがどんな名前を定義しているか ******

import module1

print(dir(module1))

del module1
print()

# ****** モジュールの名前を取得 ******

'''as を使って呼び出している時は元々の名前を出力'''

import module1
import module2 as mod2

print(module1.__name__)
print(mod2.__name__)

del module1, mod2
print()

# ****** モジュール関数を変数に代入して使う ******

import module1

func_m1 = module1.func1
func_m1()

del module1
print()
