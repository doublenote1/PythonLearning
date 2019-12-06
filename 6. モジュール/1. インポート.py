"""
■ モジュール = パイソン スクリプト ファイル

■ パッケージの種類:
    通常のパッケージ: モジュールと「__init__.py」を含むディレクトリ
    名前空間パッケージ: モジュールと「__init__.py」を含まないディレクトリ

■ オブジェクト = このファイルのコメント内では、
アクセス可能なモジュール内の関数や変数を示す

■ ローカル = カレントディレクトリ内かパスの通ったディレクトリ、もしくはその中のという意味
"""

# ****** インポート(ローカルフォルダ内) ******

# === モジュール ===

"標準ライブラリの呼び出し"
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

# ****** インポート(ローカルフォルダ以下の所から) ******

# === モジュール ===

# ① import <dir>.<dir>….<module>

import package.sub_package.package_module1


# 呼び出し
package.sub_package.package_module1.func1()
package.sub_package.package_module1.func1()
del package.sub_package.package_module1

# ② from <dir>.<dir>… import <module> (複数選択可能)

from package.sub_package import package_module1, package_module2


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

from package.sub_package.package_module1 import func1, func2


# 呼び出し
func1()
func2()
del func1, func2
print()

# === モジュール内のオブジェクトを全て ===

# from <dir>.<dir>….<module> import *

from package.sub_package.package_module1 import *


# 呼び出し
func1()
func2()
del func1, func2
print()

# ****** 別名を付けてインポート ******

# === モジュール ===

import module1 as mod
import package.sub_package.package_module1 as pk
from package.sub_package import package_module2 as pk2


# 呼び出し
mod.func1()
pk.func1()
pk2.func1()
del mod, pk, pk2
print()

# === モジュール内のオブジェクト ===

from module1 import func1 as f
from package.sub_package.package_module1 import func1 as pk_f


# 呼び出し
f()
pk_f()
del f, pk_f
print()
