# === 変数、式を定義: ===
# sympy.symbol()

"""変数は以下のように sympy.symbol() で定義する"""

import sympy

x = sympy.Symbol('x')
y = sympy.Symbol('y')
print(type(x))

"""
・その変数を使って自由に数式を定義できる
・四則演算（+, -, *, /）、べき乗（**）などの演算子はPython標準のものを使う。
"""
expr = x**2 + y + 1
print(expr)

"""
変数の名称と sympy.symbol() の引数に渡す文字列は違っていてもいいが、
分かりにくくなるだけなので、
同じものにしておいたほうが無難
"""
z = sympy.Symbol('ZZZZ')
expr_z = z**2 + 3 * z
print(expr_z)

# === 変数に値を代入: ===
# subs()メソッド

"""
・定義した式の変数に値を代入したい場合は subs() メソッドを使う
・第一引数に対象の変数、第二引数に代入する値を指定する
・数値を代入したり、ほかの変数を代入したりできる
"""
print(expr)
print(expr.subs(x, 1))
print(expr.subs(x, y))

"""
複数の変数に値を代入する場合は、
(変数, 代入する値)のタプルのリストを引数に指定する
"""
print(expr.subs([(x, 1), (y, 2)]))

# === 式の展開: ===
# sympy.expand()

"""式を定義しただけだと自動的に展開されたりはしない"""
expr = (x + 1)**2
print(expr)

"""式を展開したい場合は sympy.expand() を使う"""
expr_ex = sympy.expand(expr)
print(expr_ex)

# === 因数分解: ===
# sympy.factor()

"""変数が複数あってもよい"""

print(expr_ex)
expr_factor = sympy.factor(expr_ex)
print(expr_factor)
print(sympy.factor(x**3 - x**2 - 3 * x + 3))
print(sympy.factor(x * y + x + y + 1))

# === 方程式を解く: ===
# sympy.solve()

"""
・方程式を解く（方程式の解を取得する）場合は sympy.solve() を使う
・sympy.solve(式)で 式 = 0 とした場合の解が取得できる
・平方根（ルート）は sqrt、虚数単位は I で表される（sqrt は square rootの略）
"""
print(sympy.solve(x**2 - 3 * x + 2))
print(sympy.solve(x**2 + x + 1))

"""
・複数の変数を含む式において、任意の変数に対して解を取得することもできる
・第二引数に対象の変数を指定する
"""
expr = x + y**2 - 4
print(sympy.solve(expr, x))
print(sympy.solve(expr, y))

# === 連立方程式を解く: ===
# sympy.solve()

"""
・連立方程式を解く場合も sympy.solve() を使う
・複数の式を含むリスト（またはタプル）を
  sympy.solve() の引数に指定すれば OK
"""
expr1 = 3 * x + 5 * y - 29
expr2 = x + y - 7
print(sympy.solve([expr1, expr2]))

# === 微分: ===
# sympy.diff()

print(sympy.diff(x**3 + 2 * x**2 + x))

"""
・複数の変数を含む式において、任意の変数に対して微分することもできる
・第二引数に対象の変数を指定する
"""
expr = x**3 + y**2 - y
print(sympy.diff(expr, x))
print(sympy.diff(expr, y))

# === 積分: ===
# sympy.integrate()

print(sympy.integrate(3 * x**2 + 4 * x + 1))

# === 三角関数、指数関数、対数関数などを使う ===

"""
・三角関数、指数関数、対数関数などは sympy.sin(), sympy.exp(), sympy.log()
  のように定義されている
・微分や積分も可能
"""

print(sympy.diff(sympy.cos(x)))
print(sympy.diff(sympy.exp(x)))
print(sympy.diff(sympy.log(x)))
print(sympy.integrate(sympy.cos(x)))
print(sympy.integrate(sympy.exp(x)))
print(sympy.integrate(sympy.log(x)))

"""
いちいち sympy. をつけるのが面倒な場合は、
以下のように各関数をimportしておけばよい
"""
import sympy
from sympy import sin, exp
x = sympy.Symbol('x')
print(sympy.diff(sin(x)))
print(sympy.diff(exp(x)))

"""
from sympy import *とすればすべての関数が sympy. なしで使えるが、
import * は何が import されるか分からないので、PEP8では推奨されていない
"""
