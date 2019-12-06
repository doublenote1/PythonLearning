import math

# === 円周率（パイ）: math.pi ===

print(math.pi)

# === 角度変換（ラジアン、度）: ===
# math.degrees(), math.radians()

"""
・math モジュールの三角関数および逆三角関数は、
  角度の単位としてラジアンを使う
・ラジアン（弧度法）と度（度数法）を相互に変換するには
  math.degrees() と math.radians() を使う
・ラジアンから度に変換するのが math.degrees()
・度からラジアンに変換するのがmath.radians()
"""

print(math.degrees(math.pi))
print(math.radians(180))

# === 正弦、逆正弦: ===
# math.sin(), math.asin()

"""
・正弦（サイン、sin）を求める関数は math.sin()
・逆正弦（アークサイン、arcsin）を求める関数はmath.asin()
"""
sin30 = math.sin(math.radians(30))
print(sin30)

"""
・30度の正弦は0.5だが、
  プログラムでは無理数である円周率を正確に計算できないので誤差が生じる
・適当な桁数で四捨五入したい場合は、
  round() 関数か、print() での表示時に
  format() メソッドまたは format() 関数で丸めればOK。
"""
sin30_round = round(sin30, 3)
print(sin30_round)
print('{:.3}'.format(sin30))
print(format(sin30, '.3'))

"""
・0.5の逆正弦を求める例を示す
・math.asin() が返すのはラジアンなので、
  最後に math.degrees() で度に変換している
"""
asin05 = math.degrees(math.asin(0.5))
print(asin05)
asin05_round = round(asin05, 3)
print(asin05_round)

# === 余弦、逆余弦: ===
# math.cos(), math.acos()

"""
・余弦（コサイン、cos）を求める関数は math.cos()
・逆余弦（アークコサイン、arccos）を求める関数は math.acos()
・60度の余弦と0.5の逆余弦を求める例を示す。
"""
cos60 = math.cos(math.radians(60))
print(cos60)
acos05 = math.degrees(math.acos(0.5))
print(acos05)

# === 正接、逆正接: ===
# math.tan(), math.atan(), math.atan2()

"""
・正接（タンジェント、tan）を求める関数は math.tan()
・逆正接（アークタンジェント、arctan）を求める関数は math.atan() または math.atan2()
・45度の正接と1の逆正接を求める例を示す。
"""
tan45 = math.tan(math.radians(45))
print(tan45)
atan1 = math.degrees(math.atan(1))
print(atan1)

# === math.atan() とmath.atan2() の違い ===

"""
・math.atan() と math.atan2() はどちらも逆正接を返す関数だが、
  引数と戻り値の範囲が異なる
・math.atan(x) は引数が一つで、arctan(x) をラジアンで返す
・戻り値は -pi / 2 から pi / 2（-90度から90度）の間になる
"""
print(math.degrees(math.atan(1)))
print(math.degrees(math.atan(-1)))
print(math.degrees(math.atan(math.inf)))
print(math.degrees(math.atan(-math.inf)))

"""
・上の例の math.inf は無限大を表す（Python3.5で追加）。
・math.atan2(y, x) は引数が二つで、arctan(y / x) をラジアンで返す
・この角度は、極座標平面において原点から座標(x, y) へのベクトルが
  x 軸の正の方向となす角度であり、戻り値は -pi から pi（-180度から180度）の間になる
・第2象限、第3象限での角度も正しく取得できるので、
  極座標平面で考える場合は math.atan() よりも math.atan2() のほうが適当
・引数の順番が x, y ではなく y, x なので注意
"""

print(math.degrees(math.atan2(1, 1)))
print(math.degrees(math.atan2(1, -1)))
print(math.degrees(math.atan2(-1, -1)))
print(math.degrees(math.atan2(-1, 1)))

"""なお、x 軸の負の無限大は pi（180度）を返す"""
print(math.degrees(math.atan2(0, -math.inf)))
