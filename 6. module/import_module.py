# Import Module

## 同じフォルダか、パスの通ってるフォルダ内のモジュールをシンボルテーブルに入れる（複数選択可能）
import module
import module2

module.func1()  # -> func1
module.func2()  # -> func2
module2.mod2_func()  # -> mod2_func

# Module Name

print(module.__name__)  # -> module
print(module2.__name__)  # -> module2

## モジュール関数を変数に代入して使う

import module

substituted = module.func1
substituted()  # -> func1

## モジュール内の関数名のみを直接シンボルテーブルに入れる（複数選択可能）

from module import func1, func2

func1()  # -> func1
func2()  # -> func2

## モジュルー内の要素を全てシンボルテーブルに入れる

from module import *

func1()  # -> func1
func2()  # -> func2

## モジュール呼び出し時に、名前を変更し、シンボルテーブルに入れる

import module as mod

mod.func1()  # -> func1

## モジュール内の関数を呼び出し時に、名前を変更し、シンボルテーブルに入れる

from module import func1 as func

func()  # -> func1
print()

# Import Package

## 同じフォルダか、パスの通ってるフォルダからモジュール名までの階層をシンボルテーブルに入れる（複数選択可能）

import package.inner.package_module, package.inner.package_module2

package.inner.package_module.say_package()  # -> It'read_s called out of package !
package.inner.package_module.say_package2()  # -> It'read_s also called out of package !

## モジュール名のみをシンボルテーブルに入れる（複数選択可能）

from package.inner import package_module, package_module2

package_module.say_package()  # -> It'read_s called out of package !
package_module2.package_mod2_func()  # -> package_mod2_func

## モジュール内の関数名のみを直接シンボルテーブルに入れる（複数選択可能）

from package.inner.package_module import say_package, say_package2

say_package()  # -> It'read_s called out of package !
say_package2()  # -> It'read_s also called out of package !

## パッケージ内の__all__で定義されたモジュールを全てシンボルテーブルに入れる

from package.multiple_import import *

included_module.included()

print(dir())  # multiple_import パッケージから

## モジュルー内の要素を全てシンボルテーブルに入れる

from package.inner.package_module import *

say_package()  # -> It'read_s called out of package !
say_package2()  # -> It'read_s also called out of package !

## モジュール呼び出し時に、名前を変更し、シンボルテーブルに入れる

from package.inner import package_module as pm

pm.say_package()  # -> It'read_s called out of package !

## モジュール内の関数を呼び出し時に、名前を変更し、シンボルテーブルに入れる

from package.inner.package_module import say_package as sp

sp()  # -> It'read_s called out of package !

print()

# モジュール検索パス

import sys
from pprint import pprint

pprint(sys.path)
print()

# あるモジュールがどんな名前を定義しているか

print(dir(module))
print()

# このファイルが現在定義している、変数、モジュール、関数、その他の、すべての種類の名前

included = 'test'
print(dir())
print()
excluded = 'test'

# 組込み変数や組込み関数の名前

import builtins

print(dir(builtins))
print()
