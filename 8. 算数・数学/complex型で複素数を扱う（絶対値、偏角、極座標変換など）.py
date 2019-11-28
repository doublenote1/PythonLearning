# === 複素数の変数を生成 ===

"""虚数単位をjで表し、以下のように記述する。iではないので注意"""
c = 3 + 4j
print(c)  # -> (3+4j)
print(type(c))  # -> <class 'complex'>

"""
・虚部が1の場合、省略するとエラー NameError になる
・もし j という名前の変数が先に定義されているとその変数と見なされてしまう
・1j と明示的に記述する必要がある
"""
try:
    c = 3 + j
except NameError as e:
    print(e)

c = 3 + 1j
print(c)

"""実部が 0 の場合は省略しても OK"""
c = 3j
print(c)

"""
・虚部が 0 の値を複素数 complex型として定義したい場合は 0 を明示的に記述する
・なお、後述のように complex型と整数 int型、浮動小数点 float型との演算も可能
"""
c = 3 + 0j
print(c)

"""
・実部、虚部は浮動小数点 float型で指定できる
・指数表記などでも OK
"""
c = 1.2e3 + 3j
print(c)

"""
・complex型のコンストラクタで生成することもできる
・complex(実部, 虚部) のように指定する
"""
c = complex(3, 4)
print(c)
print(type(c))

# === 複素数の実部と虚部を取得: ===
# real, imag属性

"""
・複素数 complex型の実部と虚部はそれぞれ real, imag属性で取得できる
・どちらも浮動小数点float型
"""
c = 3 + 4j
print(c.real)
print(type(c.real))
print(c.imag)
print(type(c.imag))

"""read onlyなので変更はできない"""
try:
    c.real = 5.5
except AttributeError as e:
    print(e)

# === 共役な複素数を取得: ===
# conjugate()メソッド

c = 3 + 4j
print(c.conjugate())

# === 複素数の絶対値（大きさ）を取得: ===
# abs()関数

c = 3 + 4j
print(abs(c))
c = 1 + 1j
print(abs(c))

# === 複素数の偏角（位相）を取得: ===
# math, cmathモジュール

"""
・cmath モジュールは複素数のための数学関数モジュール
・定義どおり逆正接関数 math.atan2() で算出するか、
  偏角（位相）を返す cmath.phase() を使う
"""

import cmath
import math

c = 1 + 1j
print(math.atan2(c.imag, c.real))
print(cmath.phase(c))
print(cmath.phase(c) == math.atan2(c.imag, c.real))

"""
・いずれの場合も、取得できる角度の単位はラジアン
・度に変換したい場合は、math.degrees() を使う
"""
print(math.degrees(cmath.phase(c)))

# === 複素数の極座標変換（極形式表現）: ===
# math, cmathモジュール

"""
上述のように、複素数の絶対値（大きさ）と偏角（位相）を取得できるが、
cmath.polar() を使うと(絶対値, 偏角)のタプルでまとめて取得できる
"""
c = 1 + 1j
print(cmath.polar(c))
print(type(cmath.polar(c)))
print(cmath.polar(c)[0] == abs(c))
print(cmath.polar(c)[1] == cmath.phase(c))

"""
・極座標から直交座標への変換は cmath.rect() を使う
・cmath.rect(絶対値, 偏角)のように引数を指定すると、
  等価な複素数complex型の値が取得できる
"""
print(cmath.rect(1, 1))
print(cmath.rect(1, 0))
print(cmath.rect(cmath.polar(c)[0], cmath.polar(c)[1]))

"""
実部と虚部は、絶対値と偏角から余弦 math.cos()、正弦math.sin()
で計算した結果と等価
"""
r = 2
ph = math.pi
print(cmath.rect(r, ph).real == r * math.cos(ph))
print(cmath.rect(r, ph).imag == r * math.sin(ph))

# === 複素数の計算（四則演算、べき乗、平方根） ===
"""通常の算術演算子を使って、四則演算、べき乗の計算が可能"""

c1 = 3 + 4j
c2 = 2 - 1j
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1 ** 3)

"""
平方根は **0.5 でも算出できるが、誤差が生じる
cmath.sqrt() を使うと正確な値が算出できる
"""
print((-3 + 4j) ** 0.5)
print((-1) ** 0.5)
print(cmath.sqrt(-3 + 4j))
print(cmath.sqrt(-1))

"""complex型 と int型、float型 との演算もできる"""
print(c1 + 3)
print(c1 * 0.5)
