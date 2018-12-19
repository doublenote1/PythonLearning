import numpy as np
import pandas as pd

l_2d = [[0, 1, 2], [3, 4, 5]]

# === NumPyを使う ===

"""
・元の二次元配列から NumPy 配列 ndarray を生成し、
  .T 属性で転置したオブジェクトを取得

・最終的に list型のオブジェクトが欲しい場合は、
  さらに tolist() メソッドで list に変換
"""
arr_t = np.array(l_2d).T
print(arr_t)
print(type(arr_t))
print()

l_2d_t = np.array(l_2d).T.tolist()
print(l_2d_t)
print(type(l_2d_t))
print()

# === pandas.DataFrameを使う ===

"""
・元の二次元配列から pandas.DataFrame を生成し、
  .T 属性で転置したオブジェクトを取得

・最終的に list型のオブジェクトが欲しい場合は、
  values 属性で numpy.ndarray を取得、
  さらに tolist() メソッドでlistに変換
"""

df_t = pd.DataFrame(l_2d).T
print(df_t)
print(type(df_t))
print()

l_2d_t = pd.DataFrame(l_2d).T.values.tolist()
print(l_2d_t)
print(type(l_2d_t))
print()

# === 組み込み関数 zip() で転置 ===

l_2d_t_tuple = list(zip(*l_2d))
print(l_2d_t_tuple)
print(type(l_2d_t_tuple))
print()

l_2d_t = [list(x) for x in zip(*l_2d)]
print(l_2d_t)
print(type(l_2d_t))
print()

"""
* でリストの要素が展開され、
展開した要素が zip() 関数でまとめられ、
さらに、リスト内包表記でタプルがリストに変換される
"""

print(*l_2d)
print(list(zip([0, 1, 2], [3, 4, 5])))
print([list(x) for x in [(0, 3), (1, 4), (2, 5)]])
